# Lighthouse skills for personal injury firms

A skill is a guide your AI assistant follows. These free skills help personal injury firms review Google Ads and compare local competitors.

| Skill | What it helps you do |
| --- | --- |
| [Google Ads audit](skills/pi-google-ads-audit/README.md) | Understand your ad spending and prepare questions for your agency. |
| [Competitive research](skills/pi-competitive-research/README.md) | Compare local firms and find ways to improve your marketing. |

<a id="recommended-installation-skillssh"></a>

## Installation

### No Install Setup

Open a new ChatGPT chat, or another AI assistant that can open web links. Copy one of these prompts, including the link.

**Google Ads audit**

```text
Help me review my Google Ads spending. Read this guide and ask any setup questions you need:
https://raw.githubusercontent.com/lighthouse-legal/skills/main/skills/pi-google-ads-audit/SKILL.md
```

**Competitive research**

```text
Help me compare my firm with local competitors. Read this guide and ask any setup questions you need:
https://raw.githubusercontent.com/lighthouse-legal/skills/main/skills/pi-competitive-research/SKILL.md
```

Then answer the assistant's questions. It will tell you what information to share. If it cannot open the guide, see [setup help](docs/installation.md#the-assistant-cannot-open-the-link).

### Install with skills.sh

For Codex, Claude Code, or another supported app, open Terminal on Mac or PowerShell on Windows and run:

```sh
npx skills add lighthouse-legal/skills --global
```

Choose your skills and app if asked. Then start a new task and ask to use the skill. [Installation help](docs/installation.md#install-with-skillssh).

## From Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms. We help firms answer calls, gather case details, and connect callers with their team.

These skills are free and work without a Lighthouse account. Your AI provider's usual limits apply. The skills make recommendations; they do not change your accounts or send reports to Lighthouse.

[Test results](evals/README.md) · [Other download options](https://github.com/lighthouse-legal/skills/releases/latest) · [MIT license](LICENSE) · [Contributing](CONTRIBUTING.md)
