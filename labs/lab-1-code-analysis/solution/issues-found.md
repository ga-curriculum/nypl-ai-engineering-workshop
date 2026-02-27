# Lab 1: Issues in the Starter Code — Answer Key

These are the issues Gemini Code Assist should identify when asked to analyze `inventory_manager.py`.

## Security Issues

| Issue | Location | Severity |
|---|---|---|
| Hardcoded database password | Line 5: `DB_PASSWORD = "bookstore_admin_2026"` | Critical |

## Resource Management Issues

| Issue | Location | Severity |
|---|---|---|
| File handle not closed | `load_inventory()`: `f = open()` without `with` or `close()` | High |
| File handle not closed | `save_inventory()`: same problem | High |

## Logic Bugs

| Issue | Location | Severity |
|---|---|---|
| Duplicate search results | `search_books()`: A book matching both title AND author is added twice | High |
| Mutation during iteration | `remove_book()`: `inventory.pop(i)` inside `for i in range(len())` can skip items or raise IndexError | Critical |
| No discount validation | `apply_discount()`: Discount > 1.0 makes prices negative | Medium |
| Floating point display | `generate_report()`: `str(item["price"])` may show `35.989999...` | Low |

## Edge Case Gaps

| Issue | Location | Severity |
|---|---|---|
| Empty inventory not handled | `calculate_total_value()`: works but returns 0 without making it explicit | Low |
| Missing key crashes | `search_books()`: `inventory[i]["title"]` crashes if key is missing | Medium |
| File not found crash | `load_inventory()`: No check if file exists | High |
| Empty query returns nothing | `search_books()`: No handling for empty string query | Low |

## Readability Issues

| Issue | Location | Severity |
|---|---|---|
| No type hints | All functions | Medium |
| No docstrings | All functions | Medium |
| Non-Pythonic loops | `for i in range(len(inventory))` instead of `for item in inventory` | Low |
| String concatenation in loop | `generate_report()`: `report +=` in a loop instead of `join()` | Low |
| Generic variable names | `data`, `results`, `low`, `f` | Low |

## Summary

| Category | Count |
|---|---|
| Security | 1 |
| Resource management | 2 |
| Logic bugs | 4 |
| Edge case gaps | 4 |
| Readability | 5 |
| **Total** | **16** |
