# Technology Guide — AI-Assisted Software Engineering Workshop

This guide covers every tool used in the workshop — what it does, how to set it up, and how to fix it if something goes wrong. Complete the setup sections **before the workshop** (allow 20–30 minutes).

---

## Tools Overview

This workshop uses a **dual-tool framework** — two AI coding tools that complement each other, plus a Python codebase and testing framework.

| Tool | What It Does | Why We Use It |
|---|---|---|
| **Google Gemini Code Assist** | AI assistant for deep code analysis, architectural reasoning, and multi-file planning | 1M token context window lets it analyze entire codebases at once — best for understanding big-picture architecture and detailed code review |
| **GitHub Copilot** | AI assistant for inline code completion, fast generation, and chat-based coding | Tight GitHub integration and fast inline suggestions — best for writing code quickly in your editor |
| **VS Code** | Code editor | Both AI tools run as VS Code extensions; it's the shared workspace for the entire workshop |
| **Python 3.10+** | Programming language | All labs and the capstone use Python |
| **pytest** | Testing framework | Used in Labs 2, 3, and the Capstone to run and verify tests |
| **Git** | Version control | Clone repos and track your work |

### When to Use Which AI Tool

| Task | Best Tool | Why |
|---|---|---|
| "Explain this codebase's architecture" | Gemini Code Assist | Large context window sees the whole picture |
| "What does this function do line by line?" | Copilot | Fast, focused inline explanation |
| "Plan how to add a new feature" | Gemini Code Assist | Better at multi-step reasoning and planning |
| "Write this function for me" | Copilot | Fast inline completion right in your editor |
| "Review this code for security issues" | Gemini Code Assist | Detailed analysis with structured output |
| "Generate tests for this class" | Copilot | Fast test scaffolding, then review with Gemini Code Assist |
| "Fix this specific bug" | Either | Try Copilot first for speed; switch to Gemini Code Assist if it needs more context |

**The rule of thumb:** Gemini Code Assist for depth, Copilot for velocity.

---

## System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| **Operating System** | macOS, Windows, or Linux | macOS or Windows (tested) |
| **Python** | 3.10 | 3.11 or 3.12 |
| **VS Code** | Latest stable release | Latest stable release |
| **Git** | Any recent version | Latest stable |
| **Internet** | Required for AI tools | Stable connection (both tools call cloud APIs) |
| **Disk Space** | ~500 MB | ~1 GB (with virtual environment) |

### Check Your Versions

```bash
python --version    # or python3 --version — need 3.10+
git --version       # any recent version
code --version      # VS Code — should show version number
```

---

## Setup Instructions

### Step 1: Clone the Repositories

You'll work with **two repos** — the workshop curriculum and NYPL's Python codebase:

```bash
# Clone the workshop repo (instructions, labs, exercises)
git clone git@git.generalassemb.ly:modular-curriculum-all-courses/nypl-ai-engineering-workshop.git

# Clone the sandbox codebase (the Python code you'll work with in labs)
git clone https://github.com/NYPL-GA-Training/python-utils.git
```

Both repos should be in the same parent directory:
```
your-folder/
├── nypl-ai-engineering-workshop/    ← Workshop instructions
└── python-utils/                    ← Code you'll work with
```

### Step 2: Set Up the Python Environment

```bash
cd python-utils

# Create a virtual environment (keeps dependencies isolated)
python -m venv venv

# Activate it
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# Install all dependencies (includes pytest and mocks — no AWS credentials needed)
pip install '.[development]'
```

Verify it worked:
```bash
python -m pytest
```

You should see **103 tests pass**. If they do, your Python environment is ready.

### Step 3: Set Up VS Code

1. Open VS Code
2. Open the `python-utils` folder (`File > Open Folder`)
3. If prompted, select the Python interpreter from your `venv` (`Python 3.x ('venv')`)
4. Open a `.py` file to confirm syntax highlighting works

### Step 4: Install and Configure GitHub Copilot

> **License required:** Copilot access is provisioned through NYPL's GitHub organization. You should receive an invitation to join the org with Copilot licenses — accept the invitation before proceeding.

1. In VS Code, open the Extensions panel (`Cmd+Shift+X` on Mac / `Ctrl+Shift+X` on Windows)
2. Search for **"GitHub Copilot"** and install it
3. Click the Copilot icon in the status bar and **sign in** with the GitHub account that has NYPL org membership
4. **Verify:** Open any `.py` file and start typing — you should see gray inline suggestions appear

**What Copilot looks like when it's working:**
- Gray "ghost text" appears as you type, suggesting completions
- Press `Tab` to accept a suggestion, `Esc` to dismiss
- The Copilot icon in the status bar shows it's active (no warning symbol)

### Step 5: Install and Configure Google Gemini Code Assist

1. In VS Code, open the Extensions panel
2. Search for **"Gemini Code Assist"** (publisher: Google) and install it
3. Click the **Gemini Code Assist icon** in the sidebar and sign in with your Google account
4. **Verify:** Open the Gemini Code Assist chat panel and send a test prompt:
   ```
   Hello, what can you help me with?
   ```
   You should get a response within a few seconds.

**What Gemini Code Assist looks like when it's working:**
- The Gemini Code Assist icon appears in the VS Code sidebar
- The chat panel opens when you click it
- You can type prompts and get responses with code, explanations, and analysis

---

## Verification Checklist

Run through this before the workshop. Every item should pass:

- [ ] `python --version` shows **3.10 or higher**
- [ ] `python -m pytest` passes in the `python-utils/` directory (**103 tests**)
- [ ] VS Code opens and recognizes `.py` files
- [ ] **Copilot** suggests inline completions when you type in a `.py` file
- [ ] **Gemini Code Assist** responds to a test prompt in the chat panel

If any step fails, see Troubleshooting below.

---

## Troubleshooting

### Python Issues

| Problem | Solution |
|---|---|
| `python` command not found | Try `python3` instead. On macOS, you may need to install via [python.org](https://www.python.org/downloads/) or `brew install python`. |
| `pip install` fails | Make sure you activated the virtual environment first (`source venv/bin/activate`). Try `pip install --upgrade pip` then retry. |
| Tests fail on setup | Check your Python version — must be 3.10+. Also make sure you ran `pip install '.[development]'` (with the quotes). |
| `ModuleNotFoundError` | You're probably not in the virtual environment. Run `source venv/bin/activate` and try again. |

### GitHub Copilot Issues

| Problem | Solution |
|---|---|
| No inline suggestions | 1. Check that the Copilot icon in the status bar has no warning. 2. Reload VS Code (`Cmd+Shift+P` > "Reload Window"). 3. Verify your license at [github.com/settings/copilot](https://github.com/settings/copilot). |
| "You don't have access" error | Accept the NYPL GitHub org invitation (check your email). Then sign out and back in to Copilot in VS Code. |
| Suggestions appear for other languages but not Python | Open VS Code settings and ensure Copilot is enabled for Python (`"github.copilot.enable": {"python": true}`). |
| Copilot extension won't install | Check your VS Code version is up to date. Try uninstalling, restarting VS Code, and reinstalling. |

### Google Gemini Code Assist Issues

| Problem | Solution |
|---|---|
| Chat panel not responding | 1. Reload VS Code (`Cmd+Shift+P` > "Reload Window"). 2. Check your Google account sign-in (try signing out and back in). |
| "Extension not activated" | Make sure no other AI extensions are conflicting. Disable other AI chat extensions temporarily. |
| Sign-in loop (keeps asking to sign in) | Clear the extension's stored credentials: `Cmd+Shift+P` > "Gemini Code Assist: Sign Out", then sign in again with your organization Google account. |
| Extension not found in marketplace | Search for "Gemini Code Assist" (not "Gemini" alone). Publisher should be Google. |

### General Issues

| Problem | Solution |
|---|---|
| VS Code can't find Python interpreter | Open Command Palette (`Cmd+Shift+P`) > "Python: Select Interpreter" > choose the one from your `venv`. |
| Git clone fails | Check your SSH keys are set up for git.generalassemb.ly. For python-utils (HTTPS), no credentials needed. |
| WiFi issues during workshop | Copilot inline suggestions may work briefly offline. For extended outages, pair with a neighbor who has connectivity. The facilitator has a USB backup with the repo and dependencies. |

---

## Tool Tips for the Workshop

### Getting the Most from Gemini Code Assist

- **Be specific in prompts.** Instead of "analyze this code," try: "Analyze this function for security vulnerabilities. Check for injection, auth issues, and data exposure. Return findings in a table."
- **Use it for planning.** Before writing code, ask Gemini Code Assist to break a task into implementation steps.
- **Paste full context.** Gemini Code Assist's 1M token context means you can paste entire files — don't worry about being too verbose.
- **Use it for code review.** After writing code, paste it back and ask Gemini Code Assist to review it with a specific QA persona (e.g., "Act as a security auditor...").

### Getting the Most from Copilot

- **Write descriptive comments first.** Copilot reads your comments to understand intent. A clear comment = better suggestions.
  ```python
  # Validate email: check for empty input, missing @, invalid domain, length > 254
  # Return tuple of (is_valid: bool, error_message: str | None)
  def validate_email(
  ```
- **Accept partially.** You don't have to accept the whole suggestion. Use `Cmd+→` (Mac) to accept word by word.
- **Use Copilot Chat.** Press `Cmd+I` (Mac) / `Ctrl+I` (Windows) for inline chat, or open the chat panel for longer conversations.
- **Give it context by opening files.** Copilot reads your open tabs — open related files to give it more context.

### Using Both Tools Together

The workflow we teach all day:

1. **Plan with Gemini Code Assist** — Ask it to analyze the codebase and break down your task
2. **Build with Copilot** — Use inline suggestions and chat to write the code
3. **Review with Gemini Code Assist** — Paste your code back and apply a QA persona
4. **Refine with Copilot** — Fix issues found in review with fast inline edits

---

## Facilitator Technology Checklist

> This section is for the instructor/facilitator only.

### 1 Week Before Delivery

- [ ] Verify all 25 participant Copilot licenses are activated (check with NYPL contact)
- [ ] Verify Gemini Code Assist access for all participants (Google account access confirmed)
- [ ] Test fresh clone + full setup on a clean machine (follow Steps 1–5 above)
- [ ] Test both AI extensions on at least 3 different machines (different OS if possible)
- [ ] Confirm venue WiFi can handle 25+ simultaneous connections

### Day Before

- [ ] Clone repos fresh and run through setup one more time
- [ ] Test projector / screen share setup
- [ ] Prepare USB backup drive with:
  - [ ] Workshop repo (zipped)
  - [ ] python-utils repo (zipped)
  - [ ] Pre-built `venv` with all dependencies installed (for offline installs)
- [ ] Pre-record demo videos of key Gemini Code Assist interactions (for extension failure fallback)

### Day Of — Before Participants Arrive

- [ ] Test WiFi at the venue
- [ ] Display `docs/environment-setup.md` on screen as participants arrive
- [ ] Have this Technology Guide URL/path ready to share
- [ ] Test Copilot and Gemini Code Assist one final time on the presentation machine

### During the Workshop — Common Issues

- **Copilot not working for a participant:** Have them pair up. Check license status. Try Copilot in the browser at [github.com/copilot](https://github.com/copilot) as a fallback.
- **Gemini Code Assist not loading:** Have them sign out and back in. Disable competing AI extensions. Pair with a neighbor if unresolved.
- **WiFi drops:** Copilot inline suggestions may work briefly offline. Switch to USB backup if outage persists. Key exercises can continue with cached suggestions.
- **Python environment issues:** Have them delete and recreate the venv. If `pip install` fails on WiFi, install from the USB backup.

---

*General Assembly — All rights reserved. For educational use only.*
