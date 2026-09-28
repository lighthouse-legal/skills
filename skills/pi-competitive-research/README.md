# Competitive research for personal injury firms

See how your firm compares with local competitors. This guide helps your AI assistant compare websites and messaging, then suggest ways to improve your marketing.

## Installation

<a id="use-in-chatgpt-no-installation"></a>
<a id="your-first-report"></a>
<a id="use-in-claude-chat"></a>

### No Install Setup

Open a new ChatGPT chat, or another AI assistant that can open web links. Paste this:

```text
Help me compare my firm with local competitors. Read this guide and ask any setup questions you need:
https://raw.githubusercontent.com/lighthouse-legal/skills/main/skills/pi-competitive-research/SKILL.md
```

Answer its questions about your website, city, and the cases you want. You can name competitors, or let the assistant find them. You do not need an advertising account.

If it cannot open the guide, see [setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#the-assistant-cannot-open-the-link).

<a id="install-with-skillssh-recommended"></a>

### Install with skills.sh

For Codex, Claude Code, or another supported app, run this in Terminal on Mac or PowerShell on Windows:

```sh
npx skills add lighthouse-legal/skills --skill pi-competitive-research --global
```

Choose your app if asked. Start a new task with web access and say: **“Use pi-competitive-research to compare my firm with local competitors. Ask me what you need.”** [Installation help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#install-with-skillssh).

## What you will get

- A comparison of your firm and up to five relevant competitors.
- Links showing where each finding came from.
- Three to five ideas to test in your own marketing.

The report covers the cases firms promote, where they operate, and how people can contact them. It can also compare language options and published opening hours.

Where available, the assistant checks ads and local search results. If a page or listing is blocked, it explains the gap and continues with the information it can read.

Public information cannot reveal competitors' budgets or prove how well they serve clients. The skill does not call firms or submit their contact forms.

[See a fictional example report](examples/synthetic-report.md).

## From Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms. This skill is free and needs no Lighthouse account. Your AI provider's usual limits apply.

[Setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md) · [Test results](https://github.com/lighthouse-legal/skills/blob/main/evals/README.md)
