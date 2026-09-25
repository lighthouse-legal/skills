# Competitive research for personal injury firms

**See how your firm compares with local competitors—and what to improve next.** Give your AI assistant your website, city, and priority case types. It will compare public messaging, show its sources, and suggest changes worth testing.

| You provide | You get |
| --- | --- |
| Your website, target city, and case types | A comparison with up to five relevant firms. |
| Competitor names, if you have them | A closer look at the firms you care about. Otherwise, the assistant selects and explains a relevant set. |

**Choose your starting point:** [Install with skills.sh](#install-with-skillssh-recommended) · [Use in ChatGPT without installing](#use-in-chatgpt-no-installation) · [Use in Claude chat](#use-in-claude-chat)

Free to use. No Lighthouse account, advertising account, or paid research subscription required. Your AI provider's usual plan and usage limits apply.

## Install with skills.sh (recommended)

Use this if you work in **Codex, Claude Code, or another supported app on your computer**. Open Terminal on macOS or PowerShell on Windows and run:

```sh
npx skills add lighthouse-legal/skills --skill pi-competitive-research --global
```

If the installer asks which apps to use, choose yours; Codex may already appear as included. Complete the prompts. Start a new task with web access and paste [the prompt below](#your-first-report). If `npx` is not recognized, see [installation help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md). No GitHub account or manual ZIP download is needed.

Using ChatGPT at chatgpt.com? Follow the next section instead; a terminal installation does not add a skill to a browser chat.

## Use in ChatGPT (no installation)

1. **[Download the competitive research chat guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-competitive-research-chat-guide.txt).** It is one text file containing the full workflow. You do not need to read or edit it.
2. **[Open a new ChatGPT chat](https://chatgpt.com/)** and use the attachment button beside the message box to add the guide. Choose a chat with web search or research available so it can inspect current websites.
3. **Paste the prompt below**, replace the bracketed details, and send it. You do not need to collect competitor websites first.

The guide applies to this conversation. Attach it again when starting a new chat. [Having trouble attaching it?](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md#troubleshooting)

## Your first report

```text
Use the pi-competitive-research skill or attached competitive
research chat guide.

Our website: [https://your-firm.com]
Market: [city, state, country]
Priority cases: [for example, car accidents and truck accidents]
Decision: What should we improve in our website messaging?
Competitors: Choose up to five relevant local firms and explain why.
Languages to consider: [optional]

Confirm that you can read the guide or installed skill and access
current websites. Compare our firm with the selected competitors.
Give me a short summary, comparison table, three to five ideas to
test, and links to the evidence. Be clear about what you could not
check. Do not contact anyone or change any accounts.
```

**A useful result:** a report you can discuss with your marketing team, covering practice-area focus, local presence, language claims, contact options, and published availability. If advertising or search results are visible, those observations appear separately with their limitations.

For example, a competitor's Spanish page might prompt you to explain your own Spanish intake more clearly—after confirming your team offers it. It does not prove an untapped market or that the competitor has better service.

## What the assistant researches

The default comparison covers your firm and up to five others in one market, focused on up to three case types. It reviews comparable home, practice/location, and contact pages, then records the source and date for each material observation.

Where accessible, it checks Paid Search, Local Services Ads, Maps/local results, and organic search separately. Google results vary by location and session, so a small sample is not a permanent ranking. If ads or listings cannot be inspected, you still receive the website comparison.

Public reviews are optional. If used, the report describes which reviews were sampled and how limited that sample is. It does not treat a handful of visible reviews as representative of every client.

You do not need an advertising export. Your own Auction Insights report can add context if you already have one, but it cannot reveal competitors' actual budgets or profits. [Optional export guidance](references/auction-insights.md).

## Use in Claude chat

For Claude's regular web or desktop chat, attach the same [single chat guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-competitive-research-chat-guide.txt), enable web search if available, and send the first-report prompt.

For a reusable Claude skill, download the [skill ZIP](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-competitive-research.zip). Enable **Code execution and file creation**, then open **Customize → Skills → + → Create skill → Upload a skill**. Upload and enable the ZIP, start a new chat, and ask for `pi-competitive-research`. See [Claude's current instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Claude Code uses the skills.sh command above.

## Common questions

**Do I need to know my competitors?** No. Provide your own website, market, and case types; the assistant can find and explain a relevant set with web access.

**Does it need my Google Ads account?** No. The main workflow uses public information.

**Will it call competitors or fill out their forms?** No. It reads public information and proposes changes for your own team to consider.

**Can it tell me how much competitors spend?** No. Seeing an ad does not reveal spend, signed cases, profitability, or demand. Website claims also do not prove actual staffing or service quality.

**My chat cannot browse the web.** Supply saved pages or screenshots. The assistant can compare those materials and their dates, but should not claim to have researched current websites or search results.

**The assistant says a page or listing is blocked.** Ask it to continue with accessible sources and label the gap. Missing evidence is not proof that a competitor lacks a service or runs no ads.

**The assistant cannot find the installed skill.** Start a new task and ask for `pi-competitive-research` by name. In Codex, you can type `$pi-competitive-research`; in Claude Code, `/pi-competitive-research`. [More setup help](https://github.com/lighthouse-legal/skills/blob/main/docs/installation.md).

**Can I repeat the report later?** Yes. Ask it to use the same firms, market, and search conditions, then distinguish verified changes from differences in the new sample.

## Examples, details, and limits

See the [fictional sample report](examples/synthetic-report.md) for the output format. It contains invented firms and evidence, not a live market assessment.

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Instructions followed by the assistant |
| [Evidence guide](references/evidence-guide.md) | Comparable page coverage, source records, review sampling, experiments |
| [Search and ads guide](references/search-and-ads.md) | Channel distinctions, location limits, public ad records |
| [Auction Insights guide](references/auction-insights.md) | Optional advertising export interpretation |
| [Report template](assets/report-template.md) | Structure for the finished report |

The skill supplies a research process; your AI assistant supplies browsing and analysis tools. It does not judge attorney competence, estimate case value, or certify advertising compliance. Keep client details and private exports out of public GitHub issues. [Test results](https://github.com/lighthouse-legal/skills/blob/main/evals/README.md) distinguish executed tests from documented options; hosted ChatGPT/Claude uploads remain unverified.

## From Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI intake for personal injury firms. We publish free tools for other parts of running a firm, too. This skill is MIT licensed and works without a Lighthouse account.
