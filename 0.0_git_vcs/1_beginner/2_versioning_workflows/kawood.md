# Kawood Mastery Challenge — Versioning Workflows

Master branch strategy, feature isolation, and commit hygiene to lead AI teams confidently.

## Question 1: Why Branch Exists
What fundamental problem do branches solve in AI development, especially when multiple researchers experiment simultaneously?
- B. Branches isolate experimental changes, allowing teams to work in parallel without breaking each other's code—each researcher can have a stable working version while others iterate on unstable features- D. Branches are just for organizing folders- C. Branches are required by GitHub- A. Branches have no real purpose in AI development
**Answer: B** — Branches are the atomic unit of isolated work in modern software development.

---

## Question 2: Feature Branch Naming
Your team has a Git naming convention: `feature/model-optimization`, `bugfix/inference-timeout`, `experiment/attention-heads`. Why does naming matter, and what goes wrong with poor naming?
- A. Good names make history searchable and convey intent; poor names like `branch1` make it impossible to understand what work happened months later, complicating debugging- C. Naming doesn't matter; all branches are equivalent- B. Names should be as long as possible to include all details- D. Names should use random characters for security
**Answer: A** — Branch naming is metadata that future team members rely on to navigate history.

---

## Question 3: Commit Hygiene Under Pressure
You've been coding for 6 hours and have 47 uncommitted changes across 12 files. You're about to merge this work. What's the difference between good and bad commit organization, and how does it help when future bugs emerge?
- D. Group related changes into commits with clear messages; this enables `git bisect` to pinpoint which logical change introduced a bug, rather than reverting an enormous 6-hour blob- A. Commit everything at once with one message; it's faster- C. Don't commit; just push all files- B. Spread commits randomly across files
**Answer: D** — Good hygiene transforms debugging from archeology into precise science.

---

## Question 4: Meaningful Commit Messages
Compare these two messages: "fix stuff" vs "Fix model.evaluate() to handle empty datasets gracefully, preventing crashes in production data pipelines." When would each approach backfire?
- C. The first backfires when debugging 6 months later—you'll waste hours guessing what "stuff" meant; the second stays meaningful across time and helps other developers understand the change's impact- B. Both messages are equally good- D. The second is unnecessarily verbose- A. Commit messages don't matter
**Answer: C** — Commit messages are communication across time to your future self and your team.

---

## Question 5: Merge Strategies and History
Your team uses a strict policy: all feature branches must be merged with a commit (not fast-forward), preserving the fact that this feature existed. Why does this history preservation matter for AI projects tracking model evolution?
- B. It creates an explicit record of when features were introduced, making it easy to trace which commit brought a feature live and revert if needed—critical when reverting features affects model outputs or training pipelines- A. It's just busywork; fast-forward is always better- C. History doesn't matter; only current code matters- D. The policy doesn't affect anything
**Answer: B** — Explicit history is a debugging asset and audit trail for model lineage.

---

## Question 6: Branch Lifetime and Team Sync
A feature branch has existed for 3 weeks. The main branch has 50 new commits from other features. What problem might this create, and how often should branches be synced?
- D. Long-lived branches diverge significantly from main, making merges painful and hiding integration problems; rebase frequently (every few days) to catch conflicts early and keep work synchronized- B. Long-lived branches don't cause any problems- C. Branches should never be updated once created- A. Updates should only happen at the end before merge
**Answer: D** — Frequent syncing is prophylactic against merge disasters.

---

## Question 7: Isolation and Experimentation
In AI, you're testing three hypotheses about model architecture on three branches simultaneously. How does branch isolation protect the team from experiment failure?
- B. Each branch's experimental changes stay isolated; if one experiment crashes or produces bad results, main stays stable and other experiments unaffected—researchers can fail fast without destabilizing the pipeline- D. Branches don't provide isolation- C. All experiments must share the same code- A. Experiments should be done manually without version control
**Answer: B** — Isolation is the freedom to fail fast without dragging teammates down.

---

## Question 8: From Feature Branch to Main (Complete Workflow)
Walk through the complete workflow: you finish a feature on `feature/new-loss-function`, want to prepare it for merging. What steps ensure main never receives broken code?
- A. Test locally, verify `git status` is clean, create a pull request (PR) for review, address reviewer feedback, ensure CI/CD passes, then merge—this multi-stage gating prevents broken code from reaching main- B. Push immediately to main without review- C. Merge without testing- D. Ask colleagues to merge without reviewing code
**Answer: A** — Gating processes turn code review into safety infrastructure.

---

## Question 9: Cleaning Up After Merging
After merging `feature/model-evaluation` into main, the branch is no longer needed, but old branches clutter the remote. What command removes it, and what's the risk of keeping stale branches around?
- D. `git branch -d feature/model-evaluation` locally, then `git push origin --delete feature/model-evaluation` remotely; stale branches confuse new developers who waste time investigating dead code- B. Never delete branches; keep them forever- A. Branches delete automatically- C. Stale branches are good for documentation
**Answer: D** — Regular cleanup keeps the workspace navigable and team focus sharp.

---

## Question 10: Version Control as Documentation
A teammate new to the project asks, "How did we decide to structure this model training pipeline?" You run `git log --all --oneline --graph` and see the branching history. How does this history serve as documentation?
- B. Branch and commit history shows how the team arrived at current decisions—it documents which experiments were tried, why some were rejected, and how design evolved; this context is irreplaceable for onboarding- D. History is just noise; only the final code matters- C. You should write a separate document instead- A. History documents nothing useful
**Answer: B** — Version control history is executable documentation that's always in sync with code.
