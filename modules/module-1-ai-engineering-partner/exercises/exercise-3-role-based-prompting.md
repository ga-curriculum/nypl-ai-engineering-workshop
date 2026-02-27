# Exercise 3: Role-Based Prompting

## Duration: 12 minutes

## Purpose
See how assigning a role to the AI changes its output. The same code reviewed by a "security engineer" vs. a "performance engineer" produces very different feedback.

## Setup
Use this Python code as your review target:

```python
import json

def load_config(filepath):
    with open(filepath) as f:
        data = json.load(f)
    db_host = data["database"]["host"]
    db_pass = data["database"]["password"]
    return db_host, db_pass

def get_users(db_connection, department):
    query = f"SELECT * FROM users WHERE department = '{department}'"
    results = db_connection.execute(query)
    all_users = list(results.fetchall())
    return all_users

def calculate_average_rating(reviews):
    total = 0
    for review in reviews:
        total += review["rating"]
    return total / len(reviews)
```

## Instructions

### Step 1: Choose a role (2 min)

Pick one of these roles and write a prompt that assigns it:

**Security Engineer:**
```
You are a senior security engineer reviewing Python code
before a production deployment. Identify vulnerabilities,
injection risks, and credential handling issues.
```

**Performance Engineer:**
```
You are a performance engineer analyzing Python code for
efficiency. Identify complexity issues, unnecessary memory
usage, and optimization opportunities.
```

**QA Engineer:**
```
You are a QA engineer writing edge case tests. For each
function, identify inputs that could cause failures and
write pytest test cases for them.
```

### Step 2: Run your role-based prompt on the code above (3 min)

Enter the code and your role prompt into the Gemini Code Assist chat panel. Review the output.

### Step 3: Try a different role (3 min)

Switch to a different role and run it on the same code. Compare:
- What did role 1 catch that role 2 missed?
- What did role 2 catch that role 1 missed?

### Step 4: Reflect (4 min)

| Role | Issues Found | Most Valuable Finding |
|---|---|---|
| Role 1: | | |
| Role 2: | | |

**Discussion questions:**
- Which role found the most critical issue in this code?
- What roles would be most useful for code you write at work?
- How does role-based prompting connect to the QA Framework you'll use in labs today?

## Answer Key (for facilitators)

The code above contains:
- **Security:** SQL injection via f-string in `get_users`, password loaded in plaintext
- **Performance:** Loading all results into a list (`fetchall()`) instead of streaming, O(n) loop that could be `sum()`
- **QA edge cases:** Empty reviews list causes `ZeroDivisionError`, missing "rating" key causes `KeyError`, missing config keys cause `KeyError`, file not found not handled
