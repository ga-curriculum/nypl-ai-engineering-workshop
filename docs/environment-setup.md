# Environment Setup

Complete these steps **before** the workshop. Allow 20–30 minutes.

## Prerequisites

- [ ] Python 3.10 or higher
- [ ] Git
- [ ] VS Code (recommended) or another editor with Copilot support
- [ ] A GitHub account

## Step 1: Clone the Repository

```bash
git clone https://git.generalassemb.ly/modular-courses/nypl-ai-engineering-workshop.git
cd nypl-ai-engineering-workshop
```

## Step 2: Set Up the Python Sandbox

```bash
cd sandbox
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Verify the setup:
```bash
python -m pytest tests/ -v
```

You should see all tests pass.

## Step 3: Configure GitHub Copilot

1. **Install the extension:** In VS Code, search for "GitHub Copilot" in the Extensions panel and install it
2. **Sign in:** Click the Copilot icon in the status bar and sign in with your GitHub account
3. **Verify:** Open a Python file and start typing — you should see gray inline suggestions

If Copilot isn't suggesting anything:
- Check that your license is active at [github.com/settings/copilot](https://github.com/settings/copilot)
- Ensure the extension is enabled for Python files
- Try reloading VS Code (`Cmd+Shift+P` > "Reload Window")

## Step 4: Configure Google Gemini

### Option A: Gemini in VS Code (if using Gemini Code Assist)
1. Install the "Gemini Code Assist" extension in VS Code
2. Sign in with your Google account
3. Verify by opening the Gemini chat panel

### Option B: Gemini API Access
1. Obtain your API key (provided by your organization or at [aistudio.google.com](https://aistudio.google.com))
2. Set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
3. Add to your shell profile (`.bashrc`, `.zshrc`) to persist across sessions

### Option C: Gemini Web Interface
- Navigate to [gemini.google.com](https://gemini.google.com)
- Sign in with your Google account
- This is the fallback option if API/extension setup has issues

## Troubleshooting

| Problem | Solution |
|---|---|
| `python` command not found | Try `python3` instead. Ensure Python is on your PATH. |
| Copilot not showing suggestions | Reload VS Code. Check license status. Disable competing extensions. |
| Gemini API returns 403 | Verify your API key. Check that the Gemini API is enabled in your Google Cloud project. |
| `pip install` fails | Ensure you're in the virtual environment (`venv`). Try `pip install --upgrade pip` first. |
| Tests fail on setup | Check Python version (`python --version`). Must be 3.10+. |

## Verify Everything Works

Run this checklist:

- [ ] `python --version` shows 3.10+
- [ ] `python -m pytest sandbox/tests/ -v` passes
- [ ] Copilot suggests completions in a `.py` file
- [ ] Gemini responds to a test prompt (via extension, API, or web)

If any step fails, contact the workshop team before the session.
