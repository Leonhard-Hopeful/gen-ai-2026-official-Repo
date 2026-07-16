# Kawood Mastery Challenge — Inheritance

Master inheritance to share code, specialize behavior, and build flexible class hierarchies.

## Question 1: Inheritance Purpose
You have Model, NeuralNetwork, and DecisionTree classes. Each has train(), evaluate(), save(), load(). Should they inherit from a common base?
- D. Yes—create Model base class with train(), evaluate(), save(), load(); children inherit and customize—eliminates duplication, ensures consistent interface, enables polymorphism- C. Duplicate code in each class- B. Use separate files- A. Inheritance is overcomplicating
**Answer: D** — Inheritance eliminates duplication and enforces consistency.

---

## Question 2: super() Usage
Your NeuralNetwork overrides train() but needs to call the parent Model's train() first (for setup). How?
- C. Use `super().train()` inside NeuralNetwork.train()—super() calls the parent method, enabling extension before/after parent behavior- D. Call `Model.train(self)`- B. Copy parent code- A. Overriding means replacing entirely
**Answer: C** — super() enables extending parent behavior.

---

## Question 3: Abstract Base Classes
You want to define Model as a template that enforces train() and evaluate() in all subclasses. How?
- C. Use ABC (Abstract Base Class): `from abc import ABC, abstractmethod`; decorate methods with @abstractmethod; subclasses must implement them—prevents concrete Model instantiation, ensures children define required methods- D. Don't enforce; trust subclasses- A. Use a naming convention- B. ABC is overcomplicating
**Answer: C** — ABC enforces contracts on subclasses.

---

## Question 4: Multiple Inheritance Complexity
```python
class Trainer: def train(self): pass
class Evaluator: def evaluate(self): pass
class MLPipeline(Trainer, Evaluator): pass
```
MLPipeline gets train() and evaluate(). What problem arises if both parents have overlapping methods?
- D. Method resolution order (MRO) determines which parent's method is called; with multiple inheritance, MRO can be ambiguous—this is the "diamond problem"—best practice: avoid multiple inheritance, use composition instead- B. Multiple inheritance always works smoothly- A. The problem doesn't exist in Python- C. Both methods are called
**Answer: D** — Multiple inheritance creates ambiguity; prefer composition.

---

## Question 5: isinstance and Polymorphism
You have a list of models: `models = [NeuralNetwork(...), DecisionTree(...)]`. You iterate and call `model.train()` for each. Does it work?
- B. Yes—polymorphism means each model's own train() is called; NeuralNetwork.train() and DecisionTree.train() run their specific code—inheritance enables code working with the parent type to work with all children- C. Only the first model trains- D. All models call the same code- A. Polymorphism requires explicit type checking
**Answer: B** — Polymorphism is automatic method dispatch.

---

## Question 6: Inheritance Hierarchies in Practice
You're designing an AI platform. Is this hierarchy good? `AISystem -> Model -> NeuralNetwork -> RNN -> LSTM`. Each level adds specificity.
- B. This is reasonable for deep specialization—each level adds features; LSTM is an RNN is a NeuralNetwork is a Model—but prefer flat or shallow hierarchies; deep hierarchies become hard to understand and maintain- C. Deeper is always better- A. Flat is always better- D. Hierarchy doesn't matter
**Answer: B** — Balance specificity with complexity; avoid deep hierarchies.

---

## Question 7: Composition vs Inheritance
You have a Model that uses a DataLoader. Should DataLoader be a parent class (inheritance) or a contained object (composition)?
- B. Composition—Model contains a DataLoader; "Model IS-A DataLoader" doesn't make sense, but "Model HAS-A DataLoader" does—composition is more flexible and clearer; use inheritance for IS-A relationships- A. Always use inheritance- C. Composition is weaker- D. The choice doesn't matter
**Answer: B** — Composition models HAS-A relationships; inheritance models IS-A.

---

## Question 8: Method Override Contracts
A child class overrides a parent method. Should the signature (parameters, return type) match?
- C. Yes, or at minimum the return type should be compatible—changing signatures breaks substitutability (a child instance used as parent breaks)—strict typing helps; in Python this is convention, not enforced- B. Signatures can change freely- A. Override means replacing entirely- D. Contracts don't matter
**Answer: C** — Substitutability requires compatible signatures.

---

## Question 9: Constructor Chaining
Your child class needs to initialize parent attributes. How?
- B. Call `super().__init__(...)`  in child's __init__—initializes parent first, then child setup—ensures parent is properly initialized before child code runs- D. Duplicate parent init in child- A. Don't call parent init- C. Parent init happens automatically
**Answer: B** — super().__init__() chains initialization up.

---

## Question 10: Inheritance for Code Reuse vs Design
Is it better to inherit to reuse code (e.g., both classes use the same train_step method) or to use composition/mixins?
- D. Inheritance is fine for code reuse, but only if the IS-A relationship is genuine—forcing inheritance just for code reuse creates artificial hierarchies; consider composition or mixins if IS-A doesn't hold- A. Always inherit for reuse- B. Never inherit; only compose- C. Reuse method doesn't matter
**Answer: D** — Use inheritance when IS-A; composition otherwise.
