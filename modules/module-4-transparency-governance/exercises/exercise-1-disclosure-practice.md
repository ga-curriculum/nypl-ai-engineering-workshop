# Exercise 1: Disclosure Practice

## Duration: 10 minutes

## Purpose
Practice writing AI disclosure statements for realistic engineering scenarios.

## Instructions

### Scenario A

You used Gemini Code Assist to design the architecture for a new user authentication module. You then used Copilot to implement it, accepting many inline suggestions. You wrote the tests yourself but used Gemini Code Assist to review them.

**Write a PR description for this work.** Include an "AI Assistance" section that accurately describes what was AI-generated, AI-assisted, and human-written.

Your PR description:

```
## Summary
[Your summary]

## AI Assistance
[Your disclosure]

## Test Plan
[Your test plan]
```

### Scenario B

A colleague submits a PR with 400 lines of new code and no mention of AI tools. The code is well-structured but has an unusually consistent style — every function has perfect docstrings, type hints, and error handling. You suspect it's AI-generated.

**Questions:**
1. Would you ask about AI usage in your review? Why or why not?
2. Does it matter if the code is AI-generated, if it passes all tests and reviews?
3. What would your team's policy say about this situation?

### Scenario C

You're writing a library that will be open-sourced under the MIT license. You want to use Copilot to generate utility functions.

**Questions:**
1. What licensing risks should you consider?
2. How would you mitigate those risks?
3. Would you disclose AI usage in the project's README or CONTRIBUTING guide?

## Group Discussion (3 min)

Share your Scenario A PR description with a neighbor. Compare:
- How much detail did you each include?
- Would a reviewer find your disclosure helpful?
- What's the right level of detail — too much is noise, too little is hiding information?
