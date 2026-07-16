# Kawood Mastery Challenge — Branching and Merging

Master the mechanics of Git branches to execute complex team workflows flawlessly.

## Question 1: Fast-Forward vs Merge Commits
When you merge a feature branch back to main, Git offers two strategies: fast-forward (no commit created) vs merge commit (creates a commit). When should you enforce merge commits, and why?
- C. Enforce merge commits to preserve explicit history of feature introduction; fast-forward loses this record—critical for auditing which feature caused issues and reverting features cleanly- D. Fast-forward is always better- B. Merge commits are always better- A. The choice doesn't matter
**Answer: C** — Explicit history is traceable; implicit history is erasable.

---

## Question 2: Three-Way Merge Under the Hood
You merge `feature-branch` into main. Git reports a conflict. Explain what "three-way merge" means and why Git needs three commits to decide.
- A. Git compares three versions: the common ancestor (what both started from), feature-branch changes (what was added), and main changes (competing work)—conflicts exist where both sides modified the same lines differently- D. Three-way means it uses three computers- B. Three-way is just a marketing term- C. Git only needs two commits
**Answer: A** — Understanding three-way merge demystifies conflict reports.

---

## Question 3: Keeping Branches Small and Focused
Your branch started with one objective: "Add dropout to the model." Halfway through, you add batch normalization, fix an unrelated bug, and refactor the config parser. What's wrong with this approach?
- A. Multiple objectives make code review harder, testing unclear, and reverting impossible—if one change breaks production, you can't revert just that change without losing the others; focus keeps branches reviewable- C. More features in one branch is faster- D. Large, messy branches are good for practice- B. Objectives don't matter; just code
**Answer: A** — Branching discipline is debugging discipline.

---

## Question 4: Merge Order and Dependencies
Your team has branches: `feature-a`, `feature-b` (depends on `feature-a`), and `feature-c` (independent). In what order should you merge, and why does order matter?
- A. Merge `feature-a` first (it's a dependency), then `feature-b`, then `feature-c`—correct order prevents dependency errors and simplifies conflict resolution- B. Order doesn't matter- D. Merge all at once- C. Merge randomly
**Answer: A** — Dependency management is topological sorting in your development DAG.

---

## Question 5: Conflict Markers Anatomy
Your file has:
```
<<<<<<< HEAD
learning_rate = 0.001
=======
learning_rate = 0.0001
>>>>>>> feature/lr-tuning
```
Explain what each section represents and why making the decision is the developer's job, not Git's.
- D. HEAD is main's version, feature/lr-tuning is the feature's version; Git shows both because it can't know which is correct—that's domain knowledge only a human has- B. Git should automatically pick one- A. The sections don't mean anything- C. This is a fatal error
**Answer: D** — Conflicts surface exactly where human judgment is required.

---

## Question 6: Merge Conflict Prevention (Preemption)
Rather than waiting for conflicts, how can teams prevent them structurally?
- A. Divide work by file or subsystem (don't have two people modifying the same file simultaneously); communicate via PRs before starting; rebase feature branches onto main daily to catch conflicts early- D. Conflicts are inevitable; no prevention possible- B. Have one person do all merging- C. Don't use branches
**Answer: A** — Prevention is cheaper than resolution.

---

## Question 7: Reverting a Merged Feature
You merged a feature that was supposed to improve inference speed but actually made it 30% slower. How do you revert the feature, and what's the difference between `git revert` and `git reset`?
- B. Use `git revert <merge-commit>` to create a new commit that undoes the merge—this preserves history and is safe for shared branches; `git reset` rewrites history and is dangerous for public branches- C. Use `git reset` on the remote- A. Manually undo all changes by hand- D. The feature is permanently stuck in main
**Answer: B** — Revert vs reset is the difference between "undo" and "pretend it never happened."

---

## Question 8: Cherry-Pick: When and Why?
You have a fix on `bugfix/inference-timeout` that needs to go into both main AND the current production release branch. Merging main into production is too risky. What's the solution?
- A. Use `git cherry-pick <commit-hash>` to apply just that commit to production; cherry-pick copies a commit without merging entire branches- C. Manually copy the code by hand- B. Create a new branch from scratch- D. Cherry-pick is not a real git command
**Answer: A** — Cherry-pick is selective merging for surgical deployments.

---

## Question 9: Merge Strategy for AI Experiments
Your team runs three model architecture experiments in parallel on three branches. All must eventually merge into a "research-summary" branch for comparison. Each branch has 50+ commits. What's the best merge strategy?
- A. Merge each branch separately into research-summary with explicit merge commits, preserving each branch's commit history—this maintains clarity about which commits belong to which experiment- B. Squash all commits into one per branch- D. Rebase everything into a flat line- C. Merge all at once with no merge commits
**Answer: A** — Preserving experiment branches as distinct lines of history aids analysis.

---

## Question 10: Handling Broken Main (Emergency)
Merged code broke the build. Main no longer compiles. What immediate actions protect the team?
- D. Revert the breaking commit (`git revert <commit>`), restore main to working state immediately, then investigate the issue in a feature branch—fast reversion minimizes disruption- A. Keep main broken while debugging- B. Blame the developer- C. This can't happen if everyone tests first
**Answer: D** — Fast reversion is incident response; slow recovery wastes team time.
