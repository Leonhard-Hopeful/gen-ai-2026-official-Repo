# Kawood Mastery Challenge — Dependency Management

Master version pinning and dependency resolution to build stable, reproducible systems.

## Question 1: Semantic Versioning in Dependencies
A package uses semantic versioning: 1.5.2 means major=1, minor=5, patch=2. In your requirements.txt, you write `package==1.5.2` vs `package>=1.5.2` vs `package~=1.5.2`. When use each?
- D. `==` for strict matching (production stability), `>=` for flexibility (allow security patches), `~=` for minor updates only (~=1.5.2 allows 1.5.x but not 1.6.0)—choose based on stability vs innovation trade-off- C. All notations are equivalent- B. Always use ==- A. Notations don't affect behavior
**Answer: D** — Version specifiers balance stability and updates.

---

## Question 2: Dependency Hell
You have: A requires B==1.0, C requires B==2.0. Installing both is impossible. How do projects solve this?
- D. Either accept incompatibility (work with whoever is more recent), or negotiate compatible versions (A updates to work with B 2.0)—this is the "dependency hell"; best practice: minimize dependencies and keep versions compatible- B. Dependency managers handle this automatically- C. This never happens- A. One dependency must be removed
**Answer: D** — Dependency conflicts require negotiation.

---

## Question 3: Transitive Dependencies
You install `tensorflow`, which internally depends on `numpy`. When you `pip freeze`, numpy is listed. Why is this important?
- C. Transitive dependencies (dependencies of dependencies) accumulate—you inherit stability issues from packages you didn't choose—understanding your full dependency tree prevents surprises when sub-dependencies break- A. Transitive dependencies are hidden- B. Only direct dependencies matter- D. Sub-dependencies don't cause problems
**Answer: C** — Transitive dependency tree is important.

---

## Question 4: Lock Files
Poetry generates a `poetry.lock` file that pins exact versions of all dependencies (including transitive). Why lock?
- B. Lock files enable reproducible installs—teammates and CI get identical versions; without lock, `pip install -r requirements.txt` might install different versions if packages updated—locks are deployment checkpoints- A. Lock files are unnecessary- C. Only major versions need locking- D. Locks prevent updates
**Answer: B** — Lock files freeze dependency state.

---

## Question 5: Updating Dependencies Safely
You want to update all packages to latest versions. What's the risk?
- D. Updates might introduce breaking changes; even minor bumps can break code—best practice: update one at a time, test thoroughly, keep notes of failures—batch updates are risky- B. Updates are always safe- A. All packages are backwards compatible- C. Updating is unnecessary
**Answer: D** — Batch updates are risky; roll incrementally.

---

## Question 6: Security Vulnerabilities
A package reports a critical security vulnerability. You must update. But the new version might break your code. What's the strategy?
- B. Update immediately if possible, test thoroughly—security patches take priority; if incompatible, temporarily pin the old version and plan a migration; delay risksexposure- D. Never update if it might break things- A. Security patches are optional- C. Stay with vulnerable versions
**Answer: B** — Security updates are urgent.

---

## Question 7: Dependency Optimization
You inherit a project with 200+ installed packages. Many seem unused. How do you clean?
- A. Audit usage (`pip-audit` or import analysis), remove unused packages, pin only necessary ones—bloat increases install time, attack surface, and maintenance burden; minimal dependencies are more stable- D. Keep all packages- B. Dependencies don't impact project- C. Unused packages don't matter
**Answer: A** — Minimize dependencies to reduce friction.

---

## Question 8: Pinned vs Unpinned Trade-off
Pinned version (1.5.2): stable, predictable, but misses security patches. Unpinned (>=1.5.0): gets updates, but might break. What's the right choice for production?
- C. Pin in production (stability); use unpinned in development (flexibility)—production should be stable and reproducible; development can be more fluid and updated- A. Always pin- D. Never pin- B. The choice doesn't affect stability
**Answer: C** — Production pins; development updates.

---

## Question 9: Dependency Documentation
Your `requirements.txt` has 50 packages. A new developer sees it and asks: "Why do we need sklearn AND tensorflow AND pytorch?" How should you respond?
- A. Document each dependency: create a `DEPENDENCIES.md` explaining what each package does and why it's necessary—this helps catch bloat and guides cleanup- B. "I don't know; they've always been there"- D. Dependencies explain themselves- C. Document is busywork
**Answer: A** — Dependency documentation justifies bloat.

---

## Question 10: Circular Dependencies (Rare)
Package A depends on B, B depends on C, C depends on A. This is circular and unresolvable. How do you detect and fix?
- C. Dependency trees reveal cycles—refactor to break cycles: extract shared code to D, have A and C import from D instead of each other—cycles indicate design issues; restructuring fixes them- A. Circular dependencies are impossible- B. They resolve automatically- D. Can't fix circular deps
**Answer: C** — Cycles reveal design issues requiring refactoring.
