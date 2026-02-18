# Lab 1 Review Checklist — Code Readability Reviewer

After completing Lab 1, apply this checklist to your final code.

## Persona: Code Readability Reviewer

Use this prompt with Gemini to review your finished code:

```
Act as a code readability reviewer. Evaluate the following Python
code with this standard: a new team member should be able to
understand and modify it without external help.

Evaluate:
1. Naming — Are variables, functions, and parameters clearly named?
2. Structure — Are functions focused and under 30 lines?
3. Documentation — Do functions have docstrings and type hints?
4. Consistency — Is the style consistent throughout?
5. Idioms — Does it use Pythonic patterns where appropriate?

For each issue:
| Issue | Location | Suggested Improvement |

[paste your code here]
```

## Self-Review Checklist

Before considering this lab complete, verify:

- [ ] All functions have type hints on parameters and return types
- [ ] All functions have docstrings explaining purpose, args, and returns
- [ ] No hardcoded secrets or credentials remain in the code
- [ ] File handles use context managers (`with` statements)
- [ ] No mutation during iteration bugs
- [ ] Search results don't contain duplicates
- [ ] Edge cases are handled (empty input, missing keys, file not found)
- [ ] String building uses `join()` or f-strings, not `+=` in loops
- [ ] Loops use `for item in collection` not `for i in range(len(...))`
- [ ] Variable names are descriptive (no single-letter names outside comprehensions)

## Scoring

Count how many checklist items you addressed:

| Score | Assessment |
|---|---|
| 10/10 | Excellent — production-ready quality |
| 7-9 | Good — minor improvements remain |
| 4-6 | Needs work — review the solution for patterns you missed |
| 0-3 | Revisit Module 1 slides on high-context prompting |
