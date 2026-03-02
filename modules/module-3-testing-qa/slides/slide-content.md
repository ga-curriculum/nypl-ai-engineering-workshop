# Module 3: Testing and QA with AI — Slide Content

> These are the content notes for each slide. Convert to your slide deck tool (Google Slides, Keynote, etc.) using GA templates.

---

## Slide 1: Title

**Testing and QA with AI**
Module 3 | 60 minutes

---

## Slide 2: Learning Objectives

By the end of this module, you will:
1. Generate a pytest test suite using AI tools
2. Identify hallucinated tests in AI-generated test suites
3. Apply the test coverage analyst persona to evaluate test quality
4. Use the Generate > Review > Refine loop specifically for testing

---

## Slide 3: The Promise — Generate a Test Suite in 60 Seconds

**Demo:** Watch Copilot generate a full test suite.

Given this function:
```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """Apply a percentage discount to a price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return round(price * (1 - discount_percent / 100), 2)
```

Type this comment and let Copilot generate:
```python
# Write pytest tests for calculate_discount
```

*Copilot produces 5–8 tests in seconds. They all pass.*

**But ask yourself: Do these tests verify the right things?**

Let's look closer.

---

## Slide 4: The Pitfall — Tests That Lie

AI-generated tests have three common anti-patterns:

### 1. Tautological assertions
```python
def test_calculate_discount():
    result = calculate_discount(100, 10)
    assert result == result  # Always passes. Tests nothing.
```

### 2. Hallucinated behavior
```python
def test_discount_rounds_up():
    # Tests behavior the function doesn't have
    result = calculate_discount(10.005, 10)
    assert result == 9.01  # Assumes rounding up — function uses round()
```

### 3. Over-mocking
```python
@patch('module.calculate_discount', return_value=90.0)
def test_discount(mock_fn):
    result = mock_fn(100, 10)
    assert result == 90.0  # You mocked the function you're testing!
```

**Each of these tests passes. None of them verify real behavior.**

---

## Slide 5: What Makes a Good Test?

| Quality | Good Test | Bad Test |
|---|---|---|
| **Assertion specificity** | Asserts exact expected values | `assert result is not None` |
| **Edge cases** | Tests boundaries (0%, 100%, negative) | Only tests the happy path |
| **Independence** | Can run in any order | Depends on another test's state |
| **Naming** | `test_zero_discount_returns_original_price` | `test_1`, `test_2`, `test_3` |
| **Mocking** | Mocks external dependencies only | Mocks the function being tested |
| **Readability** | Arrange / Act / Assert structure | 20 lines of setup, 1 line of assertion |
| **Negative tests** | Tests that invalid input raises errors | Only tests valid input |

**Rule of thumb:** If a test would still pass with a broken implementation, it's not testing anything useful.

---

## Slide 6: Introducing the Test Coverage Analyst

This is a QA persona from our framework. Use it to review AI-generated tests.

### Prompt template (use in Gemini Code Assist):

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
[paste source code]

Test suite:
[paste test code]
```

**Why Gemini Code Assist for this?** Its 1M token context window can hold both source code and tests together — it sees the full picture.

---

## Slide 7: Demo — Finding Hallucinated Assertions

**Source function:**
```python
def get_active_users(users: list[dict]) -> list[dict]:
    """Return users where 'is_active' is True."""
    return [u for u in users if u.get("is_active") is True]
```

**AI-generated test suite (5 tests):**

```python
def test_returns_active_users():
    users = [{"name": "Alice", "is_active": True}, {"name": "Bob", "is_active": False}]
    result = get_active_users(users)
    assert len(result) == 1
    assert result[0]["name"] == "Alice"          # GOOD — specific assertion

def test_empty_list():
    assert get_active_users([]) == []             # GOOD — tests edge case

def test_all_inactive():
    users = [{"name": "Bob", "is_active": False}]
    assert get_active_users(users) == []          # GOOD — boundary case

def test_sorts_by_name():
    users = [{"name": "Zara", "is_active": True}, {"name": "Alice", "is_active": True}]
    result = get_active_users(users)
    assert result[0]["name"] == "Alice"           # HALLUCINATED — function doesn't sort

def test_excludes_deleted_users():
    users = [{"name": "Alice", "is_active": True, "deleted": True}]
    result = get_active_users(users)
    assert len(result) == 0                       # HALLUCINATED — function doesn't check 'deleted'
```

**Tests 4 and 5 are hallucinated.** They assert behavior the function doesn't have. Test 4 might even pass by coincidence depending on input order.

*Ask the room: "Would you have caught these in a code review?"*

---

## Slide 8: Generate > Review > Refine for Testing

The workshop loop applies directly to testing:

```
  ┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
  │  GENERATE   │────>│     REVIEW       │────>│     REFINE      │
  │             │     │                  │     │                 │
  │  Copilot    │     │  Gemini Code     │     │  Copilot fills  │
  │  generates  │     │  Assist reviews  │     │  gaps, fixes    │
  │  test suite │     │  with Test       │     │  hallucinated   │
  │             │     │  Coverage        │     │  assertions     │
  │             │     │  Analyst persona │     │                 │
  └─────────────┘     └──────────────────┘     └─────────────────┘
       │                                              │
       └──────────────── repeat ──────────────────────┘
```

### The dual-tool loop for testing:
1. **Copilot generates** — Fast test creation with inline suggestions
2. **Gemini Code Assist reviews** — Apply the Test Coverage Analyst persona with both source and tests in context
3. **Copilot fills gaps** — Use the review findings to generate missing tests and fix bad assertions

**Each pass improves the test suite.** Two rounds usually catches the worst hallucinations.

---

## Slide 9: Lab 3 Preview

**Lab 3: AI Test Suite** (30 minutes)

You'll evaluate AI-generated tests for the original `s3_client.py` and learn to spot hallucinated assertions. (You do *not* need to have finished Lab 2.)

Three tiers:
- **Base:** Generate tests with Copilot, apply Test Coverage Analyst persona, find at least 1 hallucinated test
- **Intermediate:** Use Gemini Code Assist to find coverage gaps, write tests for 3 gaps, check for tautologies
- **Stretch:** Compare Copilot vs. Gemini Code Assist test generation, create a test quality scorecard

**Hallucinated test exercise:** In `starter/` you'll find a test file with intentional hallucinations mixed in. Can you spot them?

---

## Slide 10: Recap

What we covered:
1. AI can generate test suites in seconds — but speed doesn't mean quality
2. Three anti-patterns to watch for: tautological assertions, hallucinated behavior, over-mocking
3. The Test Coverage Analyst persona systematically evaluates test quality
4. Use Gemini Code Assist for test review (1M context holds source + tests together)
5. Generate > Review > Refine works for testing too — Copilot generates, Gemini Code Assist reviews, Copilot fills gaps

**Up next:** Lab 3 — put your tests under the microscope.
