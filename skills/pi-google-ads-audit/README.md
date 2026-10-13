# Google Ads audit for personal injury firms

Understand where your ad budget goes and what results it produces. This guide helps your AI assistant review your reports and prepare useful questions for your agency.

## Installation

<a id="use-in-chatgpt-no-installation"></a>
<a id="your-first-report"></a>
<a id="use-in-claude-chat"></a>

### No Install Setup

Open a new ChatGPT chat, or another AI assistant that can open web links. Paste this:

```text
Help me review my Google Ads spending. Read this guide and ask any setup questions you need:
https://raw.githubusercontent.com/lighthouse-legal/skills/main/skills/pi-google-ads-audit/SKILL.md
```

Answer its questions about your firm and share the reports it asks for. You do not need to connect your Google account. If you are unsure about a question, say so—the assistant will help you work through it.

If it cannot open the guide, see [setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#the-assistant-cannot-open-the-link).

<a id="install-with-skillssh-recommended"></a>

### Install with skills.sh

For Codex, Claude Code, or another supported app, run this in Terminal on Mac or PowerShell on Windows:

```sh
npx skills add lighthouse-legal/skills --skill pi-google-ads-audit --global
```

Choose your app if asked. Start a new task and say: **“Use pi-google-ads-audit to review my ad spending. Ask me what you need.”** [Installation help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#install-with-skillssh).

## What you will need

Start with a Google Ads campaign report. This shows what you spent and the results Google recorded. A spreadsheet file ending in `.csv` works well. Your agency's monthly PDF can also be a starting point.

The assistant will ask what counts as a **conversion**. That is an action Google records, such as a form submission or a click on your phone number. It does not always mean a new client. It is fine to answer “I'm not sure.”

### Get reports from your agency

Copy this request to the person who manages your ads:

```text
Please send a campaign report as a CSV for the last 30 complete days.
Include all campaigns that spent money, even if now paused, with cost,
clicks, impressions, and Conversions. Please note the dates, currency,
time zone, and any filters, and explain what each conversion counts.

If available, also send a search-terms report for the same dates and
campaigns. Please leave out client names and contact details.
```

## What you will get

- A summary of your spending and reported results.
- Findings supported by your reports, with any missing information explained.
- Practical next steps and questions for your agency.

The skill reviews your account data. It does not change your campaigns.

<a id="try-an-example-first"></a>

[See a fictional example report](examples/sample-findings.md), or explore the [report details](references/exports-and-math.md) and [optional Google Ads connections](references/account-access.md).

## From Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms. This skill is free and needs no Lighthouse account. Your AI provider's usual limits apply; reports are not sent to Lighthouse.

[Setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md) · [Test results](https://github.com/lighthouse-legal/skills/blob/main/evals/README.md)
