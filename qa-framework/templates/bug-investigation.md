# Bug Investigation Template

Use this template to systematically diagnose bugs with AI assistance.

## The Prompt

```
I'm investigating a bug. Help me diagnose it systematically.

**Symptom:** [What's happening]
**Expected behavior:** [What should happen]
**Reproduction steps:**
1. [step 1]
2. [step 2]
3. [step 3]

**Environment:** Python [version], [OS], [relevant packages]

**Error output (if any):**
[paste error/traceback]

**Relevant code:**
[paste the code where the bug likely lives]

Walk me through a diagnosis:
1. What are the most likely causes, ranked by probability?
2. For each cause, what's the quickest way to confirm or rule it out?
3. What additional information would help narrow it down?
4. Suggest a minimal test case that would reproduce this bug.
```

## Follow-Up Prompts

Once the AI identifies likely causes:

```
The issue appears to be [cause]. Now:
1. Write a test that reproduces this bug (the test should FAIL right now)
2. Suggest the minimal fix
3. Write a test that verifies the fix works
4. Are there related places in the codebase where this same bug pattern might exist?
```

## Tips

- **Don't just paste the error**: Give context about what you were doing
- **Include the code**: AI can't diagnose what it can't see
- **Verify the fix independently**: Don't trust the AI's fix without testing
- **Check for related bugs**: The same pattern often repeats in a codebase
