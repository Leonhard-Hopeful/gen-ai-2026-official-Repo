# Model Architecture

## Overview

Design AI model classes that encapsulate data flow, training loops, and evaluation in a clean, maintainable package.

## Why this matters

This lesson explains a key concept and connects it to real AI course design and student success.

## Key concepts

- Model interfaces
- Training loops
- Prediction APIs
- Separation of concerns

## Example

```python
class NeuralModel:
    def train(self, data): ...
```

## Tutor guide

Use this section to keep the lesson interactive and clear:

- Explain the concept with a simple analogy.
- Demonstrate code live and ask students to predict the result.
- Ask learners to make one small modification.
- Pause for questions and reinforce the main idea.

### Tutor workflow

1. Introduce the concept in 2-3 minutes.
2. Open the lesson markdown and read the overview together.
3. Run the example live or in the notebook.
4. Encourage learners to write the same example with their own data.
5. End with the review questions and connect to the next topic.

## Reflection questions

- What should a model class own?
- Why separate training and prediction?
