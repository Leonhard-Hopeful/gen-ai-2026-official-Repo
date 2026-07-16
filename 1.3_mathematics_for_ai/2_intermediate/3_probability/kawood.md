# Kawood Mastery Challenge — Probability

Master probability theory to reason about uncertainty and build robust probabilistic models.

## Question 1: Probability Space
A probability space has sample space S (all possible outcomes), events (subsets of S), and probabilities P. For a die roll: S = {1,2,3,4,5,6}, event "even" = {2,4,6}. What's P(even)?
- B. P(even) = 3/6 = 0.5—each outcome equally likely—probability is the sum over outcomes in the event; this extends to continuous spaces with probability densities- A. Probability is arbitrary- C. All events have equal probability- D. Probability space is too abstract
**Answer: B** — Probability assigns numbers to events.

---

## Question 2: Conditional Probability
P(A|B) = P(A and B) / P(B). You have a test for disease: P(positive|disease) = 0.95. If disease has 1% prevalence, what's P(disease|positive)?
- D. P(disease|positive) = 0.95 × 0.01 / [0.95 × 0.01 + 0.05 × 0.99] ≈ 0.16—Bayes' theorem—even if test is 95% accurate, disease is rare, so positive test is only ~16% likely to indicate disease- B. P(disease|positive) = 0.95- C. Conditional probability isn't useful- A. Base rates don't affect this
**Answer: D** — Bayes' theorem is conditional probability.

---

## Question 3: Independence
Events A and B are independent if P(A|B) = P(A). Why does independence simplify calculations?
- D. If A and B are independent, P(A and B) = P(A) × P(B)—independence simplifies joint probabilities from complex dependencies to products; many models assume independence (Naive Bayes) because it's tractable- C. Independence doesn't help- A. All events are independent- B. Independence is never true
**Answer: D** — Independence enables factorization.

---

## Question 4: Probability Distribution
A random variable X follows a distribution P(X). For continuous X (e.g., temperature), probability density p(x) is used. Why not point probabilities?
- C. Continuous variables have infinitely many values; P(X=23.5°C) = 0 exactly (measure zero)—density p(x) enables integration to find probabilities over ranges (P(20 < X < 30))—densities are the continuous analog of discrete probabilities- A. Point probabilities work for continuous- B. Continuous probability is impossible- D. Density and probability are identical
**Answer: C** — Density integrates to probability.

---

## Question 5: Expectation (Mean)
E[X] = Σ x × P(x) (discrete) or ∫ x × p(x) dx (continuous). What does expectation represent?
- D. Expectation is the average outcome if you repeat many times; it's the center of the distribution—used to summarize distributions; in machine learning, expected loss guides optimization- C. Expectation is just a formula- B. Expectation isn't practical- A. Distributions don't have expectations
**Answer: D** — Expectation is the long-run average.

---

## Question 6: Variance
Var(X) = E[(X - E[X])²]. What does this measure?
- A. Variance measures spread—how far X typically deviates from its mean—high variance means uncertain/spread-out; low variance means concentrated—used to measure model confidence and stability- B. Variance is identical to expectation- C. Variance doesn't summarize distributions- D. Spread is unmeasurable
**Answer: A** — Variance measures dispersion.

---

## Question 7: Joint Probability
You have two events: coin flip (H/T) and die roll (1-6). What's the joint space size?
- D. 2 × 6 = 12 outcomes—joint probability P(H, 3) requires specifying both outcomes; this grows exponentially with variables—high dimensionality is a challenge in probabilistic modeling- C. 2 + 6 = 8- B. Joint space is undefined- A. Product rule doesn't apply
**Answer: D** — Joint space is a Cartesian product.

---

## Question 8: Probability vs Likelihood
A model predicts probabilities. Likelihood is P(data | model parameters). Why distinguish?
- C. Probability P(X) treats X as random; likelihood L(θ|X) treats data as fixed and parameters as variables—in learning, you observe data and maximize likelihood to find best parameters; distinguishing clarifies what's random vs fixed- B. They're the same- A. Distinction doesn't matter- D. Likelihood is outdated
**Answer: C** — Probability: random variable; likelihood: parameter inference.

---

## Question 9: Maximum Likelihood Estimation (MLE)
Given observed data, you find parameters θ that maximize likelihood L(θ|data). Why is MLE popular?
- B. MLE is principled and computationally tractable; it finds parameters most consistent with data—used in most machine learning (regression, classification); no arbitrary choices unlike Bayesian methods- D. MLE is just one approach- A. MLE doesn't guarantee good parameters- C. ML always uses alternatives
**Answer: B** — MLE is the standard estimation principle.

---

## Question 10: Probabilistic Models
Why use probabilistic models (outputting distributions) rather than deterministic models (outputting points)?
- C. Probabilistic models quantify uncertainty—you don't just predict output, but also confidence; enables decision-making with risk (medicine: both accuracy and confidence matter); calibrated uncertainty is more useful than point predictions alone- D. Probabilistic models are always slower- A. Uncertainty isn't useful- B. Deterministic is always better
**Answer: C** — Probabilistic outputs quantify confidence.
