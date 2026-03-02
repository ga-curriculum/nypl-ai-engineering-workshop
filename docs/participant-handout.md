# Participant Handout — AI-Assisted Software Engineering

Welcome to the AI-Assisted Software Engineering workshop. Today you'll learn to use **Google Gemini Code Assist** and **GitHub Copilot** as professional engineering tools.

## Today's Schedule

| Time | Session |
|---|---|
| 10:00–11:30 | Module 1: AI as an Engineering Partner |
| 11:30–1:00 | Module 2: Working with Existing Codebases |
| 1:00–2:00 | Lunch |
| 2:00–3:00 | Module 3: Testing and QA with AI |
| 3:00–3:30 | Module 4: Transparency and Governance |
| 3:30–4:00 | Wrap-up |

## Tools You'll Use

### Google Gemini Code Assist
- Best for: Deep code analysis (1M token context), detailed reasoning, multi-file planning with Agent Mode
- Access: [Setup instructions in environment-setup.md](environment-setup.md) — install the VS Code extension

### GitHub Copilot
- Best for: Inline code completion, context-aware suggestions, chat-based coding
- Access: Ensure the Copilot extension is active in VS Code

## The QA Refinement Loop

Every lab follows this pattern:

1. **Generate** — Use Gemini Code Assist or Copilot to produce code
2. **Review** — Apply a QA persona to evaluate the output
3. **Refine** — Feed review feedback back and iterate

This is the core skill we're teaching today: **AI output is a draft, not a deliverable.**

## Lab Difficulty Tiers

Each lab has three levels. Start where you're comfortable and stretch up:

| Tier | Experience Level | Description |
|---|---|---|
| **Base** | 2–5 years | Core task with guided steps |
| **Intermediate** | 5–15 years | Extended task with less scaffolding |
| **Stretch** | 15–25 years | Open-ended challenge, minimal guidance |

## Quick Reference: Effective AI Prompts

### For Gemini Code Assist (deep analysis and reasoning)
```
Analyze this Python function and identify potential edge cases
that could cause failures in production. For each edge case,
suggest a specific test that would catch it.

[paste code here]
```

### For Copilot (inline generation)
```python
# Write a function that validates an email address
# and returns a tuple of (is_valid: bool, error_message: str | None)
# Handle: empty input, missing @, invalid domain, length > 254
```

### For Code Review (QA persona)
```
Act as a security auditor reviewing this code for a production
deployment. Check for:
- Input validation gaps
- Injection vulnerabilities
- Authentication/authorization issues
- Sensitive data exposure

Provide findings in a table: Issue | Severity | Location | Fix
```

## Repository Structure

You'll work with **two repos** today:

```
nypl-ai-engineering-workshop/    # Workshop instructions and exercises
├── labs/                        # Your lab instructions and starter code
│   ├── lab-1-code-analysis/
│   ├── lab-2-feature-build-sprint/
│   ├── lab-3-ai-test-suite/
│   └── lab-4-code-review-tagging/
├── capstone/                    # Final challenge
└── qa-framework/                # QA personas for reviewing AI output

python-utils/                    # The Python codebase you'll work with
├── src/nypl_py_utils/classes/   # S3Client (Labs 2-3), KmsClient (capstone)
└── tests/                       # Existing test suite
```

## Need Help?

- Raise your hand — facilitators are circulating
- Check the `solution/` folder in each lab if you get stuck
- Pair with a neighbor — two perspectives are better than one
