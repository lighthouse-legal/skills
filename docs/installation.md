# Install Lighthouse skills

**Choose the app you actually use.** Claude Code is a different product from Claude's regular chat. A skill installed on your computer is separate from a ChatGPT browser conversation.

| Where you work | Best starting point |
| --- | --- |
| Codex, Claude Code, Cursor, or another supported local app | Use the skills.sh installer below. |
| ChatGPT in a browser | Follow the three-step chat guide for [Google Ads](../skills/pi-google-ads-audit/README.md#use-in-chatgpt-no-installation) or [competitive research](../skills/pi-competitive-research/README.md#use-in-chatgpt-no-installation). No terminal required. |
| Claude's regular web or desktop chat | Attach a chat guide, or use the optional ZIP upload in the [Ads](../skills/pi-google-ads-audit/README.md#use-in-claude-chat) or [competitor](../skills/pi-competitive-research/README.md#use-in-claude-chat) instructions. |

## Install with skills.sh

The recommended installer is [skills.sh](https://skills.sh/docs). You need your chosen AI app installed and signed in, [Node.js](https://nodejs.org/en/download) (choose the current LTS version), and [Git](https://git-scm.com/downloads). You do not need a GitHub account. The installer version tested here, skills 1.7.0, requires Node.js 22.20 or newer.

Open **Terminal** from Applications → Utilities on macOS, or search for **PowerShell** in the Windows Start menu. Paste this command there and press Enter:

```sh
npx skills add lighthouse-legal/skills --global
```

If npm asks to install the `skills` utility, enter `y`. Select the skills you want with the arrow keys and Space, then press Enter. If asked which apps to use, choose yours. Codex can appear under “Universal” as already included; some installations skip this question. Keep the recommended installation method. `--global` means the skills are available across your workspaces on this computer.

The command is **`npx skills add`**. `npm add skills` installs an npm package but does not install these Lighthouse skills into your assistant.

### Install for one app directly

If you prefer to skip choosing the app, use **one** of these commands:

```sh
# Codex
npx skills add lighthouse-legal/skills --global --agent codex
```

```sh
# Claude Code
npx skills add lighthouse-legal/skills --global --agent claude-code
```

To install only one skill, add `--skill pi-google-ads-audit` or `--skill pi-competitive-research`. For a project-only installation, run the command inside that project's folder and omit `--global`.

## Check that it worked

1. The installer should name the installed skill and its destination.
2. Start a new task in the app you selected. Ask: **“Use pi-competitive-research. Confirm you can load the skill, then ask for the inputs you need for my first report.”** Substitute `pi-google-ads-audit` if that is the one you installed.
3. The assistant should identify the skill and ask for the relevant inputs. If it says it cannot load the skill, use the troubleshooting table below.

Then follow the [Ads first-report prompt](../skills/pi-google-ads-audit/README.md#your-first-report) or [competitive research first-report prompt](../skills/pi-competitive-research/README.md#your-first-report). Installing a skill does not connect your Google account or add web browsing; the skill works with the tools and files your assistant can access.

## Troubleshooting

| What you see | What to do |
| --- | --- |
| `npx` is not recognized or command not found | Install Node.js LTS, close Terminal/PowerShell, reopen it, and retry. Your IT team can help. |
| A Node version or engine error | Upgrade to the current Node.js LTS release and reopen Terminal/PowerShell. |
| `git` is not found | Install Git and reopen Terminal/PowerShell. |
| PowerShell blocks `npx.ps1` | Use `npx.cmd` in place of `npx`; no execution-policy change is needed. |
| The assistant does not see the skill | Confirm you selected the right app, start a new task, and restart the app if needed. Run `npx skills list --global` to check the installation. |
| ChatGPT treats the install command as a question | The command belongs in your computer's Terminal/PowerShell. For a browser chat, use the single-file chat guide instead. |
| The chat cannot read an attached guide | Open the downloaded text file and paste its contents. Ask the assistant to confirm it can read them before proceeding. |
| The assistant asks for account credentials | Use exported Ads reports. Do not paste passwords or API keys into chat. |

## Updates and removal

In Terminal/PowerShell, update just these skills with:

```sh
npx skills update pi-google-ads-audit pi-competitive-research --global
```

Remove one with:

```sh
npx skills remove pi-google-ads-audit --global
```

Follow the prompts to select the relevant app. These commands manage installed skills, not your reports or advertising accounts. See the [installer's command reference](https://github.com/vercel-labs/skills#readme) for other supported apps and options.

## Other installation options

[ZIP downloads](https://github.com/lighthouse-legal/skills/releases/latest) remain available for clients with a skill-upload control and for manual installation. Keep the complete skill folder together. For manual local installation, put it in `.agents/skills/` within a Codex project, or `.claude/skills/` within a Claude Code project. Personal installations use those directories under your home folder.

ChatGPT workspace skills, local skills, and plugins have separate installation controls. A local skills.sh installation does not create a ChatGPT workspace skill. If your workspace provides a skill upload feature, follow its current controls; the single-file chat guide is the simpler way to try the workflow without that setup. [Official OpenAI skill controls](https://learn.chatgpt.com/docs/enterprise/skills).

Instructions checked September 25, 2026. See the [test record](../evals/README.md) for what was actually exercised. Chat guides are conversation instructions, not native installed skills; hosted ChatGPT/Claude use has not been independently verified here.
