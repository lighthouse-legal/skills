#!/usr/bin/env python3
"""Build clean, deterministic, single-folder skill ZIPs; never append to old ZIPs."""

import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_SUFFIXES = {".md", ".py", ".yaml", ".csv", ".json"}


def package_all(destination=None, source_root=ROOT):
    source_root = Path(source_root)
    destination = Path(destination or ROOT / "dist")
    destination.mkdir(parents=True, exist_ok=True)
    result = []
    manifest = json.loads((source_root / "distribution.json").read_text())
    for skill_name, members in sorted(manifest.items()):
        if not re.fullmatch(r"[a-z0-9-]{1,64}", skill_name):
            raise ValueError(f"Invalid skill name: {skill_name}")
        if not isinstance(members, list) or not {"SKILL.md", "README.md"}.issubset(members):
            raise ValueError(f"Missing required distribution members: {skill_name}")
        if len(members) != len(set(members)):
            raise ValueError(f"Duplicate distribution members: {skill_name}")
        skill = source_root / "skills" / skill_name
        if skill.is_symlink():
            raise ValueError(f"Refusing symlink: {skill}")
        files = []
        for member in sorted(members):
            relative = Path(member)
            if relative.is_absolute() or any(part.startswith(".") or part in
                {"private", "reports", "eval-runs", "dist", "__pycache__"}
                for part in relative.parts) or "\\" in member:
                raise ValueError(f"Unsafe distribution path: {member}")
            path = skill / relative
            if any((skill / Path(*relative.parts[:i])).is_symlink()
                   for i in range(1, len(relative.parts) + 1)):
                raise ValueError(f"Refusing symlink: {path}")
            if not path.is_file() or path.suffix not in ALLOWED_SUFFIXES:
                raise ValueError(f"Missing or unexpected distribution file: {path}")
            files.append((str(Path(skill.name) / relative), path.read_bytes()))
        files.append((f"{skill.name}/LICENSE", (source_root / "LICENSE").read_bytes()))
        archive = destination / f"{skill.name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
            for name, data in sorted(files):
                info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                output.writestr(info, data)
        result.append((archive, hashlib.sha256(archive.read_bytes()).hexdigest()))
    (destination / "SHA256SUMS").write_text("".join(f"{digest}  {path.name}\n" for path, digest in result))
    return result


if __name__ == "__main__":
    for archive, digest in package_all():
        print(f"{archive.name}: {digest}")
