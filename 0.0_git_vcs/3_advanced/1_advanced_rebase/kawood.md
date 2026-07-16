# Kawood Mastery Challenge — Advanced Rebase

Master interactive rebase to craft beautiful, understandable commit histories that future developers will appreciate.

## Question 1: Rebase vs Merge Philosophy
Explain the core philosophical difference: merging preserves "what happened" (history stays messy), while rebasing rewrites "what should have been" (history becomes clean). When is each appropriate?
- A. Merge for shared branches (preserves reality); rebase for local branches (cleans up before sharing)—mixing them on shared branches rewrites public history, causing chaos- B. Always rebase- D. Always merge- C. The choice doesn't matter
**Answer: A** — Rebasing is a local craft; merging is shared reality.

---

## Question 2: Interactive Rebase (-i) Capabilities
What can `git rebase -i` do beyond just moving commits? List three operations.
- A. Reorder commits, squash multiple commits into one, edit commit messages, drop commits entirely, split large commits—these transform messy history into clarity- D. Interactive rebase only moves commits- B. Interactive rebase is dangerous and should never be used- C. These operations aren't possible in git
**Answer: A** — Interactive rebase is history sculpting.

---

## Question 3: Squashing Commits (Cleanup Before Main)
You have 8 commits on your feature branch, but they're really just one feature with false starts and corrections. Should you squash them into one commit before merging to main? What's the trade-off?
- C. Yes—squashing before merge makes the feature appear as one logical unit, simplifying history; the trade-off is losing the false-start commits (acceptable for local history, problematic if others depend on them)- D. Never squash; preserve all commits- A. Squashing loses information permanently- B. Squashing doesn't change anything
**Answer: C** — Squashing is cleanup; timing matters.

---

## Question 4: Rebase Onto a Moving Target
You started `feature-new-loss` three weeks ago from main. Main has 50 new commits since then. You want to rebase your branch onto the latest main. What happens, and why is this different from merging?
- D. `git rebase main` replays your commits on top of the new main—this moves your work forward in time and prevents merge conflicts later; merging would create a merge commit instead- B. Rebase and merge do the same thing- A. Rebasing is impossible- C. Rebasing breaks everything
**Answer: D** — Rebasing is time travel; merging is preservation.

---

## Question 5: Conflict Resolution During Rebase
Rebasing encounters a conflict in the first of ten commits. You resolve it, but then the third commit has the same conflict again. What's happening, and should you abort or continue?
- D. Each commit in a rebase is independent; conflicts repeat when commits touch the same code—you'll resolve the same conflict multiple times if you're rebasing many commits; continue if you understand why, abort if it's a sign of bad design- A. Rebase automatically resolves all conflicts- B. Multiple conflicts mean rebase failed- C. This never happens in practice
**Answer: D** — Rebasing can surface repeated conflicts; they're informative.

---

## Question 6: Golden Rule of Rebase
Your team's rule: "Never rebase commits that have been pushed to a shared remote." Why is this rule sacred?
- A. Rewriting shared history breaks teammates' local copies—when they pull, git sees conflicting histories; they must manually rebuild their branches—rebase is fine for unpushed commits, destructive for shared ones- C. This rule is unnecessary- B. Rebasing shared commits is always fine- D. Only experienced developers should break this rule
**Answer: A** — The golden rule prevents history warfare.

---

## Question 7: Autosquash for Intelligent Cleanup
You have commits with messages like "Fix typo in model.py" and "Add test for new function" that are really corrections to earlier commits. `git rebase -i --autosquash` can reorganize these automatically. How does this save time?
- D. You mark cleanup commits with `fixup!` prefix; autosquash moves them next to the commits they fix and squashes automatically—this is faster than manual reordering in interactive rebase- C. Autosquash doesn't exist- A. Manual reordering is always better- B. Autosquash is just a gimmick
**Answer: D** — Autosquash is intelligent automation for a common pattern.

---

## Question 8: Rebase as Education
A junior developer makes a messy feature branch: 25 commits with titles like "WIP", "fix", "oops", "working version." Before merging, you show them `git rebase -i main` to clean it up. What skill are you teaching?
- A. You're teaching that commit quality matters for team readability; cleanup discipline shows respect for future maintainers—this becomes a career-building habit- B. Rebasing is pointless nitpicking- D. Messy commits are fine- C. This teaches nothing useful
**Answer: A** — Rebase discipline is a proxy for professionalism.

---

## Question 9: Rebase Abort and Recovery
You're 7 commits into an interactive rebase and realize you made a mistake in conflict resolution. What's the escape hatch?
- C. `git rebase --abort` cancels the entire rebase and restores your branch to where it started—this is your safety net for rebase mistakes- B. You're stuck; rebase can't be undone- A. Manual fix is required- D. Abort doesn't exist
**Answer: C** — Abort is your escape route; use it freely.

---

## Question 10: Rebasing Entire Feature for Main PR
Before merging your `feature-model-serving` branch to main, you run `git rebase -i main` to squash 12 commits into 3 logical chunks with clear messages. What is the outcome of this discipline?
- C. A clean PR history that reviewers can understand at a glance; future developers using `git log` see the feature as three conceptual units, not twelve confusing iterations—this is respect for the codebase- D. This wastes time- A. Commits should never be reorganized- B. Clean history is irrelevant to code quality
**Answer: C** — History is communication; rebase enables it.
