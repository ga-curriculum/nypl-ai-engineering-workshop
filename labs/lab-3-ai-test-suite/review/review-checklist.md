# Lab 3 Review Checklist — Test Coverage Analyst

After completing Lab 3, apply this checklist to your AI-generated test suite.

## Persona: Test Coverage Analyst

Use this prompt in the Gemini Code Assist chat panel to review your test suite:

```
Act as a test coverage analyst reviewing the following Python test
suite against the source code it's testing. Evaluate completeness
and correctness.

Check for:
1. Missing coverage — What code paths have no tests?
2. Edge cases — Are boundary conditions tested?
3. Assertion quality — Are assertions specific enough? Any tautologies?
4. Test isolation — Do tests depend on each other or shared state?
5. Error paths — Are failure modes tested (exceptions, invalid input)?
6. Hallucinated tests — Do any tests assert things the code doesn't do?

For each finding:
| Gap | What's Missing | Severity | Suggested Test |

Source code:
[paste your Lab 2 code here]

Test suite:
[paste your Lab 3 tests here]
```

## Self-Review Checklist

Before considering this lab complete, verify:

- [ ] Every public function has at least one test
- [ ] Happy path is tested for each function with specific assertions
- [ ] At least one edge case per function (empty input, boundary values)
- [ ] Error handling paths are tested (expected exceptions are raised)
- [ ] Assertions check specific values, not just `is not None` or `is True`
- [ ] No tautological assertions (`assert result == result`, `assert True`)
- [ ] No hallucinated tests (tests asserting behavior the code doesn't have)
- [ ] Tests are independent — can run in any order without shared state
- [ ] Test names clearly describe what they verify (`test_empty_input_returns_empty_list`)
- [ ] Mocking is used only for external dependencies, not for the function under test

## Key Question

For each test in your suite, ask yourself:

**"If all tests pass, am I confident the code works correctly?"**

If a broken implementation would still pass your tests, the test suite needs more work.

## Scoring

Count how many checklist items you addressed:

| Score | Assessment |
|---|---|
| 10/10 | Excellent — trustworthy test suite |
| 7-9 | Good — minor gaps in coverage or assertion quality |
| 4-6 | Needs work — hallucinated or tautological tests remain |
| 0-3 | Revisit Module 3 slides on test quality and the Generate > Review > Refine loop |
