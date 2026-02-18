# Pre-Commit Review Template

Run this prompt sequence **before every commit** of AI-generated or AI-assisted code.

## The Prompt

```
I'm about to commit the following code changes. Before I do,
review them as a senior engineer doing a pre-commit check.

Verify:
1. No hardcoded secrets, API keys, or credentials
2. No debug code (print statements, console.log, breakpoints)
3. All new functions have type hints and docstrings
4. Error handling is appropriate (not swallowing exceptions)
5. No commented-out code blocks
6. Variable/function names are clear and consistent
7. No TODO comments that should be resolved before committing

Format your review as:
PASS ✓ — Ready to commit
or
HOLD ✗ — Fix these issues first:
[list of issues]

Code to review:
[paste your diff or changed code]
```

## When to Use

- Before every `git commit` of AI-generated code
- Before pushing to a shared branch
- As the final step in any lab exercise

## Workshop Integration

Introduce this template in **Lab 1** and reinforce it in every subsequent lab. By the capstone, participants should use it automatically.
