# PI competitive research

See how your personal injury firm presents itself alongside local competitors, with sources you can check.

This free skill guides an AI assistant through a focused comparison of your firm's website, nearby firms, public advertising, and local search results. It is designed for owners, managing partners, office managers, marketing staff, and agencies preparing for a website update or marketing review.

Published by [Lighthouse](https://www.lighthouselegal.ai), which builds voice AI intake for personal injury firms. You do not need a Lighthouse account. The report's recommendations follow the evidence and your business question.

## What you receive

- A short executive brief with supported findings, strengths, and unanswered questions.
- A comparison matrix covering positioning, practice areas, geography, language claims, contact options, and published availability.
- Separate observations for Paid Search, Local Services Ads, Maps/local results, and organic results where they can be inspected.
- Three to five proposed experiments, each with an owner, scope, measurement plan, and decision rule.
- An evidence appendix with source links, dates, methods, search conditions, and any review-sampling limits.

The default scope is your firm plus up to five comparison firms in one market, with up to three priority practice areas. You can name competitors or let the assistant find and explain a relevant set. Start with one market so the comparison stays useful.

See the [report template](assets/report-template.md) and [fictional sample](examples/synthetic-report.md). The sample demonstrates the format with invented firms and incomplete evidence; it is not a real research result.

## What you need

Provide your firm's website, a city or metro area with its state/country, the case types that matter, and the decision you want to make. Optional inputs include competitor names, languages of interest, and a redacted export from your own Google Ads account.

Use an assistant with web access for current research. A browser or research tool may expose only some search channels. The assistant should complete the website comparison and identify unavailable channels instead of guessing. If web access is unavailable, you can supply saved pages, screenshots, or excerpts for a comparison of those materials; the result should state their dates and avoid claiming current coverage.

The skill itself is free and includes no paid data dependency. Your AI provider's plan limits, browsing availability, and usage charges still apply. No advertising account or Auction Insights export is required.

## Install or use it

This folder is the complete skill: keep `SKILL.md`, `references/`, and `assets/` together. The `agents/` folder supplies optional Codex display information; the workflow does not require it in other assistants. The README and example are for people learning the workflow.

Installation guidance below was checked against provider documentation on September 25, 2026. Hosted upload acceptance for this package has not yet been verified. Current test status and broader setup guidance belong in the [repository guide](https://github.com/lighthouse-legal/skills#readme).

### Get the folder or ZIP

Use the individual `pi-competitive-research.zip` from [Releases](https://github.com/lighthouse-legal/skills/releases) when available. If downloading the repository through GitHub's **Code → Download ZIP**, extract it first and locate `skills/pi-competitive-research`. For a Claude upload, compress that complete folder as its own ZIP; the archive should contain a top-level `pi-competitive-research/` folder with `SKILL.md` inside it. Do not upload the whole repository as one skill. [Claude packaging guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

For local clients, you can instead download with Git:

```sh
git clone https://github.com/lighthouse-legal/skills.git lighthouse-skills
cd lighthouse-skills
```

### ChatGPT workspace Skills

In an eligible Business, Enterprise, Healthcare, or Edu workspace, with the required permissions:

1. Open **Plugins → Skills → Create → Upload from your computer**.
2. Upload the skill package accepted by that control and complete the scan or review it presents.
3. Confirm that the skill appears as installed. Start a new conversation and ask ChatGPT to use `pi-competitive-research` with the brief below.

This is the documented workspace route. OpenAI's public help does not specify the exact accepted ZIP member layout, so the single-folder ZIP's acceptance remains unverified until a successful upload in the relevant workspace. If the upload control requires another package type, follow its current instructions. If Skills is missing, check account eligibility and workspace permissions. A chat attachment is a separate way to supply instructions; it does not demonstrate native installation. [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), [OpenAI skill controls](https://learn.chatgpt.com/docs/enterprise/skills).

### Claude web or desktop

Claude's documented Skills feature includes Free, Pro, Max, Team, and Enterprise, subject to account and organization controls:

1. Enable **Code execution and file creation** in your capabilities settings where required.
2. Open **Customize → Skills → + → Create skill → Upload a skill**.
3. Upload the single-folder ZIP and enable the skill.
4. Start a new conversation and ask Claude to use `pi-competitive-research` with your brief. Make web search available for current research.

Enterprise administrators may need to enable Skills and cloud code execution. A successful upload does not add web or advertising-account permissions. [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Claude web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search).

### Codex: local installation

With Codex installed and signed in, copy the whole skill folder into your personal skills directory. For a first installation on macOS or Linux, run these commands from the downloaded repository root:

```sh
mkdir -p "$HOME/.agents/skills"
cp -R skills/pi-competitive-research "$HOME/.agents/skills/"
```

For a project-only installation, place the folder inside that project's `.agents/skills/` instead. Start a Codex task in your research workspace and enter this as a **prompt**, not a shell command:

```text
$pi-competitive-research
```

Add your firm brief to that prompt. Codex detects skills automatically; restart if the skill does not appear. The CLI and IDE extension also have a `/skills` picker. [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code: local installation

With Claude Code installed and authenticated, run from the downloaded repository root for a first installation:

```sh
mkdir -p "$HOME/.claude/skills"
cp -R skills/pi-competitive-research "$HOME/.claude/skills/"
```

For a project-only installation, use `.claude/skills/` in that project. Start Claude Code in your research workspace and invoke `/pi-competitive-research`, followed by your brief. Claude web's Free Skills availability does not imply free Claude Code access. [Claude Code skills](https://code.claude.com/docs/en/skills), [Claude Code setup](https://code.claude.com/docs/en/quickstart).

On Windows, copy the complete folder with File Explorer or PowerShell into `.agents/skills` for Codex or `.claude/skills` for Claude Code under your user home directory. For updates, replace the existing skill folder intentionally rather than merging old and new files. Keep personal reports outside the installed skill folder.

### Use as a portable research brief

If your assistant cannot install custom skills, attach `SKILL.md`, all three files in `references/`, and `assets/report-template.md` to a conversation or project that supports readable file attachments. Explicitly ask it to read those instructions and follow them for your brief. If attachments are not readable, paste the relevant instructions instead. This is a manual workflow, not automatic skill discovery.

For any route, a pasted GitHub URL alone does not guarantee the assistant loaded the skill or its references. Installation also does not create new browsing capabilities. Ask it to identify which files it loaded and which research channels it can inspect before it reports results.

## Start your first report

Copy this and replace the bracketed fields:

```text
Use pi-competitive-research to compare our firm with local competitors.

Our website: [https://your-firm.com]
Market: [city/metro, state, country]
Priority case types: [for example, car crashes and truck crashes]
Decision: [for example, what should we clarify in our next website update?]
Competitors: [names/URLs, or choose up to five and explain the selection]
Languages of interest: [optional]

Give me the executive brief, comparison matrix, three to five proposed
experiments, and source appendix. Record what you actually inspect.
Keep Paid Search, Local Services Ads, Maps, and organic results separate.
```

Useful follow-ups:

```text
Which two findings are best supported? Show me their exact sources and
what you could not verify before I discuss them with our agency.
```

```text
Repeat the same comparison for the same firms and query conditions.
Separate actual changes from differences in the new research sample.
```

```text
I have attached a redacted Auction Insights CSV for [date range].
Explain what it adds to the report and what it cannot tell us.
Keep its campaign scope separate from public search observations.
```

The assistant may ask for a missing market or a material ambiguity. It should otherwise state reasonable research choices and proceed. If a site is blocked, it should continue with accessible information and disclose the gap.

## How it works

The assistant verifies relevant firms, reviews comparable public pages, and builds an evidence ledger. It records what each source says and keeps interpretation separate. The same claim can have different meanings: a Spanish page, an advertised bilingual team, and owner-confirmed Spanish intake are different observations.

For searches, it records the exact query, date, target geography, tool, and observer location when known. The city typed into a query is not proof that Google treated the search as coming from that city. A generic AI search result list is useful for finding firms but is not a verified Google ranking.

Public ad libraries are optional. Their creative records are reported separately from ads actually observed for local queries. If reviews are accessible, the assistant explains the sample's size, selection rule, dates, and bias. Five visible review texts do not represent every client.

The assistant then proposes small changes or investigations that follow from the evidence. A missing language-service statement might motivate a message test after you confirm the service is offered. It does not prove an untapped market or that a competitor has better service.

## Boundaries and privacy

This is public-information research. It does not contact competitors, submit forms, conduct mystery-shop calls, click sponsored contact actions, impersonate clients, or change any website, listing, or account. Experiments are proposals for you to review; they are not executed by the skill.

The report compares public communication. It does not determine legal competence, certify advertising compliance, estimate case value, or establish a competitor's actual budgets, acquisition costs, signed cases, profitability, or demand. Source failures appear as unavailable, not as evidence that a firm lacks a service or runs no ads.

Only share information your organization is comfortable giving to your chosen AI provider. Redact client details, account identifiers, and unnecessary business data from exports. The workflow does not require client records, passwords, or call recordings. Keep actual reports and exports in your own workspace; do not add them to this public repository.

## Files and optional resources

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Main instructions and research boundaries |
| [Evidence guide](references/evidence-guide.md) | Page coverage, source ledger, review sampling, experiments |
| [Search and ads guide](references/search-and-ads.md) | Query conditions, channel distinctions, public creative, access limits |
| [Auction Insights guide](references/auction-insights.md) | Optional export interpretation and reporting limits |
| [Report template](assets/report-template.md) | Reusable deliverable structure |
| [Fictional example](examples/synthetic-report.md) | Compact illustration with clearly invented evidence |

This original workflow uses existing public resources where useful. [Google Ads Transparency Center](https://adstransparency.google.com/) can provide creative records, and [BrightLocal's free local SEO tools](https://www.brightlocal.com/free-local-seo-tools/) include a local results checker. Availability and tool conditions can change; neither is required to finish a website comparison. Definitions and source links appear in the relevant guides.
