# Kawood Mastery Challenge — Data Types

Master Python's core data types (int, float, str, bool, list, dict, set, tuple) to manipulate information effectively.

## Question 1: Numeric Types (int vs float)
Compare: `x = 5` (int) vs `x = 5.0` (float). When use each?
- A. Use int for whole numbers (counters, indices); use float for decimals (probabilities, measurements)—int is exact, float has rounding errors—choosing the right type prevents precision issues- B. They're interchangeable- D. ints are always better- C. floats are always better
**Answer: A** — int is precise; float is approximate.

---

## Question 2: String Manipulation
Python has string methods: `"hello".upper()` returns "HELLO". Are strings mutable?
- D. No—strings are immutable—upper() returns a new string, doesn't modify the original—immutability makes strings safe for dict keys and hashable operations- A. Strings are mutable- C. Immutability doesn't apply- B. Methods modify strings in-place
**Answer: D** — Strings are immutable; methods return new strings.

---

## Question 3: Boolean Logic
In Python, `bool` is a subclass of int: `True == 1`, `False == 0`. Why?
- A. Historically, booleans are 1s and 0s in hardware; Python preserves this—True can be used in arithmetic (3 + True = 4)—understanding this quirk prevents surprises with boolean arithmetic- D. They're completely separate- B. Booleans are primitive- C. This relationship doesn't exist
**Answer: A** — bool is a subclass of int.

---

## Question 4: Type Conversion
You read a number from user input: `x = input()` returns a string. To compute with it, convert: `int(x)`. What happens if x = "abc"?
- A. ValueError—int("abc") fails because "abc" isn't a valid integer—type conversion assumes input is valid; always validate or handle exceptions- C. x becomes 0- D. Conversion is automatic- B. abc is treated as octal
**Answer: A** — Type conversion fails on invalid input.

---

## Question 5: None Type
```python
def func():
    pass  # does nothing
x = func()
print(x)
```
What's x?
- A. None—functions without explicit return return None; None is the null value in Python—it's useful for representing "no value" or uninitialized state- B. 0- C. An error- D. Empty string
**Answer: A** — Implicit return is None.

---

## Question 6: Type Checking
You want to verify x is an int before using it in arithmetic. How?
- C. Use `isinstance(x, int)`—returns True if x is an int or bool (since bool is a subclass)—isinstance is the Pythonic way to check types- B. Use `type(x) == int`- D. Just assume and handle errors- A. Type checking isn't possible
**Answer: C** — isinstance is the preferred type check.

---

## Question 7: Numeric Type Coercion
```python
x = 3
y = 2.0
z = x + y
```
What's z, and what type?
- A. z = 5.0 (float)—Python coerces int to float for addition; result type is the "wider" type—int + float → float; this prevents data loss but can hide subtle bugs- B. z = 5 (int)- C. Error: mixing types- D. Type coercion doesn't happen
**Answer: A** — Arithmetic coerces to the wider type.

---

## Question 8: Bytes vs Strings
Python 3 distinguishes `str` (Unicode text, "hello") from `bytes` (raw bytes, b"hello"). When use each?
- C. Use str for text (human-readable); use bytes for binary data (files, network)—encoding/decoding converts between them; confusing them causes Unicode errors- B. They're the same- D. Only use str- A. bytes are obsolete
**Answer: C** — str is text; bytes is binary.

---

## Question 9: Empty Container Behavior
```python
if []:
    print("not empty")
if [1]:
    print("not empty")
```
Empty list is falsy; non-empty is truthy. Why?
- C. Python treats empty containers as falsy (false in boolean context), non-empty as truthy—useful for checking `if my_list:` instead of `if len(my_list) > 0:`—semantic truthiness makes code readable- B. Containers don't have truth values- D. Empty is truthy- A. Truthiness is arbitrary
**Answer: C** — Empty containers are falsy; non-empty are truthy.

---

## Question 10: Type Annotations in Data Types
You write: `x: list[int] = [1, 2, 3]`. What does this declare?
- A. x is a list of ints—type hints can specify container element types (in Python 3.9+)—IDE and type-checkers verify: x = [1, 2, "three"] would be flagged as wrong; hints improve code quality- C. Enforces type at runtime- B. Type annotations don't specify element types- D. Annotations are comments only
**Answer: A** — Type hints specify container element types.
