# Google Ads audit for personal injury firms

A free agent skill that turns Google Ads data into a useful account review: what the firm is paying for, what its reported conversions actually mean, and which questions or changes deserve attention first.

Use it before an agency meeting, when reviewing a budget, or when results look different from what the dashboard suggests. It works with account exports, an authorized browser, or Google's official Ads MCP. You do not need a Lighthouse account, call recordings, a CRM integration, or Local Services Ads access.

## What you get

The agent produces a report with the reporting scope, reconciled performance, important findings tied to evidence, and a short list of proposed actions. It distinguishes recorded conversions from qualified leads or signed cases, separates brand and nonbrand performance, and investigates query intent against your firm's actual services.

The report can identify a mismatch between the queries receiving spend and the cases you take. It can also reveal that the account's conversion metric combines useful inquiries with softer activity, making its apparent cost per lead unreliable. Those are different problems with different next steps; the skill is designed to explain the distinction.

An audit can still be worthwhile with missing data. If you supply only campaign totals, the agent should tell you what those totals establish and what additional evidence would change the advice. It should not invent a search-term review or claim to have checked settings it cannot see.

## Try it with the included example

The [example firm context](examples/firm-context.md), [campaigns](examples/campaigns.csv), and [search terms](examples/search-terms.csv) are entirely fictional. See [sample findings](examples/sample-findings.md) for the kind of output to expect. After installing the skill, attach the three input files or place them in your agent's working folder, then ask:

> Use pi-google-ads-audit to review these reports for our next agency meeting. Explain what the numbers establish, the main uncertainties, and the next improvements to investigate.

For a real account, replace the example with your files and add a few sentences about the cases you want, service area, exclusions, and what the conversion actions represent. Do not paste credentials or client records.

## Install

Download [pi-google-ads-audit.zip](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-google-ads-audit.zip). It contains one complete skill folder, including instructions, references, examples, and a small local calculation script. Keep those files together; downloading `SKILL.md` alone loses supporting material.

### Claude on the web or desktop

In Claude, enable **Code execution and file creation**, open **Customize → Skills**, choose **+ → Create skill → Upload a skill**, and select the ZIP. Enable the uploaded skill, then start a new conversation and ask for it by name. Workspace policies can limit access. See [Claude's current skill instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [ZIP packaging guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

Attach your exports to that conversation. Installing the skill does not connect your Google account. If you use a remote Google Ads connector, configure and authorize it separately.

### ChatGPT

In an eligible workspace, use **Plugins → Skills → Create → Upload from your computer** and follow the upload/scan controls. Ask ChatGPT to use `pi-google-ads-audit` in a new conversation and attach the exports. OpenAI currently documents workspace Skills for eligible Business, Enterprise, Healthcare, and Edu accounts; availability and permissions vary. [Official ChatGPT Skills instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

The upload route is documented, but acceptance of this repository's standalone ZIP in ChatGPT has not yet been verified. If your upload control requires a different package type, do not upload the whole repository as a substitute. You can instead attach `SKILL.md`, the relevant references, and your exports to a file-capable chat and explicitly ask it to follow the workflow. That is a conversation-specific fallback, not a persistent installation. Without file analysis/code tools, ask for a qualitative preliminary review and do not assume the calculation helper ran.

### Claude Code or Codex

Clone the repository, then copy the whole skill folder to the appropriate location. These commands are for a first installation on macOS/Linux:

```sh
git clone https://github.com/lighthouse-legal/skills.git lighthouse-skills
cd lighthouse-skills

# Claude Code
mkdir -p "$HOME/.claude/skills"
cp -R skills/pi-google-ads-audit "$HOME/.claude/skills/"

# Codex
mkdir -p "$HOME/.agents/skills"
cp -R skills/pi-google-ads-audit "$HOME/.agents/skills/"
```

Run only the copy commands for your client. For a project-only install, use `.claude/skills/` or `.agents/skills/` inside that project instead. On Windows, copy the extracted folder to the same relative location under your user profile. For updates, intentionally replace the old skill folder after saving any customizations; avoid merging stale files into a new release.

Start the agent in the folder containing your reports. In a **chat prompt**, use `/pi-google-ads-audit` in Claude Code or `$pi-google-ads-audit` in Codex, followed by your request. These are not shell commands. If it does not appear, restart the client and check that the installed folder contains `SKILL.md` directly. See [Claude Code skills](https://code.claude.com/docs/en/skills) and [Codex skill creation and discovery](https://learn.chatgpt.com/docs/build-skills).

## Choose a data path

**Exports are the easiest starting point.** Download the campaign table and search terms report for the same date range, including Cost, Clicks, Impressions, and Conversions. Supply the account currency, time zone, filters, and conversion definitions. [The export guide](references/exports-and-math.md) explains the useful columns and optional reports. Keep files in a private folder outside this public checkout. Uploading them to your chosen AI service uses that service's data controls; the skill does not send them to Lighthouse.

**Google Ads MCP is an optional connection.** Google's [open-source server](https://github.com/googleads/google-ads-mcp) provides account reporting tools. Follow its [current setup guide](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) and your client's connector instructions. A local stdio setup works in supporting local clients; hosted chat needs its own supported remote connection. This repository contains the analysis workflow, not a hosted Google Ads service or credentials. Read [account access](references/account-access.md) for scope and query handling.

**Browser access also works** when your agent has an authorized browser and you are signed in. The agent can inspect reports or download exports and must record the selected dates, filters, and visible coverage. A screenshot of an overview is useful but cannot stand in for every account setting or table row.

## Calculation helper

The optional helper needs Python 3.10+ and no external packages:

```sh
python3 skills/pi-google-ads-audit/scripts/summarize_ads_csv.py \
  skills/pi-google-ads-audit/examples/campaigns.csv --currency USD
```

It preserves fractional conversions, recomputes ratios from totals, separates summary rows, and refuses ambiguous or malformed inputs. It supports common English CSV headers and several delimiters/locales, not every Google export format. Its JSON contains the original cells, so treat results as private. See the [supported formats and limits](references/exports-and-math.md).

## Design choices and limits

This skill never applies account changes. Recommendations are for a person to review; no bids, budgets, ads, targets, conversions, or access settings are modified. No arbitrary “good PI CPA,” guaranteed savings, broad-match ban, or universal conversion-volume rule is built in. It does not certify advertising compliance or judge a potential client's legal claim.

Google's tools are a useful foundation, but Google does not endorse these recommendations. The quality of the review depends on the evidence supplied and the agent running it. Cross-channel attribution, call quality, signed cases, listings, and LSA analysis are outside the report unless you provide matching evidence. [Evaluation methodology and results](https://github.com/lighthouse-legal/skills/blob/main/evals/README.md) distinguish tested paths from remaining integration gaps.

## About Lighthouse

[Lighthouse](https://www.lighthouselegal.ai) builds voice AI for personal injury intake: answering calls, gathering the information a firm needs, and connecting priority callers with its team. We publish these tools to help firms run other parts of their business too. This skill is free under the repository's MIT license and works independently of Lighthouse.
