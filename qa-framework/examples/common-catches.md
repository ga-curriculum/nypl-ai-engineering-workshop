# Common Catches: What QA Personas Flag in AI-Generated Code

Real examples of issues found by applying QA personas to AI-generated Python code.

## Security Auditor Catches

### Hardcoded Secrets
```python
# AI generated this for a database connection
DB_PASSWORD = "admin123"
conn = psycopg2.connect(host="localhost", password=DB_PASSWORD)
```
**Fix:** Use environment variables: `os.environ.get("DB_PASSWORD")`

### SQL Injection
```python
# AI generated this query
def get_user(username):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
```
**Fix:** Use parameterized queries: `cursor.execute("SELECT * FROM users WHERE name = %s", (username,))`

### Verbose Error Messages
```python
except Exception as e:
    return {"error": f"Database error at {DB_HOST}:{DB_PORT}: {str(e)}"}
```
**Fix:** Return generic messages to users, log details internally.

---

## Edge Case Hunter Catches

### Empty Input Crashes
```python
def calculate_average(scores):
    return sum(scores) / len(scores)  # ZeroDivisionError on []
```

### Unguarded Dictionary Access
```python
def get_display_name(user):
    return f"{user['first_name']} {user['last_name']}"  # KeyError if keys missing
```

### Off-By-One in Pagination
```python
def get_page(items, page_num, page_size):
    start = page_num * page_size  # Page 0 and page 1 return the same data
    return items[start:start + page_size]
```

---

## Code Readability Reviewer Catches

### Generic Names
```python
def process(data):      # What does it process? What kind of data?
    result = []          # Result of what?
    for item in data:    # What's an item?
        temp = item[0]   # What's at index 0?
        result.append(temp)
    return result
```

### Overly Clever One-Liners
```python
# AI-generated "Pythonic" code
users = {k: [x for x in v if x.get('active')] for k, v in groupby(sorted(data, key=lambda x: x['dept']), key=lambda x: x['dept'])}

# Readable alternative
active_users_by_dept = {}
for user in data:
    if user.get('active'):
        dept = user['dept']
        active_users_by_dept.setdefault(dept, []).append(user)
```

---

## Performance Engineer Catches

### N+1 Query Pattern
```python
def get_order_details(order_ids):
    results = []
    for order_id in order_ids:  # 1000 orders = 1000 queries
        order = db.query(f"SELECT * FROM orders WHERE id = {order_id}")
        results.append(order)
    return results
```
**Fix:** Batch query: `SELECT * FROM orders WHERE id IN (...)`

### String Concatenation in Loop
```python
def build_report(lines):
    report = ""
    for line in lines:
        report += line + "\n"  # Creates new string object each iteration
    return report
```
**Fix:** `return "\n".join(lines)`

---

## Test Coverage Analyst Catches

### Hallucinated Test
```python
def test_user_email_validation():
    user = create_user(email="test@example.com")
    assert user.email_verified == True  # The code has no email_verified field!
```

### Tautological Assertion
```python
def test_get_users():
    users = get_users()
    assert users is not None  # This tells us nothing about correctness
```

### Missing Error Path Test
```python
# Source code raises ValueError on negative input
# But the test suite only tests positive inputs
def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(50, 0.2) == 40
    # Where's test_calculate_discount_negative_price()?
```

---

## Pattern Summary

| Persona | Most Common AI Mistake | Frequency |
|---|---|---|
| Security Auditor | Hardcoded secrets and credentials | Very High |
| Edge Case Hunter | No empty/null input handling | Very High |
| Readability Reviewer | Generic variable names | High |
| Performance Engineer | N+1 query patterns | Medium |
| Junior Dev Reviewer | Advanced patterns without explanation | High |
| Test Coverage Analyst | Hallucinated assertions | Very High |
