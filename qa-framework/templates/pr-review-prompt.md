# PR Review Prompt Template

Use this template to conduct AI-assisted pull request reviews.

## The Prompt

```
You are reviewing a pull request. The PR makes the following changes:

**PR Title:** [title]
**PR Description:** [description]
**Files Changed:** [list files]

Review this PR against these criteria:

## Correctness
- Does the code do what the PR description says?
- Are there logic errors or missed requirements?

## Security
- Any new attack surfaces introduced?
- Input validation present where needed?

## Testing
- Are the changes tested?
- Do existing tests still pass?
- Are edge cases covered?

## Readability
- Is the code clear to someone unfamiliar with this PR?
- Are naming conventions followed?

## Performance
- Any performance regressions?
- Efficient use of resources?

Provide your review as:
### Approve / Request Changes / Comment

**Summary:** [1-2 sentence summary]

**Findings:**
| Category | Finding | Severity | File:Line |
|---|---|---|---|

**Questions for the author:**
[list any clarifying questions]

Changes to review:
[paste diff]
```

## Tips for Effective AI PR Reviews

1. **Provide context**: Include the PR description so the AI understands intent
2. **Include the diff, not just the new code**: The AI needs to see what changed
3. **Don't skip human review**: Use AI review as a first pass, not a replacement
4. **Cross-reference with tests**: Ask the AI to verify that tests cover the changes
