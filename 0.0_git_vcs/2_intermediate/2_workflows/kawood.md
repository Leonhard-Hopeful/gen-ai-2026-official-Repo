# Kawood Mastery Challenge — Git Workflows for Teams

Master workflow patterns to organize large AI teams around shared code discipline.

## Question 1: Comparing Workflows (Feature Branch vs Trunk-Based)
Explain the core difference: Feature Branch Workflow (all work on separate branches) vs Trunk-Based Development (short-lived branches, quick merges to main). When does each excel?
- A. Feature branches isolate work longer (good for large features, code review); trunk-based enables rapid integration (good for CI/CD, fast feedback)—pick based on team size and feature scope- D. One is always better than the other- B. They're identical- C. Neither works in practice
**Answer: A** — Different scales and rhythms require different workflows.

---

## Question 2: Release Branch Purpose
After sprint 5, you create `release/v1.5` from main. What changes go into this branch vs main, and why this separation?
- D. Release branch gets only bug fixes and version bumps; main continues new feature development—this decouples stability from velocity, allowing teams to fix production while developing future versions- C. Both main and release branches get the same changes- B. Release branches are not used in real projects- A. Release branches are for backup only
**Answer: D** — Release branches decouple stability from progress.

---

## Question 3: Hotfix Flow
Production model crashed with data validation failing. You need to ship a fix immediately without waiting for the next planned release. Walk through the hotfix workflow.
- B. Create `hotfix/validation-crash` from production tag, fix the bug, test rigorously, merge into both main and release branch with a new tag, deploy to production—this ensures the fix reaches all code paths- C. Patch production manually- A. Wait for the next scheduled release- D. Hotfixes are not recommended
**Answer: B** — Hotfixes balance urgency with code integration.

---

## Question 4: Continuous Integration Discipline
Your team rule: "All commits to main must pass CI/CD within 15 minutes." How does this enforce good workflow practice?
- C. It forces small, testable commits (large commits take too long to test), discourages incomplete work (CI fails), and creates rapid feedback loops—developers learn within minutes if they broke something- B. CI/CD is optional busywork- A. Tests should be run manually after deployment- D. Time limits on builds don't matter
**Answer: C** — Tight feedback loops train developers toward quality reflexively.

---

## Question 5: Preventing Broken Main
You see a PR with 200 lines added, no tests. CI will pass anyway (insufficient coverage). Should you approve? Why does this decision affect team workflow for months?
- D. Don't approve—untested code will eventually break main, triggering firefighting; each broken main wastes 2-3 hours of team time; declining now prevents future chaos- B. Approve; tests are optional- A. Tests aren't your concern as a reviewer- C. Main being broken sometimes is normal
**Answer: D** — Standards enforcement prevents compounding disaster.

---

## Question 6: Parallel Feature Workflow
Three teams work on features A, B, and C simultaneously. A and B don't depend on each other; C depends on both. How do you coordinate merges to prevent C from merging before its dependencies?
- D. A and B merge into main independently; C creates feature branch from main after both A and B are merged—explicit dependency ordering prevents broken code- A. All three merge simultaneously- B. C merges first, then A and B- C. Linear merging; one at a time
**Answer: D** — Dependency management is workflow management.

---

## Question 7: Monorepo vs Multiple Repos Workflow
Your AI platform spans data pipeline (Python), API server (Go), and frontend (TypeScript). Should this be one repo or three? How does your answer affect team workflow?
- B. Monorepo keeps related changes atomic and reviews holistic; separate repos enable independent deployment—choose based on whether teams move together (monorepo) or independently (separate repos)- A. Always use monorepos- D. Always use separate repos- C. This choice doesn't affect workflow
**Answer: B** — Repo structure encodes team structure.

---

## Question 8: Code Review SLA in Workflow
Your team standard: "Reviews happen within 4 hours; PRs stale after 2 days." Why are these time limits part of workflow, not just suggestions?
- A. Timely reviews maintain momentum (developers stay focused); aging PRs accumulate conflicts and context loss—SLAs protect productivity rhythm- B. Time limits are micromanagement- D. Reviews should happen whenever someone feels like it- C. SLAs don't affect outcomes
**Answer: A** — Process SLAs are productivity infrastructure.

---

## Question 9: Dealing with Stale Branches
You notice 47 merged branches still hanging around on the remote. Some are 6 months old. Why does cleanup matter for team health?
- B. Clutter confuses new developers, wastes cognitive load, and makes the branch list unusable—regular cleanup (weekly) keeps the workspace navigable- C. Old branches should stay forever- A. Cleanup is busywork- D. Branch count doesn't affect anything
**Answer: B** — Hygiene is part of discipline.

---

## Question 10: Scaling Workflows as Teams Grow
Your AI team is growing from 5 to 25 people. The old workflow (everyone reviews everything) will break. What workflow adjustments maintain quality while scaling?
- D. Assign CODEOWNERS file; establish reviewing teams by subsystem; require minimum two reviews for main branches; use automate bots for style checks—this scales review without requiring all-hands code reading- C. Keep the old workflow; everyone stays involved- A. Abandon code review to save time- B. Workflows don't need to scale
**Answer: D** — Organizational structure should be encoded in your workflow rules.
