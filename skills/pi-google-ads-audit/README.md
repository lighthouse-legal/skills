# Google Ads audit for personal injury firms

**Walk into your next agency meeting knowing what to ask.** Give your AI assistant your Google Ads reports. It will explain where your budget goes, what the reported results mean, and which improvements deserve attention first.

| You provide | You get |
| --- | --- |
| Campaign report + a description of what Google counts as a conversion | A spending review, measurement concerns, and questions for your agency. |
| Search-terms report, if available | A closer look at the searches your firm is paying for. |

**Choose your starting point:** [Install with skills.sh](#install-with-skillssh-recommended) · [Use in ChatGPT without installing](#use-in-chatgpt-no-installation) · [Use in Claude chat](#use-in-claude-chat)

Free to use. No Lighthouse account or Google account connection required. Your AI provider's usual plan and usage limits apply.

## Install with skills.sh (recommended)

Use this if you work in **Codex, Claude Code, or another supported app on your computer**. Open Terminal on macOS or PowerShell on Windows and run:

```sh
npx skills add lighthouse-legal/skills --skill pi-google-ads-audit --global
```

If the installer asks which apps to use, choose yours; Codex may already appear as included. Complete the prompts. Start a new task in that app, add your reports, and paste [the prompt below](#your-first-report). If `npx` is not recognized, see [installation help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md). No GitHub account or manual ZIP download is needed.

Using ChatGPT at chatgpt.com? Follow the next section instead; a terminal installation does not add a skill to a browser chat.

## Use in ChatGPT (no installation)

1. **[Download the Google Ads chat guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-google-ads-audit-chat-guide.txt).** It is one text file containing the full workflow. You do not need to read or edit it.
2. **[Open a new ChatGPT chat](https://chatgpt.com/)** and use the attachment button beside the message box to add the guide and your Ads reports. A spreadsheet export ending in `.csv` works well.
3. **Paste the prompt below**, replace the bracketed details, and send it.

The guide applies to this conversation. Attach it again when starting a new chat. [Having trouble attaching it?](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#troubleshooting)

## Your first report

Paste this into your AI assistant after installing the skill **or** attaching the chat guide and reports:

```text
Use the pi-google-ads-audit skill or attached Google Ads chat guide.

Our firm: [name]
Market: [city and state]
Cases we want: [for example, car accidents and truck accidents]
Cases we do not take: [list, or say none]
Our reported conversions mean: [calls, forms, other, or not sure]
Report dates, currency, and time zone: [include if known]

First confirm you can read the guide or installed skill, then name
the reports you can read and their date ranges.
Then review our spending and measurement. Give me the most useful
findings, the evidence for each, and questions for our agency.
If information is missing, tell me what you can conclude and ask
only for what would change the advice. Do not change the account.
```

**A useful result:** a short summary, a table of spending and reported outcomes, findings tied to your data, and next steps for your team. The assistant should explain whether a “conversion” means a phone-button click, an inquiry, or something closer to a qualified case. It should label gaps rather than fill them with guesses.

## Get the reports from your agency

You can copy this request to whoever manages your Google Ads account:

```text
Please send a campaign performance CSV for the last 30 complete days,
including all campaigns that spent money, even if now paused.
Include campaign name/ID, campaign type, status, cost, clicks,
impressions, and Conversions. Please note the exact dates, account
currency, time zone, and any filters.

Please also explain the conversion actions: what each counts,
which are used for bidding, and whether repeat actions count.
A screenshot or written explanation is fine to start.

If available, include a search-terms CSV for the same dates and
campaigns, with search term, campaign/ad group, cost, clicks, and
Conversions. No client names, contact details, or call recordings.
```

The campaign report and conversion explanation are enough to begin. The search-terms report helps investigate relevance. If you manage the account yourself, use the download control above the Google Ads campaign table after selecting the reporting dates. See the [export guide](references/exports-and-math.md) for columns and calculation details.

## Try an example first

Use the fictional [firm details](examples/firm-context.md), [campaign report](examples/campaigns.csv), and [search-terms report](examples/search-terms.csv). On a GitHub file page, use **Download raw file** to save each input. Attach those three files along with the chat guide, or give them to your installed agent, and ask it to audit the fictional firm. No live account is needed. [Sample findings](examples/sample-findings.md) show the kind of output to expect; they are not an input to the audit.

## Use in Claude chat

For Claude's regular web or desktop chat, the quickest trial is the same [single chat guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-google-ads-audit-chat-guide.txt): attach it with your reports, then send the first-report prompt. File analysis and calculation availability depend on your account settings.

For a reusable Claude skill, download the [skill ZIP](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-google-ads-audit.zip). Enable **Code execution and file creation**, then open **Customize → Skills → + → Create skill → Upload a skill**. Upload and enable the ZIP, start a new chat, and ask for `pi-google-ads-audit`. See [Claude's current instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Claude Code uses the skills.sh command above.

## Common questions

**Will it change my campaigns?** No. It reviews evidence and proposes actions for you or your agency.

**Do I need to connect Google Ads?** No. Start with exported reports. An existing authorized browser connection or Google's Ads MCP can be used instead. [Optional connection setup](references/account-access.md).

**I only have my agency's monthly PDF.** Start with that. Ask the assistant to confirm which tables it can read and give a preliminary review. CSV exports allow a more complete, reproducible calculation; use the agency request above when you need them.

**What if I do not know my conversion setup?** Say “not sure.” The assistant can begin with the available reports and explain the measurement questions to resolve.

**Does it tell me my cost per signed case?** Only when you supply evidence that actually measures signed cases. A reported conversion is not automatically a qualified lead or a client.

**The assistant cannot find the installed skill.** Start a new task and ask for `pi-google-ads-audit` by name. In Codex, you can type `$pi-google-ads-audit`; in Claude Code, `/pi-google-ads-audit`. [More setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md).

**Where does my data go?** Files you attach go to your chosen AI provider under its data controls. This skill does not send reports to Lighthouse. Keep client details and account exports out of public GitHub issues.

## Technical details and limits

The skill works with exports, an authorized browser, or a separately configured [Google Ads MCP](https://github.com/googleads/google-ads-mcp). Installing it supplies instructions, not account access. Missing Local Services Ads, listings, call recordings, or CRM data does not block an Ads review.

The optional [CSV helper](scripts/summarize_ads_csv.py) needs Python 3.10+ with no external packages. It preserves fractional conversions, recomputes ratios from totals, and separates summary rows. It supports common English headers and several formats, not every export. Its JSON preserves original cells, so treat its output as private. [Formats and usage](references/exports-and-math.md).

No universal “good PI CPA,” guaranteed savings, broad-match ban, or compliance certification is built in. Reports depend on the available evidence and the agent running the workflow. [Test results](https://github.com/lighthouse-legal/skills/blob/main/evals/README.md) distinguish executed tests from documented installation options; hosted ChatGPT/Claude uploads and live MCP integration remain unverified.

## From Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms. We publish free tools for other parts of running a firm, too. This skill is MIT licensed and works without a Lighthouse account.
