#!/usr/bin/env python3
"""Validate this repository's portable skill structure and local Markdown links."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    skills = sorted((ROOT / "skills").iterdir())
    for skill in skills:
        if not skill.is_dir():
            continue
        main = skill / "SKILL.md"
        if not main.exists():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        text = main.read_text()
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{skill.name}: missing YAML frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z-]+): (.+)$", match.group(1), re.M))
        if fields.get("name") != skill.name or not re.fullmatch(r"[a-z0-9-]{1,64}", skill.name):
            errors.append(f"{skill.name}: invalid or mismatched name")
        if not 20 <= len(fields.get("description", "")) <= 1024:
            errors.append(f"{skill.name}: invalid description length")
        if len(text.splitlines()) > 500:
            errors.append(f"{skill.name}: SKILL.md exceeds 500 lines; move detail to references")
        if not (skill / "README.md").exists():
            errors.append(f"{skill.name}: missing user README")
        for path in skill.rglob("*"):
            if path.is_symlink():
                errors.append(f"{path.relative_to(ROOT)}: symlinks are not portable")
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts or "dist" in md.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", md.read_text()):
            if re.match(r"[a-z]+:|#", target):
                continue
            target = target.split("#", 1)[0].strip("<>")
            if target and not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken local link {target}")
        if md.name == "SKILL.md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", md.read_text()):
                if target.startswith("../"):
                    errors.append(f"{md.relative_to(ROOT)}: runtime reference escapes skill folder")
    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("Skill metadata, structure, portable references, and local Markdown links passed.")
