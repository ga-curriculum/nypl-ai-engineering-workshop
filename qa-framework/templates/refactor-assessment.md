# Refactor Assessment Template

Use this template to evaluate whether and how to refactor code with AI assistance.

## The Prompt

```
I'm considering refactoring the following code. Before I change
anything, help me assess whether a refactor is warranted and
what approach to take.

**Current code:**
[paste code]

**Why I want to refactor:**
[explain the motivation — readability, performance, extensibility, etc.]

Assess:
1. **Is a refactor warranted?** What's the current code's biggest weakness?
2. **Risk assessment** — What could break? What depends on this code?
3. **Proposed approach** — How would you refactor this? Show before/after.
4. **Scope control** — What's the minimum viable refactor vs. ideal refactor?
5. **Test impact** — What tests need to change? What new tests are needed?
6. **Rollback plan** — If the refactor causes issues, how do we revert safely?
```

## Follow-Up: After the Refactor

```
I've completed the refactor. Review the before and after:

**Before:**
[paste original code]

**After:**
[paste refactored code]

Verify:
1. Behavioral equivalence — Does the refactored code do exactly the same thing?
2. Test coverage — Are all original tests passing? New edge cases covered?
3. Readability improvement — Is this actually clearer than before?
4. No scope creep — Did I change only what was necessary?
```

## Tips

- **Refactor for a reason**: Don't refactor code just because AI suggests it
- **One thing at a time**: Don't combine feature changes with refactoring
- **Tests first**: Ensure test coverage before refactoring, not after
- **Small steps**: Prefer multiple small refactors over one large one
