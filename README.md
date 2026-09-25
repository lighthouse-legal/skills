# Lighthouse skills for personal injury firms

**Put your AI assistant to work on your firm's marketing.** These free skills give it a repeatable process for reviewing Google Ads and researching local competitors. You get a report to discuss with your team or agency.

| Skill | What it does | What you provide |
| --- | --- | --- |
| [Google Ads audit](skills/pi-google-ads-audit/) | Explains where ad spend goes, checks what counts as a conversion, and prioritizes improvements. | Google Ads reports from you or your agency. |
| [Competitive research](skills/pi-competitive-research/) | Compares local firms' websites and messaging, with sources and ideas to test. | Your website, city, and priority case types. |

**Use ChatGPT in your browser?** Start with the no-install guide for [Google Ads](skills/pi-google-ads-audit/#use-in-chatgpt-no-installation) or [competitive research](skills/pi-competitive-research/#use-in-chatgpt-no-installation). No terminal or GitHub account needed.

## Recommended installation: skills.sh

For **Codex, Claude Code, and other supported apps**, open your computer's Terminal (macOS) or PowerShell (Windows) and run:

```sh
npx skills add lighthouse-legal/skills --global
```

Select the skills you want. If asked which apps to use, choose yours; Codex may already appear as included. Follow the install prompts. `--global` makes them available across your workspaces. You need [Node.js](https://nodejs.org/en/download) and [Git](https://git-scm.com/downloads); your IT team can handle this once. You do not need to clone this repository or create a GitHub account. [Setup help](docs/installation.md).

This command installs into supported apps on your computer. For ChatGPT's browser chat or Claude's regular chat app, use the instructions in each skill's guide instead.

After installation, start a new task and paste the first-report prompt from the [Ads guide](skills/pi-google-ads-audit/#your-first-report) or [competitor guide](skills/pi-competitive-research/#your-first-report).

## Free from Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms: answering calls, gathering the information each firm needs, and connecting priority callers with its team. These tools help with other parts of the business and require no Lighthouse account.

Your AI provider's plan and usage limits apply. The skills make recommendations; they do not change your ads or contact competitors. Reports are not sent to Lighthouse by these tools.

[Alternative ZIP downloads](https://github.com/lighthouse-legal/skills/releases/latest) · [Test results](evals/README.md) · [MIT license](LICENSE) · [Contributing](CONTRIBUTING.md)
