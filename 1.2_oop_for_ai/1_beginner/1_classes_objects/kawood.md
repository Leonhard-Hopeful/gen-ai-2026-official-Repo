# Kawood Mastery Challenge — Classes and Objects

Meet the building block of object-oriented programming: classes define structure and objects bring them to life.

## Question 1: Class vs Instance
What's the difference between a class and an object (instance)? Give an example from AI.
- B. Class is the blueprint (Model class defines structure); instance is a concrete realization (model_v1 = Model(...))—classes are abstract templates; instances are actual objects with real data- C. They're the same thing- A. Classes are for small projects- D. Instances are templates
**Answer: B** — Classes are templates; instances are concrete.

---

## Question 2: The __init__ Constructor
Why does `class Student: def __init__(self, name): self.name = name` exist, and what happens if you don't define it?
- D. __init__ initializes instance attributes when you create an object; without it, default __init__ does nothing—you'd create objects but have no way to set initial state, making objects useless- B. __init__ is optional- C. Python creates __init__ automatically- A. __init__ is only for large classes
**Answer: D** — __init__ sets up new instances with initial state.

---

## Question 3: The self Parameter
Every method has `self` as the first parameter. What is self?
- C. self is the instance itself—when you call `student.introduce()`, Python passes `student` as self automatically; methods need self to access or modify instance attributes- B. self is just a naming convention- A. self is a global variable- D. Methods don't need self
**Answer: C** — self is the instance reference inside methods.

---

## Question 4: Instance vs Class Attributes
```python
class Dog:
    species = "Canis familiaris"  # class attribute
    def __init__(self, name):
        self.name = name  # instance attribute
```
If two dogs exist, do they share species? Do they share name?
- C. Both share species (defined in class, shared by all instances); each has its own name (defined in __init__ per instance)—class attributes are shared, instance attributes are individual- A. They share both- D. They share neither- B. There's no difference
**Answer: C** — Class attributes are shared; instance attributes are individual.

---

## Question 5: Methods and Behavior
```python
class NeuralNetwork:
    def forward(self, x): ...
    def backward(self, loss): ...
```
Why encapsulate behavior in a class rather than standalone functions?
- C. Methods bind behavior to data—forward() and backward() operate on the network's weights (self); this encapsulation prevents passing the network everywhere; it's data + methods together- B. Classes don't provide benefits- D. Functions and classes are equivalent- A. Classes are just style
**Answer: C** — Methods bind behavior to the object's state.

---

## Question 6: Privacy with Underscore
You write `self._internal = value` with an underscore. Later, someone accesses it directly: `obj._internal`. Is this a problem?
- D. Python doesn't enforce privacy; underscore is a convention meaning "internal, don't rely on this"—it's not a protection, but a communication signal—if the internal changes, users were warned- A. Underscore prevents access- B. Python enforces privacy- C. Privacy conventions don't matter
**Answer: D** — Underscore signals intent, not enforcement.

---

## Question 7: Object State Persistence
You train a model and save the weights to an object: `model.weights = weights_array`. Will the weights survive if you close Python?
- A. No—object state exists only in memory; closing Python erases it—to persist, you must save to disk (pickle, h5, safetensors); loading recreates the object from disk- D. State is automatically saved- C. Weights persist indefinitely- B. You must manually back up state
**Answer: A** — Object state is ephemeral unless explicitly persisted.

---

## Question 8: Object Comparison
Two Model objects with identical weights: `model1 = Model(weights); model2 = Model(weights)`. Are they equal if compared with `==`?
- B. By default, no—Python compares object identity (are they the same object in memory?), not content; to compare content, implement `__eq__()` method—this gives classes control over equality semantics- A. They're always equal- D. Comparison is impossible- C. You must check attributes manually
**Answer: B** — Equality is defined by __eq__; default is identity.

---

## Question 9: Object Deletion and Cleanup
Do you need to explicitly delete objects (`del obj`), or does Python handle it?
- B. Python's garbage collector handles deletion automatically when no references remain; explicit `del` removes the reference and may trigger garbage collection—usually you don't need to delete explicitly unless managing resource limits- A. You must delete every object- C. Deletion is optional- D. Python never deletes objects
**Answer: B** — Garbage collection is mostly automatic.

---

## Question 10: Designing a Class Hierarchy
You're building an ML system with Model, NeuralNetwork, and DecisionTree classes. All have train() and evaluate() methods. Should they share code?
- B. Yes—create a base Model class with train() and evaluate(); NeuralNetwork and DecisionTree inherit and specialize—this is inheritance, discussed next; shared methods prevent duplication- C. Duplicate the methods in each class- A. Use separate files- D. Class relationships don't matter
**Answer: B** — Shared behavior suggests inheritance.
