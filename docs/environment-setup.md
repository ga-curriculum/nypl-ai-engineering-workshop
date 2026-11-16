# Environment Setup

Complete these steps **before** the workshop. Allow 20–30 minutes.

## Prerequisites

- [ ] Python 3.10 or higher
- [ ] Git
- [ ] VS Code (recommended) or another editor with Copilot support
- [ ] A GitHub account

## Step 1: Clone the Repository

```bash
git clone https://github.com/ga-curriculum/nypl-ai-engineering-workshop.git
cd nypl-ai-engineering-workshop
```

## Step 2: Set Up the Python Sandbox (python-utils)

The workshop uses NYPL's **python-utils** library as the codebase you'll work with. Clone it as a separate repo alongside the workshop repo:

```bash
# From the same parent directory as the workshop repo
git clone https://github.com/NYPL-GA-Training/python-utils.git
cd python-utils

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install all dependencies (includes pytest, mocks — no AWS credentials needed)
pip install '.[development]'
```

Verify the setup:
```bash
python -m pytest
```

You should see all 103 tests pass.

## Step 3: Configure GitHub Copilot

> **Copilot access** will be provisioned through NYPL's GitHub organization. You will receive an invitation to join the organization with Copilot licenses attached. Accept the invitation before proceeding.

1. **Install the extension:** In VS Code, search for "GitHub Copilot" in the Extensions panel and install it
2. **Sign in:** Click the Copilot icon in the status bar and sign in with the GitHub account that has the NYPL org membership
3. **Verify:** Open a Python file and start typing — you should see gray inline suggestions

If Copilot isn't suggesting anything:
- Ensure you accepted the NYPL GitHub org invitation
- Check that your license is active at [github.com/settings/copilot](https://github.com/settings/copilot)
- Ensure the extension is enabled for Python files
- Try reloading VS Code (`Cmd+Shift+P` > "Reload Window")

## Step 4: Configure Google Gemini Code Assist

1. **Install the extension:** In VS Code, search for "Gemini Code Assist" in the Extensions panel (publisher: Google) and install it
2. **Sign in:** Click the Gemini Code Assist icon in the sidebar and sign in with your Google account
3. **Verify:** Open the Gemini Code Assist chat panel and send a test prompt (e.g., "Hello, what can you help me with?")

If Gemini Code Assist isn't working:
- Ensure you're signed in with the correct Google account (your organization account, not personal)
- Try reloading VS Code (`Cmd+Shift+P` > "Reload Window")
- Check that the extension is enabled and not conflicting with other AI extensions

## Troubleshooting

| Problem | Solution |
|---|---|
| `python` command not found | Try `python3` instead. Ensure Python is on your PATH. |
| Copilot not showing suggestions | Reload VS Code. Check license status. Disable competing extensions. |
| Gemini Code Assist not responding | Reload VS Code. Check Google account sign-in. Verify the extension is enabled. |
| `pip install` fails | Ensure you're in the virtual environment (`venv`). Try `pip install --upgrade pip` first. |
| Tests fail on setup | Check Python version (`python --version`). Must be 3.10+. |

## Verify Everything Works

Run this checklist:

- [ ] `python --version` shows 3.10+
- [ ] `python -m pytest` passes (run from the `python-utils/` directory)
- [ ] Copilot suggests completions in a `.py` file
- [ ] Gemini Code Assist responds to a test prompt in the VS Code chat panel

If any step fails, contact the workshop team before the session.
