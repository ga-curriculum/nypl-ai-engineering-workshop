# Lab 2 Review Checklist — Edge Case Hunter

After completing Lab 2, apply this checklist to your new feature code.

## Persona: Edge Case Hunter

Use this prompt in the Gemini Code Assist chat panel to review your finished code:

```
Act as an edge case hunter reviewing the following Python code.
Your goal is to find inputs and conditions that would cause
unexpected behavior, crashes, or incorrect results.

Check for:
1. Boundary values — Empty inputs, zero, negative numbers, max values
2. Type issues — None, wrong types, mixed types in collections
3. State issues — Uninitialized state, race conditions, stale data
4. Data issues — Unicode, special characters, extremely long strings
5. Environmental — Missing files, network failures, permission errors

For each edge case found:
| Edge Case | Input/Condition | Expected Behavior | Actual Behavior | Severity |

[paste your Lab 2 code here]
```

## Self-Review Checklist

Before considering this lab complete, verify:

- [ ] Empty inputs are handled gracefully (empty lists, empty strings, None)
- [ ] Type mismatches don't cause unhandled exceptions (wrong argument types)
- [ ] Boundary values are handled (zero, negative numbers, very large numbers)
- [ ] Missing dictionary keys don't cause `KeyError` crashes
- [ ] List operations don't cause `IndexError` on empty or short lists
- [ ] Division operations guard against division by zero
- [ ] File operations use context managers and handle missing files
- [ ] String operations handle Unicode and special characters
- [ ] Functions validate their inputs before processing
- [ ] Error messages are descriptive (not just "Error occurred")

## Key Question

For each function in your feature, ask yourself:

**"What input would break this code in production?"**

If you can think of an input that would cause an unhandled exception, the code needs more work.

## Scoring

Count how many checklist items you addressed:

| Score | Assessment |
|---|---|
| 10/10 | Excellent — robust against edge cases |
| 7-9 | Good — most common edge cases handled |
| 4-6 | Needs work — several unhandled edge cases remain |
| 0-3 | Revisit Module 2 slides on context and decomposition |
