# Installation

## No Install Setup

Open a new ChatGPT chat, or another AI assistant that can open web links. Copy the short prompt from the [Google Ads guide](../skills/pi-google-ads-audit/README.md#no-install-setup) or [competitive research guide](../skills/pi-competitive-research/README.md#no-install-setup).

Include the link when you paste it. The assistant will read the guide and ask for the information it needs. Use the prompt again when you start a new chat.

### The assistant cannot open the link

Download the matching text guide below. Attach it to your chat using the attachment button beside the message box. Then say: **“Follow the attached guide. Ask me what you need to get started.”**

| Skill | Text guide |
| --- | --- |
| Google Ads audit | [Download the Ads guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-google-ads-audit-chat-guide.txt) |
| Competitive research | [Download the competitor guide](https://github.com/lighthouse-legal/skills/releases/latest/download/pi-competitive-research-chat-guide.txt) |

You do not need to read or edit the file. If attachments are unavailable, open the text file and paste its contents into the chat.

For competitive research, the assistant also needs web access to read current websites. If it cannot browse, share saved pages or screenshots for it to compare.

## Install with skills.sh

Use this option for Codex, Claude Code, or another supported app on your computer. It makes the skills available for future tasks in that app.

1. Install [Node.js](https://nodejs.org/en/download) (choose LTS) and [Git](https://git-scm.com/downloads), if needed.
2. Open Terminal from Applications → Utilities on Mac, or search for PowerShell on Windows.
3. Paste this command and press Enter:

```sh
npx skills add lighthouse-legal/skills --global
```

If asked to install the `skills` utility, enter `y`. Use the arrow keys and Space to choose skills, then press Enter. Choose your app if asked and confirm installation.

Start a new task in your app. Ask to use `pi-google-ads-audit` or `pi-competitive-research`, and let the assistant ask its setup questions.

No GitHub account is needed. This command installs skills for local apps; it does not add them to your ChatGPT browser chats. [skills.sh documentation](https://skills.sh/docs).

## Troubleshooting

| Problem | Try this |
| --- | --- |
| The chat cannot open the guide link | [Attach the text guide instead](#the-assistant-cannot-open-the-link). |
| `npx` or `git` is not found | Install Node.js LTS and Git, then close and reopen Terminal or PowerShell. |
| A Node version error appears | Upgrade to the current Node.js LTS version. The tested installer requires Node 22.20 or newer. |
| PowerShell blocks `npx.ps1` | Use `npx.cmd` in place of `npx`. |
| The assistant cannot find an installed skill | Check that you chose the right app. Start a new task, or restart the app. Check installed skills with `npx skills list --global`. |
| The assistant asks for your Google password | Share Ads reports instead. Do not paste passwords into chat. |

## Other options

<details>
<summary>Choose one app or one skill</summary>

Add `--agent codex` or `--agent claude-code` to the install command to choose your app directly. Add `--skill pi-google-ads-audit` or `--skill pi-competitive-research` to choose one skill.

For a project-only installation, run the command in that project's folder and leave out `--global`.

</details>

<details>
<summary>Update or remove installed skills</summary>

Run these in Terminal or PowerShell:

```sh
npx skills update pi-google-ads-audit pi-competitive-research --global
```

```sh
npx skills remove pi-google-ads-audit --global
```

Follow any prompts. These commands manage skills, not your reports or advertising accounts.

</details>

<details>
<summary>ZIP downloads and manual installation</summary>

[ZIP downloads](https://github.com/lighthouse-legal/skills/releases/latest) are available for apps with a skill-upload control. Keep the complete skill folder together.

For manual local installation, put the folder in `.agents/skills/` within a Codex project, or `.claude/skills/` within a Claude Code project. Personal installations use those directories under your home folder.

For native upload controls, see [OpenAI's workspace skill guide](https://learn.chatgpt.com/docs/enterprise/skills) or [Claude's skill guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

</details>

[Test results](../evals/README.md) explain what has been checked. Link prompts and text attachments supply instructions for the conversation; they do not install a skill. Hosted ChatGPT and Claude behavior has not been independently verified here.
