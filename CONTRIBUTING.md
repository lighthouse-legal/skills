# Contributing

Useful improvements include clearer instructions, new synthetic failure cases, corrected provider setup guidance, and better evidence handling. Open an issue describing the problem, or send a focused pull request. Include the agent/client version, the relevant skill version, and a small fictional input that reproduces the issue.

Do not include real customer exports, account IDs, credentials, client records, call recordings, or private research reports. Replace identifying details and business figures with synthetic data before sharing. The repository's skills never require a Lighthouse account and should remain useful without one.

## Local checks

Python 3.10+; no packages to install:

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
python3 scripts/package_skills.py
```

The last command writes one ZIP and one single-file chat guide per skill to ignored `dist/`, with checksums for all four downloads. Inspect them before release. Chat guides embed the canonical instructions and resources so ordinary chat users need only one attachment; they exclude the human README and agent display metadata. Do not hand-edit generated guides. Only the files explicitly listed in [distribution.json](distribution.json), plus the license, are distributed. Update that manifest when adding an intended resource; unlisted files are never collected. Hidden/private paths and symlinks are rejected even if listed. Private test outputs belong outside this checkout.

Instruction changes need a fresh-agent evaluation as well as structural checks. Give the evaluator the task, complete skill folder, and raw inputs without the expected answer or author commentary. Review whether the actual result helps the user, cites inspected evidence, calculates correctly, and handles missing data. Record failures and fixes. See [the evaluation guide](evals/README.md).

Prefer small dependency-free helpers when they make an important calculation repeatable. Keep the core `SKILL.md` concise and put detailed reference material in the skill folder. Document platform-specific instructions from current primary sources, distinguishing documentation checks from installs actually executed.
