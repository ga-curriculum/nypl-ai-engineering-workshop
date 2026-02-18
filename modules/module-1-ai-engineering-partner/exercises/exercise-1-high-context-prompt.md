# Exercise 1: Build a High-Context Prompt

## Duration: 10 minutes

## Setup
- Open Google Gemini (web, API, or VS Code extension)
- Have GitHub Copilot active in your editor

## Instructions

### Step 1: Start with a vague prompt (2 min)

Here is a bad prompt:

```
Write a Python function that processes data.
```

Rewrite this as a high-context prompt. Your prompt should include:
- A specific function name
- Clear input and output types
- At least 2 edge cases to handle
- Style requirements (type hints, docstrings, etc.)

**Your scenario:** You're building a user management system. The function should filter a list of user records based on criteria the caller provides.

### Step 2: Test your prompt (3 min)

1. Paste your prompt into Gemini
2. Evaluate the output:
   - Did it match your expectations?
   - What did it get right?
   - What did it miss or get wrong?

### Step 3: Refine (2 min)

Based on the output, revise your prompt. Add any missing context that would have improved the result.

### Step 4: Compare with Copilot (3 min)

Take your refined prompt and use it as a comment in your editor:

```python
# [Paste your prompt as a comment here]
def filter_users(
```

Let Copilot complete the function. Compare:
- How does Copilot's output differ from Gemini's?
- Which tool produced more usable code for this task?

## Record Your Findings

| Version | Tool | Output Quality (1-5) | What worked | What to improve |
|---|---|---|---|---|
| Vague prompt | Gemini | | | |
| High-context prompt | Gemini | | | |
| High-context prompt | Copilot | | | |
