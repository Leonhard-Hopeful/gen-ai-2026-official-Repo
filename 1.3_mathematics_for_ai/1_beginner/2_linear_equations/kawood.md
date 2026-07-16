# Kawood Mastery Challenge — Linear Equations

Master systems of linear equations to understand linear transformations that power neural networks.

## Question 1: Linear Equation Definition
What makes an equation "linear"? (e.g., 2x + 3y = 7 vs x² + y = 1)
- D. Linear equations have variables to the first power only—no exponents, no products of variables; linear means straight-line solutions in 2D, hyperplane in higher dimensions- A. Equations with many terms are linear- C. Linearity is arbitrary- B. All equations are linear
**Answer: D** — Linear means first power, first degree.

---

## Question 2: System of Linear Equations
You have two equations: x + y = 5, 2x - y = 4. Solve to find x and y.
- B. From first: y = 5 - x. Substitute into second: 2x - (5 - x) = 4 → 3x - 5 = 4 → x = 3, y = 2—solving systems is fundamental to linear algebra; neural networks solve similar systems at scale- C. Guess and check- A. Systems can't be solved- D. Only one equation is solvable
**Answer: B** — Substitution solves linear systems.

---

## Question 3: Unique vs No vs Infinite Solutions
When can a system of linear equations have zero solutions, exactly one, or infinite?
- A. One solution if lines intersect (independent equations); zero solutions if lines are parallel (contradictory); infinite if lines coincide (dependent)—this is the solution space geometry—understanding it is critical for understanding neural network expressivity- D. Only one solution exists always- B. Multiple solutions mean the system is wrong- C. Solutions don't depend on equations
**Answer: A** — Solution count reflects equation relationships.

---

## Question 4: Linear Transformations
A neural network layer applies y = Wx + b (W is weight matrix, b is bias). Why is this a linear transformation?
- D. It's affine (linear + offset); W scales and rotates vectors, b shifts—despite the bias, it's called linear in ML; matrix multiplication is the core linear operation that composes through layers- C. It's not linear; it's nonlinear- B. Linearity doesn't apply to networks- A. Linearity is just terminology
**Answer: D** — y = Wx + b is an affine transformation.

---

## Question 5: Solving Ax = b
You want to find x given matrix A and vector b. When is there a unique solution?
- A. When A is square and invertible (full rank)—then x = A⁻¹b; this is the fundamental operation: solving linear systems is inverting the transformation—it's central to neural network training and physics simulations- B. Always solvable- D. Solutions don't depend on A- C. Inverse always exists
**Answer: A** — A⁻¹ exists only if A is invertible.

---

## Question 6: Overdetermined Systems
You have 10 equations but only 3 unknowns (overdetermined). Is there always a solution?
- B. No—overdetermined systems have no exact solution usually; you find the best approximate solution (least squares regression)—this is exactly what neural networks do: minimize error over overdetermined systems- D. Always solvable exactly- C. Overdetermined means impossible- A. Extra equations are useless
**Answer: B** — Least squares finds best-fit solutions.

---

## Question 7: Matrix Rank and Solutions
Matrix A has full rank 3 (3×3 matrix). What does full rank guarantee about solutions to Ax = b?
- A. Full rank means A is invertible; each b has a unique x—rank determines solvability; rank 3 means 3 independent equations (full information); lower rank means some equations are redundant- C. Rank doesn't affect solutions- B. Full rank means infinite solutions- D. Solutions don't depend on rank
**Answer: A** — Rank determines solution uniqueness.

---

## Question 8: Gaussian Elimination
To solve a system, you can use Gaussian elimination (row operations to triangular form, then back-substitute). When would this fail?
- D. When you reach a row of zeros with nonzero right-hand side (0 = 3), indicating contradiction—Gaussian elimination reveals inconsistencies as it progresses; this is how computers detect unsolvable systems- B. Gaussian elimination always works- A. It can't fail- C. Failure doesn't happen in practice
**Answer: D** — Zero rows with nonzero RHS reveal contradictions.

---

## Question 9: Linear Equations in ML Contexts
In linear regression, you fit y = βx to data. This involves solving a linear system. Why is linear regression the foundation for understanding more complex methods?
- D. Linear regression demonstrates core concepts—fitting, optimization, generalization—applied to the simplest case; understanding why linear methods work enables understanding why nonlinear methods are needed- A. Linear regression is outdated- B. Complex methods don't build on linear regression- C. Foundations aren't important
**Answer: D** — Linear regression teaches fundamentals.

---

## Question 10: Rank Deficiency in Practice
Your neural network gets "rank deficiency" warnings during training (weight matrix loses full rank). What's the problem?
- B. Rank deficiency means some neurons become redundant (output doesn't depend on all weights)—the layer loses capacity; regularization or better initialization can fix this; it indicates the network isn't using all its parameters effectively- C. Rank deficiency is harmless- A. Networks always have full rank- D. Warnings are just noise
**Answer: B** — Rank deficiency reduces network capacity.
