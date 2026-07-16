# Kawood Mastery Challenge — Basic Statistics

Master distributions, variance, and hypothesis testing to reason about uncertainty in AI.

## Question 1: Mean, Median, Mode
Your training data has values: [1, 2, 2, 3, 100] (outlier). Compare mean, median, mode.
- C. Mean = (1+2+2+3+100)/5 = 21.6 (skewed by outlier), Median = 2 (middle value, robust), Mode = 2 (most frequent)—median is robust to outliers; mean is sensitive—choosing the right statistic depends on your data distribution- A. All three are identical- D. Mean is always best- B. Statistics don't matter
**Answer: C** — Different statistics suit different scenarios.

---

## Question 2: Variance and Standard Deviation
Data: [1, 2, 3, 4, 5]. Why is standard deviation more interpretable than variance?
- D. Variance = 2, Std Dev = √2 ≈ 1.41—std dev is in the same units as data (easier interpretation); variance is harder to interpret; both measure spread, but std dev is more intuitive- C. They're equivalent- B. Variance is more interpretable- A. Units don't matter
**Answer: D** — Std dev is units-friendly.

---

## Question 3: Normal Distribution
Model outputs follow a normal (Gaussian) distribution. Why is this important?
- C. Normal distributions have nice properties (symmetry, well-understood tails)—many phenomena are approximately normal; it's the default assumption in statistics—if data isn't normal, transformations can help; many statistical tests assume normality- A. Most data is non-normal- D. Distribution doesn't matter- B. Only toy examples use normal
**Answer: C** — Normal distribution is fundamental in stats.

---

## Question 4: Skewness and Kurtosis
Data with positive skew (long tail right) vs negative skew (long tail left). How does this affect model training?
- B. Skewed data can mislead algorithms—they assume features are balanced; skew can cause bias toward one side; preprocessing (log transform, normalization) helps; understanding skew prevents surprises- C. Skew doesn't matter- D. Skew is just academic- A. All data is symmetric
**Answer: B** — Skewness affects model behavior.

---

## Question 5: Confidence Intervals
Your model achieves 95% accuracy on a test set of 100 samples. Is 95% the true accuracy?
- B. No—95% is a point estimate; true accuracy has uncertainty; confidence intervals quantify this (e.g., 92-98% with 95% confidence)—larger samples narrow intervals; understanding uncertainty prevents overconfidence- A. 95% is exact- C. Uncertainty is immeasurable- D. Confidence intervals aren't practical
**Answer: B** — Point estimates hide uncertainty.

---

## Question 6: Hypothesis Testing
You claim model A is better than model B. How do you test this statistically (not just compare accuracies)?
- D. Perform t-test or similar: define null hypothesis (no difference), compute p-value (probability of observing data if null were true); if p < 0.05, reject null (A is likely better)—this prevents false positives from random variance- C. Compare point estimates- B. Statistical testing isn't rigorous- A. Intuition is enough
**Answer: D** — Hypothesis testing quantifies evidence rigorously.

---

## Question 7: Correlation vs Causation
Two variables correlate: high social media use correlates with depression. Does this prove social media causes depression?
- D. No—correlation doesn't imply causation; common cause (stress causes both), reverse causation (depression drives usage), or confounding can explain correlation—in AI, correlation drives predictions, but causation is needed for intervention- B. Correlation equals causation- A. This distinction doesn't matter- C. Correlation is proof
**Answer: D** — Correlation is necessary but not sufficient.

---

## Question 8: Bayes' Theorem in Practice
A test for disease has 95% accuracy. You test positive. What's your actual disease probability?
- C. Not 95%—depends on disease prevalence (base rate); if disease is rare (1%), even a 95%-accurate test gives ~16% probability of having disease—base rates are critical; Bayes' theorem combines prior (prevalence) with likelihood (test accuracy)- D. Exactly 95%- B. Base rates don't matter- A. Bayes' theorem is theoretical
**Answer: C** — Bayes factors in base rates.

---

## Question 9: Type I and Type II Errors
In medical testing: Type I (false positive, test says sick when healthy) vs Type II (false negative, test says healthy when sick). Which is worse?
- C. Depends on context—Type II misses disease (dangerous health outcome); Type I causes unnecessary worry/treatment (less immediately dangerous)—medical contexts prioritize Type II reduction; different contexts balance these errors differently- B. Type I is always worse- D. Type II is always worse- A. Errors are equivalent
**Answer: C** — Context determines error importance.

---

## Question 10: Data Exploration with Statistics
Before building a model, what statistics would you examine?
- B. Mean, std dev, quantiles, skewness, outliers, correlations—these exploratory stats reveal data shape, anomalies, and relationships; understanding data distribution informs preprocessing and model choice- C. Just load and train- D. Statistics are overcomplicating- A. Data exploration isn't necessary
**Answer: B** — EDA with statistics prevents model mistakes.
