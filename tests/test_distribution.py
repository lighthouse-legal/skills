import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_skills", ROOT / "scripts/package_skills.py")
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)


class DistributionTests(unittest.TestCase):
    def test_individual_archives_are_portable_complete_and_repeatable(self):
        with tempfile.TemporaryDirectory() as directory:
            first = PACKAGE.package_all(directory)
            for path, _ in first:
                name = path.stem
                with zipfile.ZipFile(path) as archive:
                    members = archive.namelist()
                    self.assertIn(f"{name}/SKILL.md", members)
                    self.assertIn(f"{name}/README.md", members)
                    self.assertIn(f"{name}/LICENSE", members)
                    self.assertTrue(all(member.startswith(name + "/") for member in members))
                    self.assertFalse(any(".." in Path(member).parts for member in members))
                    self.assertFalse(any("__pycache__" in member or "/." in member for member in members))
                    self.assertIsNone(archive.testzip())
                    archive.extractall(Path(directory) / "installed")
                    for member in members:
                        if not member.endswith(".md"):
                            continue
                        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", archive.read(member).decode()):
                            if re.match(r"[a-z]+:|#", target):
                                continue
                            target = target.split("#", 1)[0]
                            resolved = Path(directory) / "installed" / Path(member).parent / target
                            self.assertTrue(resolved.exists(), f"Missing packaged reference: {member}: {target}")
            installed = Path(directory) / "installed/pi-google-ads-audit"
            run = subprocess.run(
                [sys.executable, str(installed / "scripts/summarize_ads_csv.py"),
                 str(installed / "examples/campaigns.csv"), "--currency", "USD"],
                cwd=directory, capture_output=True, text=True, check=True,
            )
            self.assertEqual(json.loads(run.stdout)["totals"]["cost"], "8000.00")
            second = PACKAGE.package_all(directory)
            self.assertEqual(first, second)
            self.assertEqual(len(first), 2)

    def test_unlisted_private_files_never_enter_a_package(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills/test-skill"
            skill.mkdir(parents=True)
            for name in ("SKILL.md", "README.md"):
                (skill / name).write_text("# Public documentation\n")
            (root / "LICENSE").write_text("Synthetic test license")
            (root / "distribution.json").write_text(json.dumps({"test-skill": ["SKILL.md", "README.md"]}))
            for name in (".private/account.csv", "private/account.csv", "reports/report.json",
                         "examples/customer.csv", "references/.credentials.json"):
                path = skill / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("synthetic private sentinel")
            packages = PACKAGE.package_all(root / "dist", source_root=root)
            with zipfile.ZipFile(packages[0][0]) as archive:
                self.assertEqual(set(archive.namelist()),
                                 {"test-skill/SKILL.md", "test-skill/README.md", "test-skill/LICENSE"})

    def test_manifest_rejects_traversal_hidden_and_symlink_members(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills/test-skill"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("# Skill")
            (skill / "README.md").write_text("# Readme")
            (root / "LICENSE").write_text("Synthetic test license")
            (root / "secret.json").write_text("synthetic secret sentinel")
            (skill / "linked.json").symlink_to(root / "secret.json")
            for member in ("../../secret.json", ".private/account.csv", "private/account.csv", "linked.json"):
                (root / "distribution.json").write_text(json.dumps({"test-skill": ["SKILL.md", "README.md", member]}))
                with self.subTest(member=member), self.assertRaises(ValueError):
                    PACKAGE.package_all(root / "dist", source_root=root)


if __name__ == "__main__":
    unittest.main()
