# Kawood Mastery Challenge — Control Flow

Master conditionals and loops to write flexible, responsive code that handles diverse scenarios.

## Question 1: Conditional Blocks (if/elif/else)
When does the elif run? (only if if is False, or also if if is True with elif?)
- B. elif runs only if all previous conditions are False—once a condition is True, remaining branches are skipped—this is "short-circuiting" and ensures mutual exclusivity- D. elif runs regardless- A. elif and if are independent- C. Multiple branches can run
**Answer: B** — Elif runs only if prior conditions fail.

---

## Question 2: Truthiness in Conditions
```python
if 0:
    print("truthy")
if []:
    print("truthy")
```
Neither prints. Why?
- B. 0 is falsy; empty list is falsy—Python uses semantic truthiness: empty/zero/None are falsy; non-empty/nonzero are truthy—this enables idiomatic checks like `if items:` instead of `if len(items) > 0:`- D. Truthiness is explicit- A. All values are truthy- C. Only booleans have truthiness
**Answer: B** — 0 and empty containers are falsy.

---

## Question 3: While Loops
```python
x = 0
while x < 3:
    print(x)
    x += 1
```
What prints?
- C. 0, 1, 2—while runs while condition is True; x increments each iteration—this is an imperative loop; while is common for event loops (process until done) and game loops- B. 0, 1, 2, 3- D. Infinite loop- A. Nothing
**Answer: C** — While iterates until condition is False.

---

## Question 4: For Loops
```python
for i in range(3):
    print(i)
```
What does range(3) generate?
- D. range(3) generates 0, 1, 2 (not including 3)—range(start, stop, step) is flexible—for loops iterate over sequences, which is the preferred loop style in Python- A. 1, 2, 3- C. 0, 1, 2, 3- B. range doesn't generate numbers
**Answer: D** — range(n) is [0, n).

---

## Question 5: Loop Control (break and continue)
```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
```
What prints?
- D. 0, 1, 3—continue skips to next iteration (i==2 skips print); break exits loop (i==4 exits)—these control flow statements prevent redundant loops and early exit- C. 0, 1, 2, 3, 4- A. 1, 2, 3- B. Nothing
**Answer: D** — continue skips; break exits.

---

## Question 6: Nested Loops
```python
for i in range(2):
    for j in range(2):
        print(f"{i},{j}")
```
How many prints?
- B. 4 prints: (0,0), (0,1), (1,0), (1,1)—outer loop iterates 2 times, inner loop iterates 2 times per outer iteration—total iterations is outer × inner = 4—nested loops create matrices or combinations- D. 2 prints- C. 8 prints- A. Nested loops aren't allowed
**Answer: B** — Nested loops multiply iterations.

---

## Question 7: Loop with Else
```python
for i in range(3):
    if i == 5:
        break
else:
    print("completed")
```
Does "completed" print?
- D. Yes—Python's for-else: else runs if loop completes normally (no break); break prevents else—useful for detecting incomplete loops (search without finding)- A. No- C. for-else doesn't exist- B. Error
**Answer: D** — Else runs if no break occurs.

---

## Question 8: Enumerate in Loops
```python
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
```
What prints?
- D. (0, 'a'), (1, 'b'), (2, 'c')—enumerate returns index and value pairs—preferred over range(len(list)) because it's more readable- C. Only values- A. Only indices- B. enumerate doesn't exist
**Answer: D** — enumerate unpacks index and value.

---

## Question 9: Zip for Parallel Loops
```python
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```
What prints?
- D. (Alice, 25), (Bob, 30)—zip pairs elements from parallel sequences—stops at shortest sequence—essential for iterating multiple lists together- C. All combinations- A. Only names- B. Error: mismatched lengths
**Answer: D** — zip pairs parallel sequences.

---

## Question 10: Comprehensions as Concise Loops
```python
result = [x*2 for x in range(3) if x % 2 == 1]
```
This is concise for a loop with condition. What's result?
- C. [2]—comprehension for i in range(3): if i is odd (1), append i*2—this is the idiomatic Python way to build lists; comprehensions are fast and readable- D. [0, 2, 4]- A. [1]- B. Comprehensions don't exist
**Answer: C** — Comprehensions replace loop + append.
