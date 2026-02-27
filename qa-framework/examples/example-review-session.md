# Example Review Session: Generate > Review > Refine

This walkthrough demonstrates the full QA Refinement loop on a realistic task.

## The Task

Build a function that processes a list of user records and returns summary statistics.

---

## Step 1: Generate

**Prompt to Copilot:**
```python
# Write a function that takes a list of user dicts with keys
# 'name', 'age', 'department' and returns a summary dict with:
# - total_users: count of users
# - average_age: mean age
# - departments: dict of department -> count
```

**AI Output:**
```python
def get_user_summary(users):
    total = len(users)
    avg_age = sum(u['age'] for u in users) / len(users)
    depts = {}
    for u in users:
        d = u['department']
        if d in depts:
            depts[d] += 1
        else:
            depts[d] = 1
    return {
        'total_users': total,
        'average_age': avg_age,
        'departments': depts
    }
```

This looks correct at first glance. But let's review it.

---

## Step 2: Review (Edge Case Hunter)

**Prompt in Gemini Code Assist chat:**
```
Act as an edge case hunter. Review this function for inputs
that would cause failures:

[paste function above]
```

**Persona Findings:**

| Edge Case | Input | What Happens | Severity |
|---|---|---|---|
| Empty list | `[]` | `ZeroDivisionError` on line 3 | **Critical** |
| Missing 'age' key | `[{'name': 'Jo'}]` | `KeyError: 'age'` | High |
| Non-numeric age | `[{'name': 'Jo', 'age': 'thirty', 'department': 'Eng'}]` | `TypeError` in `sum()` | High |
| None in list | `[None, {'name': 'Jo', ...}]` | `TypeError` on subscript | Medium |
| Missing department | `[{'name': 'Jo', 'age': 30}]` | `KeyError: 'department'` | High |

---

## Step 3: Refine

**Prompt to Copilot:**
```
The edge case review found these issues with my function:
1. ZeroDivisionError on empty list
2. KeyError when 'age' or 'department' keys are missing
3. TypeError on non-numeric age values
4. None values in the list cause crashes

Refactor the function to handle all of these gracefully.
Include type hints and a docstring.
```

**Refined Output:**
```python
from typing import Any


def get_user_summary(users: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize a list of user records.

    Args:
        users: List of dicts with 'name', 'age', and 'department' keys.

    Returns:
        Dict with 'total_users', 'average_age', and 'departments' keys.
        Returns zero/empty values for empty or invalid input.
    """
    if not users:
        return {'total_users': 0, 'average_age': 0.0, 'departments': {}}

    valid_ages = []
    departments: dict[str, int] = {}

    for user in users:
        if not isinstance(user, dict):
            continue

        age = user.get('age')
        if isinstance(age, (int, float)):
            valid_ages.append(age)

        dept = user.get('department')
        if dept is not None:
            departments[dept] = departments.get(dept, 0) + 1

    return {
        'total_users': len(users),
        'average_age': sum(valid_ages) / len(valid_ages) if valid_ages else 0.0,
        'departments': departments,
    }
```

---

## What Changed

| Before | After | Why |
|---|---|---|
| No empty list check | Early return for empty input | Prevents ZeroDivisionError |
| Direct key access `u['age']` | `.get('age')` with type check | Handles missing/invalid keys |
| No type hints | Full type annotations | Clarity for team and AI tools |
| No docstring | Descriptive docstring | Self-documenting |
| Single-letter variable `d` | Descriptive name `dept` | Readability |

## Key Takeaway

The AI's first output was **functionally correct for the happy path** but would crash on 5 different realistic inputs. One review pass caught all of them. This is why we never ship the first draft.
