# Kawood Mastery Challenge — Git Basics

Master the foundational Git commands and workflows that secure your code and enable collaboration.

## Question 1: Atomic Commits
When you commit code, what does it mean to make an "atomic change," and why is this crucial in AI projects where multiple experiments run in parallel?
- C. A change that is complete, self-contained, and testable in isolation—ensuring any branch or experiment can be reverted without breaking others- B. A change that uses the `-a` flag to automatically commit all files at once- D. A change that must be committed on a Monday at 9 AM for best results- A. A change that is small enough to fit in a single line of code
**Answer: C** — Atomic commits are essential in AI because you may need to revert a failed experiment without affecting other researchers' work.

---

## Question 2: Status and Diffs
You run `git status` and see "modified: model.py". When would you use `git diff` instead, and what would it reveal?
- A. `git diff` shows the exact line-by-line changes you made since the last commit—critical when reviewing what you actually changed before committing- D. `git diff` is the same as `git status`, just slower- C. `git diff` tells you if your code will run correctly- B. `git diff` compares two different repositories
**Answer: A** — `git diff` reveals the exact changes, helping you catch unintended modifications or debug incremental changes.

---

## Question 3: Repository Initialization vs Cloning
Your team is starting an AI project. When should you use `git init` vs `git clone`? What goes wrong if you choose incorrectly?
- A. Use `git init` when creating a brand new project locally; use `git clone` when downloading an existing project from a remote server—cloning saves setup time and automatically links to the remote- C. They are the same; use whichever one you prefer- B. Always use `git init`, even if the project already exists on GitHub- D. Always use `git clone`; `git init` is obsolete
**Answer: A** — Choosing correctly ensures your team's work is synced and prevents duplicate repositories.

---

## Question 4: Commit History and Blame
A critical bug was introduced in the model evaluation pipeline last week. You need to identify which commit caused it. What is the correct command, and what will it tell you?
- A. `git log` shows the full history with commits, and `git blame file.py` pinpoints which commit and author changed each line—this is your diagnostic tool- C. `git status` will show you who caused the bug- D. `git init` will revert the bug automatically- B. There is no way to find out who caused the bug
**Answer: A** — `git log` and `git blame` are detective tools that help you trace bugs to their source.

---

## Question 5: Staging Area Mastery
You have 5 modified files, but only 3 of them should be in your next commit. Walk through the correct workflow using `git add`, `git status`, and `git commit`.
- B. Use `git add filename.py` three times to stage only the files you want, verify with `git status`, then commit—this gives you fine-grained control over what goes into each commit- C. Use `git add .` to add everything, then commit- D. Delete the 2 files you don't want, commit, then restore them- A. Run `git commit` and manually select files during the commit process
**Answer: B** — The staging area is a powerful feature for organizing related changes into logical commits.

---

## Question 6: Recovering from Mistakes
You accidentally committed `secrets.txt` containing API keys. You haven't pushed yet. What is the safest way to remove it from the last commit, and why is speed important here?
- B. Use `git reset HEAD~1` to undo the commit (keeping changes), remove the file, add it to `.gitignore`, then recommit—doing this before pushing prevents the secret from reaching the remote where it could be exposed- A. Push immediately so others can see your mistake- C. Delete your entire repository and start over- D. There is no way to undo a commit
**Answer: B** — Swift action before pushing prevents secrets from leaking to the remote repository.

---

## Question 7: Multi-User Workflow (Scenario)
Two researchers push commits to the same `main` branch within 5 minutes of each other. The second push is rejected. Explain what happened, why it's a safety feature, and what the researcher should do next.
- B. The remote has newer commits; Git prevents overwriting work. The researcher should run `git pull` to fetch the latest changes, then push again—this protects against accidentally deleting teammates' work- C. The first researcher has Git disabled- D. The second researcher has the wrong Git version- A. This is impossible in Git
**Answer: B** — Git's refusal to overwrite is a safety mechanism that forces explicit integration of teammates' changes.

---

## Question 8: Best Practices for AI Project Longevity
Your AI project will run for 2 years with dozens of team members joining and leaving. Describe what commit message format, frequency, and content practices will make your project's history valuable to future developers.
- B. Use clear, descriptive messages explaining the "why," commit logical units frequently (daily minimum), and avoid committing broken code—this creates searchable history that helps team members understand decisions months later- C. Write short messages like "fix"; commit once per month in one giant commit- A. Don't worry about messages; just use commit hashes- D. Commit every keystroke so the history is as detailed as possible
**Answer: B** — Well-crafted history is an investment in team productivity and knowledge preservation.

---

## Question 9: Diff as a Code Review Tool
Before merging a branch into main, a reviewer needs to check your changes. What command shows them exactly what's different, and what should they look for?
- A. `git diff main..feature-branch` shows all changes—reviewers should check for logic errors, performance issues, missing error handling, and alignment with team standards- C. The reviewer should just run your code and trust it works- D. There is no way for others to review your changes- B. Use `git log` instead of `git diff`
**Answer: A** — `git diff` enables asynchronous code review, a cornerstone of distributed AI development.

---

## Question 10: History Rewriting Ethics
You want to use `git rebase -i` to clean up your commit history before merging. When is this safe vs dangerous?
- C. It's safe only on branches you haven't pushed to a shared remote; never rebase public history because it rewrites commits that teammates might depend on, creating chaos- D. It's always safe- B. It's never safe- A. It only affects your local machine, so it doesn't matter
**Answer: C** — Understanding the boundary between local and public history prevents team conflicts.
