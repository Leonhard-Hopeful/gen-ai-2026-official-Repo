# Kawood Mastery Challenge — Variables

Master variable assignment, scope, and naming conventions to write clean, understandable Python code.

## Question 1: What is a Variable?
A variable is a named reference to an object in memory. When you write `x = 5`, what happens?
- B. Python creates an integer object (5), assigns it to the name x; x is a reference (label) pointing to that object—this is crucial: x doesn't contain 5, it references the object 5- C. x is a container holding 5- A. x and 5 are the same thing- D. Variables don't exist in Python
**Answer: B** — Variables are references, not containers.

---

## Question 2: Variable Naming Conventions
Python convention is `snake_case` for variables: `learning_rate`, not `learningRate`. Why conventions?
- B. Conventions make code readable and consistent—teammates expect this style; readability is maintenance; PEP 8 standardizes Python style—following conventions prevents style debates and makes code professional- C. Naming doesn't matter- A. Use whatever style you want- D. Conventions are just suggestions
**Answer: B** — Conventions are social agreements for clarity.

---

## Question 3: Reserved Words
You can't use `import`, `if`, `for` as variable names—they're reserved. Why?
- D. Reserved words are language keywords—using them as variables breaks parsing—Python can't distinguish between keyword and variable name, causing syntax errors- B. Reservations are arbitrary- C. You can use them with escaping- A. Reservations don't exist
**Answer: D** — Keywords are language structure; can't rebind.

---

## Question 4: Variable Scope (Local vs Global)
```python
x = 10  # global
def func():
    x = 20  # local
    print(x)
func()
print(x)
```
What prints?
- D. Prints 20 (in func, local x shadows global), then 10 (global x)—scope determines which variable is accessed; local masks global; good practice: minimize globals, prefer function parameters and returns- C. Prints 10, then 10- A. Prints 20, then 20- B. Error: duplicate x
**Answer: D** — Local scope shadows global scope.

---

## Question 5: Variable Lifetime
An object is created, assigned to x, then x is reassigned to a different object. What happens to the first object?
- A. The first object is unreferenced—Python's garbage collector eventually deletes it (when reference count reaches 0)—memory is freed—objects live as long as they're referenced- D. Objects persist forever- C. Objects are manually deleted- B. Reassignment deletes immediately
**Answer: A** — Garbage collection frees unreferenced objects.

---

## Question 6: Mutable vs Immutable
```python
x = [1, 2, 3]  # list (mutable)
y = x
y.append(4)
```
Now what's x?
- A. x is also [1, 2, 3, 4]—x and y reference the same list object; modifying through y affects x—mutable objects can be changed; references point to the same changeable object- D. x is still [1, 2, 3]- C. x and y are independent- B. Append doesn't work on lists
**Answer: A** — Mutable objects are shared across references.

---

## Question 7: Variable Shadowing in Nested Scopes
```python
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
```
What prints?
- D. Prints 3 (inner's local x), then 2 (outer's local x)—each scope has its own x; inner shadows outer shadows global—nested scopes create separate namespaces- A. Prints 3, then 3- C. Prints 1, then 1- B. Error: multiple definitions
**Answer: D** — Nested scopes each have their own namespace.

---

## Question 8: Nonlocal and Global Keywords
Inside a function, you want to modify a variable from enclosing scope (not global). Use `nonlocal`:
```python
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    inner()
outer()
```
What does `nonlocal` do?
- C. `nonlocal x` allows inner to modify outer's x (not create a local x)—without nonlocal, assignment creates a local variable; nonlocal breaks out to enclosing scope- B. nonlocal doesn't exist- A. nonlocal and global are the same- D. nonlocal is just a comment
**Answer: C** — nonlocal modifies enclosing scope.

---

## Question 9: Object Identity vs Equality
```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
```
What's the difference?
- C. `x == y` checks value equality (both are [1,2,3], True); `x is y` checks identity (are they the same object?, False)—== is for content, is for identity—use == for data comparison- A. They're equivalent- B. is and == do the same thing- D. Only one is meaningful
**Answer: C** — == compares content; is compares identity.

---

## Question 10: Variable Type Hints
Python allows type hints: `x: int = 5`. Do type hints enforce types?
- B. No—type hints are documentation and enable IDE/type-checker support, but Python doesn't enforce them at runtime—you can assign x = "hello" without error; type hints are optional aids, not constraints- A. Type hints enforce types strictly- D. Type hints are compiled- C. Python doesn't support type hints
**Answer: B** — Type hints are optional documentation.
