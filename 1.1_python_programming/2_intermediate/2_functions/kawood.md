# Kawood Mastery Challenge — Functions

Master function design, arguments, and modularity to write reusable, testable Python code.

## Question 1: Function Purpose and Naming
A function named `f(x)` computes the sum of squares. Why is the name problematic, and how should it be renamed?
- D. `f` gives no hint about what it does; rename to `sum_of_squares(values)` or `compute_variance(data)`—clear names tell readers intent without reading code; vague names force investigation- B. Short names are more efficient- C. Function names don't matter- A. `f` follows mathematical convention
**Answer: D** — Naming is communication; clarity saves debugging time.

---

## Question 2: Return Values vs Side Effects
Compare: function A modifies a global variable; function B returns a new value. Which is better for AI pipelines?
- C. Function B—return values make dependencies explicit (function output comes only from inputs), enabling easy testing, chaining, and parallel execution; side effects hide dependencies and make debugging harder- A. Side effects are more efficient- B. They're equivalent- D. Globals are standard practice
**Answer: C** — Return values are explicit contracts.

---

## Question 3: Function Modularity
Your training script has 200 lines doing: data loading, preprocessing, model training, evaluation. Split or leave monolithic? Why?
- B. Split into functions: `load_data()`, `preprocess()`, `train()`, `evaluate()`—each function has one purpose, is testable independently, and can be reused; monolithic code is harder to test and reuse- A. Monolithic code is simpler- C. Functions are overcomplicating- D. Script length doesn't matter
**Answer: B** — Modularity is testability and reusability.

---

## Question 4: Default Arguments Pitfall
```python
def add_item(item, items=[]):
    items.append(item)
    return items
```
Call `add_item(1)`, then `add_item(2)`. What's in the list on the second call?
- B. [1, 2]—mutable default arguments are evaluated once at function definition, creating a shared list—every call appends to the same list—this is a notorious Python gotcha; use None and create a new list inside- C. [2]- D. [1] and [2] separately- A. Error
**Answer: B** — Mutable defaults are shared traps.

---

## Question 5: *args and **kwargs
When training multiple models, you write: `train_models(*models)` where models is a list of Model objects. What does *args accomplish?
- B. *args unpacks the list into individual positional arguments—`train_models(model1, model2, model3)` receives args = (model1, model2, model3); this enables flexible function signatures that accept variable numbers of arguments- D. *args is just a convention- C. You always need to unpack manually- A. *args doesn't do anything special
**Answer: B** — *args makes variable arguments elegant.

---

## Question 6: Function Composition
You have `preprocess(data)` and `normalize(data)`. To use them together repeatedly, you could write `normalize(preprocess(raw_data))` each time, or compose them. Why compose?
- D. Composing creates a new function `pipeline = compose(preprocess, normalize)` that encodes the sequence—single call to `pipeline(raw_data)` replaces manual nesting; composition is reusable and readable- A. Composition is overcomplicating- B. Manual nesting is fine- C. Composition doesn't save anything
**Answer: D** — Composition is sequence reuse.

---

## Question 7: Recursive vs Iterative Functions
Computing factorial: recursion is elegant, but iterative is often safer. For AI, why prefer iteration?
- D. Iteration avoids stack overflow on large inputs (deep recursion uses stack space); AI trains on huge datasets (factorial of 1M would crash recursion, but iteration handles it)—iteration is the safer bet for production code- B. Recursion is more efficient- C. Recursion is always better- A. The choice doesn't matter
**Answer: D** — Iteration scales; deep recursion crashes.

---

## Question 8: Type Hints as Documentation
Compare: `def train(model, data)` vs `def train(model: Model, data: Dataset) -> Dict[str, float]`. What does the second accomplish?
- B. Type hints document expected input/output types, enable IDE autocompletion and type checking (mypy), and make code self-documenting—future developers know immediately what types are needed- A. Hints slow down execution- C. Type hints are optional in Python- D. Hints don't help
**Answer: B** — Type hints are executable documentation.

---

## Question 9: Function Testing Example
You write `calculate_accuracy(predictions, labels)`. How would you design test cases to cover edge cases?
- D. Test: empty lists (edge case), all correct (100%), all wrong (0%), mixed results, class imbalance cases—edge cases expose bugs that normal cases miss; comprehensive testing catches edge failures- C. One test case is enough- A. Edge cases aren't important- B. Testing is optional
**Answer: D** — Edge case testing finds hidden bugs.

---

## Question 10: Performance-Critical Function
A function is called 1 million times per training step. It's currently slow. How would you optimize without sacrificing clarity?
- C. Profile first (`cProfile`) to find the bottleneck, then optimize that specific part; avoid premature optimization—90% of optimization effort goes to 10% of the code; targeted optimization is smart- D. Optimize everything speculatively- B. Optimization always hurts readability- A. Profiles are overkill
**Answer: C** — Profiling enables targeted optimization.
