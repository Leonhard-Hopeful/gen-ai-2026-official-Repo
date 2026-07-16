# Kawood Mastery Challenge — Collaboration with Git

Master remote workflows, pull requests, and conflict resolution to lead distributed AI teams.

## Question 1: Remote Repositories as Communication Hubs
What does "adding a remote" accomplish, and why is `origin` the standard name?
- C. It links your local repository to a server location, enabling team collaboration; `origin` conventionally names the shared repository where all pushes flow, creating a single source of truth- A. Remotes are just file backups- B. Remote is a single fixed location per developer- D. Multiple remotes are not useful
**Answer: C** — Remotes are the network topology of distributed development.

---

## Question 2: Push vs Pull Workflow
Explain the asymmetry: You can pull from a colleague's branch immediately, but they can't see your branch until you push. What protection does this provide?
- A. You can share incomplete work without broadcasting it—pushing only when ready gives you control over what's shared; pulling from teammates is always safe because it only updates your local copy- C. There is no difference between push and pull- D. Everyone should always see all changes instantly- B. Pushing and pulling happen simultaneously
**Answer: A** — Asymmetry provides creative freedom before publication.

---

## Question 3: Pull Request Purpose (Beyond Just Merging)
A pull request isn't just a merge mechanism. What three things does it enable for AI teams beyond the merge itself?
- C. Code review (catching errors), discussion (sharing context), and CI/CD integration (automated testing)—PRs turn merging into a documented, quality-gated process- D. PRs are only for merging code- B. PRs are unnecessary bureaucracy- A. The merge button could work just as well
**Answer: C** — PRs are asynchronous collaboration architecture.

---

## Question 4: Code Review and Accountability
A reviewer looks at your PR and comments: "This loop has O(n²) complexity. The model won't scale to 1M samples." How should you respond, and why does respectful feedback matter in AI teams?
- D. Thank the reviewer, update the code to O(n log n), commit the fix, and re-request review—respectful review cycles catch real performance problems and build trust across the team- A. Ignore the feedback; you know better- B. Become defensive; your code is perfect- C. Ask the reviewer to just merge it anyway
**Answer: D** — Review is a trust-building protocol when executed with humility.

---

## Question 5: Merge Conflict Scenario
Two researchers push nearly simultaneously to main. Researcher B's push is rejected with "non-fast-forward update." They run `git pull`, and Git reports a merge conflict in `config.yaml`. Walk through the conflict resolution process.
- A. Open `config.yaml`, see conflict markers (`<<<<<<<`, `=======`, >>>>>>>), decide which changes are needed (both might be valid), edit manually, then `git add config.yaml` && `git commit` && `git push`—this forces explicit decision-making- C. Run `git merge --abort` and give up- B. Overwrite the file with your version- D. Delete the file entirely
**Answer: A** — Conflict resolution is where Git forces explicit communication.

---

## Question 6: Resolving Merge Conflicts Politely
You and your teammate both modified the model training hyperparameters in the same commit. The conflict shows: your learning rate change vs their batch size change. Both are correct. What's the ethical approach?
- D. Integrate both changes—git often auto-merges non-conflicting parts; manually test that both changes coexist correctly; if unsure, discuss with your teammate before committing- C. Accept only your changes and discard theirs- A. Merge randomly and hope it works- B. Ask Git to decide automatically
**Answer: D** — Respectful conflict resolution integrates diverse expertise.

---

## Question 7: PR Review Checklist
As a reviewer, what five categories should you examine in a PR before approving?
- A. Correctness (logic sound?), testing (new tests added?), performance (will it scale?), style (follows conventions?), documentation (will future readers understand?)—this checklist prevents tech debt- D. Just check if the code runs- B. Don't review; just approve everything- C. Only review the first line of code
**Answer: A** — Comprehensive review prevents future headaches.

---

## Question 8: Small, Focused Changes
Your colleague's PR has 2,000 lines changed across 15 files. The reviewer comments: "Please split this into three smaller PRs by feature." Why is this request about quality, not bureaucracy?
- D. Smaller PRs are easier to review, test, and revert if needed; they clarify which changes introduced a bug; large PRs hide problems in noise- C. Reviewers are just being difficult- A. Large PRs are more efficient- B. PR size doesn't matter
**Answer: D** — Modularity is a quality attribute, enforced through process.

---

## Question 9: Deployment and Testing Before Merge
Your team has a rule: "No PR merges without passing CI/CD." A colleague's PR fails a test but says, "The test is flaky; let me merge anyway." How should you respond?
- A. Don't approve—flaky tests are bugs too; either fix the test or fix the code to be more robust; approving teaches the team that rules are flexible, which erodes standards- B. Let them merge; flaky tests are acceptable- C. Have them commit directly to main to bypass the test- D. Disable the test
**Answer: A** — Consistency in standards prevents "just this once" from becoming a habit.

---

## Question 10: Remote as Backup and Continuity
Your laptop crashes. You hadn't pushed today's work. Meanwhile, a teammate has pushed their branch. Explain what's lost, what's recoverable, and what this teaches about push frequency.
- A. Local unpushed commits are lost (git can't recover); pushed commits survive on the server; this teaches that pushing frequently (at least daily) is catastrophe insurance—unpushed work is temporary and vulnerable- D. Everything is recoverable from git- C. Nothing is backed up by default- B. Pushing is optional
**Answer: A** — Remote is a disaster recovery mechanism; push daily.
