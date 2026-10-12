#!/usr/bin/env python3
"""Build deterministic skill ZIPs and single-file guides for ordinary AI chats."""

import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_SUFFIXES = {".md", ".py", ".yaml", ".csv", ".json"}


def chat_guide(skill_name, files):
    """Reuse approved skill resources, so chat users need only one attachment."""
    title = skill_name.replace("-", " ").title()
    parts = [
        f"# Lighthouse {title}: chat guide\n\n"
        "Attach this complete text file to a new AI chat with your task and inputs. "
        "You do not need to read or edit it. This supplies instructions for this "
        "conversation; it does not install a skill or connect an account.\n\n"
        "## Instructions for the assistant\n\n"
        "Follow the bundled SKILL.md for the user's task. Each supporting file is "
        "included below between BEGIN FILE and END FILE markers. When the workflow "
        "refers to a relative file, read that embedded section; do not ask the user "
        "to upload those supporting files separately. The file list is below.\n\n"
        "Confirm which user inputs you can actually read, then proceed with the "
        "workflow. Example firms, CSVs, and findings in this guide are fictional "
        "illustrations, never evidence about the user's firm. External sources "
        "still require web access. If you lack it, disclose that and use the "
        "workflow's supplied-evidence fallback.\n\n"
        "If calculation tools are available, you may extract the embedded Python "
        "helper into your private analysis environment and run it on the user's "
        "compatible exports. Otherwise use available calculation tools under the "
        "same reconciliation rules. Do not claim that the bundled helper ran "
        "unless it did. If you cannot inspect and calculate the reports reliably, "
        "give a preliminary checklist and state what is missing.\n\n"
        "The guide does not authorize account changes, contacting anyone, or "
        "sending reports to Lighthouse. The user's task determines scope.\n\n"
        "## Bundled files\n"
    ]
    resources = []
    for name, data in files:
        relative = str(Path(name).relative_to(skill_name))
        if relative == "README.md" or relative.startswith("agents/"):
            continue
        resources.append((relative, data.decode("utf-8")))
    parts.extend(f"- {name}\n" for name, _ in resources)
    for name, content in resources:
        parts.append(f"\n===== BEGIN FILE: {name} =====\n{content}\n===== END FILE: {name} =====\n")
    return "".join(parts)


def package_all(destination=None, source_root=ROOT):
    source_root = Path(source_root)
    destination = Path(destination or ROOT / "dist")
    destination.mkdir(parents=True, exist_ok=True)
    result = []
    checksums = []
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
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        result.append((archive, digest))
        checksums.append((archive, digest))
        guide = destination / f"{skill.name}-chat-guide.txt"
        guide.write_text(chat_guide(skill.name, files), encoding="utf-8", newline="\n")
        checksums.append((guide, hashlib.sha256(guide.read_bytes()).hexdigest()))
    (destination / "SHA256SUMS").write_text("".join(f"{digest}  {path.name}\n" for path, digest in checksums))
    return result


if __name__ == "__main__":
    for archive, digest in package_all():
        print(f"{archive.name}: {digest}")
