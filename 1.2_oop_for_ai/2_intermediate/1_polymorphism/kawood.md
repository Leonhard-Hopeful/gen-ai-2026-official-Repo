# Kawood Mastery Challenge — Polymorphism

Master polymorphism to write flexible code that works with many object types without modification.

## Question 1: Polymorphism Definition
What does "polymorphism" mean? (Many forms)
- B. Polymorphism enables one interface to work with multiple types—same method call produces different behavior depending on object type—in AI, this enables training code to work with NeuralNetwork or DecisionTree identically- A. Polymorphism is inheritance- D. Polymorphism is overloading- C. Polymorphism isn't used in Python
**Answer: B** — Polymorphism is flexible interfaces.

---

## Question 2: Polymorphic Method Override
```python
class Animal:
    def speak(self): return "sound"

class Dog(Animal):
    def speak(self): return "woof"

class Cat(Animal):
    def speak(self): return "meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```
What prints?
- B. woof, meow—each object's speak() is called; Dog returns "woof", Cat returns "meow"—same method call, different behavior—this is polymorphism in action- C. sound, sound- A. woof, woof- D. Error
**Answer: B** — Same method, different behavior per type.

---

## Question 3: Duck Typing
Python practice: if it walks like a duck and quacks like a duck, it's a duck. For code: if an object has train() and evaluate() methods, treat it like a Model. What's the advantage?
- A. You don't need inheritance or explicit interfaces—if the object has required methods, it works—this is "duck typing" and enables flexibility; you can retrofit new classes without modifying original code- D. You must inherit from Model- C. Type checking is required- B. Duck typing is fragile
**Answer: A** — Duck typing enables flexible polymorphism.

---

## Question 4: Operator Overloading
```python
class Vector:
    def __add__(self, other): return Vector(...)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
```
This uses polymorphism. How?
- A. __add__ overloads the + operator; v1 + v2 calls v1.__add__(v2)—operators can be overloaded for custom types—this makes Vector addition feel natural, like math- C. Operator overloading is cheating- B. Operators are fixed- D. + doesn't work on custom types
**Answer: A** — __add__ enables operator polymorphism.

---

## Question 5: Polymorphic Collections
```python
models = [NeuralNetwork(), DecisionTree(), SVMModel()]
for model in models:
    model.train(data)
```
This code trains different model types uniformly. Why is this polymorphism?
- A. Same method call (train) on different types; each executes its own train()—without polymorphism, you'd need if-checks for each type; polymorphism handles variety transparently- B. This isn't polymorphism- D. Collections can't be polymorphic- C. You need explicit type checks
**Answer: A** — Collections of different types, same interface.

---

## Question 6: Abstract Base Classes Enforce Interface
```python
from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def train(self): pass
```
Why enforce an interface?
- D. Abstract base classes guarantee subclasses implement required methods; this enforces polymorphism contracts—ensures all Models have train(), preventing missing-method errors at runtime- B. Abstract classes are optional- C. Enforcement happens automatically- A. Interfaces aren't enforced in Python
**Answer: D** — ABC enforcement ensures polymorphic safety.

---

## Question 7: Polymorphism in Neural Networks
A trainer object has: `fit(model, data)`. It works with different model types without modification. What makes this possible?
- B. Polymorphism—fit() calls model.train(), model.evaluate(), etc; as long as the model has these methods, it works—the trainer doesn't need to know the exact model type- D. Fit needs to check model type- A. Separate trainers for each model- C. Polymorphism doesn't apply
**Answer: B** — Generic code via polymorphism.

---

## Question 8: Runtime Type Checking
```python
if isinstance(obj, NeuralNetwork):
    obj.special_method()
elif isinstance(obj, DecisionTree):
    obj.other_method()
```
Is this good polymorphism?
- B. No—this is type checking (anti-polymorphism); good polymorphism avoids checks—if you need type checks, design failed; instead, put special_method() and other_method() in common interface- D. Type checks are essential- C. Polymorphism requires type checks- A. This is the only way
**Answer: B** — Type checks indicate polymorphism failure.

---

## Question 9: Liskov Substitution Principle (LSP)
Child class should be substitutable for parent without breaking code. If Model has train(data), LLMModel shouldn't change signature to train(data, config). Why?
- B. LSP ensures polymorphism works—if callers expect train(data), LLMModel must accept that—violating LSP breaks polymorphic assumptions; code using "Model" breaks on subclasses- D. Signature changes don't matter- C. Subclasses can change anything- A. LSP is just theory
**Answer: B** — LSP is polymorphism contract.

---

## Question 10: Polymorphism Benefits in Machine Learning
Your system trains 10 model types. With polymorphism, training code is simple. Without it, what's the cost?
- C. Without polymorphism, you'd have 10 separate training loops (one per model type) or massive if-elif chains; polymorphism enables one loop to handle all types—saves code, enables easy extension (add model 11, training works immediately)- B. Polymorphism has no advantages- A. Without polymorphism code is simpler- D. Code complexity doesn't scale with model count
**Answer: C** — Polymorphism enables code reuse across types.
