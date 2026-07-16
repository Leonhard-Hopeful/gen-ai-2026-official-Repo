# Kawood Mastery Challenge — Attributes and Methods

Master instance and class attributes, properties, and methods to design flexible, maintainable classes.

## Question 1: Mutable Default Attributes
```python
class Dataset:
    def __init__(self, items=[]):
        self.items = items  # dangerous!
```
Create two datasets without providing items. Both share the same list (classic gotcha). How do you fix it?
- B. Use None as default: `def __init__(self, items=None): self.items = items or []`—creates a new list per instance instead of sharing one mutable default- C. The original code is fine- D. Use a tuple instead- A. This is unsolvable
**Answer: B** — None + creation is the pattern for mutable defaults.

---

## Question 2: Properties vs Direct Access
Compare: `obj.weight` (direct access) vs `obj.get_weight()` (method). With properties, you can have the elegance of access with method flexibility. How?
- A. Use @property decorator: `@property def weight(self): return self._weight`—looks like access but runs code, enabling validation, caching, or lazy computation- B. Properties don't exist- D. Direct access is always better- C. Methods and properties are identical
**Answer: A** — Properties blend access syntax with method power.

---

## Question 3: Validation in __init__
Your Model class takes learning rate. Should you validate in __init__ (reject invalid rates immediately) or later (validate before training)?
- D. Validate in __init__—fail fast; invalid state from construction is a programming error that should crash immediately; discovering bad state later wastes computation- B. Validate later during training- A. Don't validate- C. Both approaches are equivalent
**Answer: D** — Fail fast prevents garbage in, garbage out.

---

## Question 4: Lazy Initialization
Computing `self.expensive_property` is slow. Only compute when accessed, not on object creation. How?
- D. Use @property with caching: `@property def expensive_property(self): if not hasattr(self, "_cache"): self._cache = compute_expensive(); return self._cache`—compute once on first access, reuse- C. Always compute in __init__- A. Never cache- B. This pattern is overcomplicating
**Answer: D** — Lazy initialization defers expensive work until needed.

---

## Question 5: Method Chaining
Your class has methods: `load_data()`, `preprocess()`, `train()`. Design them to enable chaining: `obj.load_data().preprocess().train()`. How?
- B. Each method returns `self`—allows calling the next method on the return value—this is fluent API design, enabling readable pipelines- D. Methods should return results- C. Chaining is unpythonic- A. Chain with separate statements only
**Answer: B** — Returning self enables method chaining.

---

## Question 6: Class Methods vs Instance Methods
When would you use `@classmethod` instead of a regular instance method?
- C. Class methods operate on class data (not instances): `@classmethod def from_checkpoint(cls, path): return cls(torch.load(path))`—this creates an instance from a checkpoint; constructors (alternative constructors) are common class method uses- A. Class methods are always worse- D. Instance methods do everything- B. The decorators are cosmetic
**Answer: C** — Class methods are alternative constructors and factories.

---

## Question 7: Static Methods
When would you use `@staticmethod`?
- C. Static methods don't access instance or class state—pure utility functions: `@staticmethod def normalize(x): return (x - mean) / std`—these are helpers that logically belong to the class but don't need instance data- A. Static methods are useless- B. Always use regular methods- D. Static methods are just functions
**Answer: C** — Static methods are logical namespace organization.

---

## Question 8: Attribute Initialization Strategies
You're creating a complex model with many optional attributes. Initialize all in __init__ (even to None) or create them dynamically as needed?
- A. Initialize all in __init__—this makes the class schema explicit and prevents AttributeErrors on access; readers immediately see all possible attributes- C. Create dynamically- B. Never initialize attributes- D. Both approaches are equivalent
**Answer: A** — Explicit initialization documents the class schema.

---

## Question 9: Read-Only Attributes
You want `model.version` to be readable but not modifiable. How?
- D. Use @property with no setter: `@property def version(self): return self._version`—provides read-only access; attempting assignment raises AttributeError- C. Use regular attributes- A. Set manually with `__setattr__`- B. Read-only is impossible
**Answer: D** — Property without setter creates read-only attributes.

---

## Question 10: Attribute Access Introspection
You want to print all attributes of an object for debugging. How?
- D. Use `vars(obj)` or `obj.__dict__`—returns the instance's attributes as a dictionary—useful for debugging and serialization- B. Manually print each attribute- A. Use `dir(obj)` (includes methods too)- C. Introspection isn't possible
**Answer: D** — __dict__ is the instance attribute dictionary.
