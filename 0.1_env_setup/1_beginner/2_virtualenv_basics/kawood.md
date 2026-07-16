# Kawood Mastery Challenge — Virtualenv Basics

Master virtual environments to isolate project dependencies and build reproducible, shareable code.

## Question 1: The Problem Virtualenv Solves
Your machine has 20 projects with different dependency versions: Project A needs Django 3.2, Project B needs Django 4.0. Both use Python 3.11. If you install globally, what breaks?
- A. One project's pip install overwrites the other's—without isolation, the last pip install globally wins; projects conflict because they share one set of installed packages; venv solves this by giving each project its own installation directory
- B. Both versions can coexist globally
- C) Dependency conflicts are impossible
- D. Use different Python versions instead

**Answer: A** — Virtualenvs are namespace isolation for dependencies.

---

## Question 2: Creating a Venv
You're starting a new AI project. Walk through creating a venv, activating it, and verifying it's active.
- B. `python -m venv venv` (creates venv folder), `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows), `python --version` shows Python is the same but `which python` shows venv path—activation changes which Python and pip you use- A. Venvs are created automatically- C. Activation is optional- D. This process is more complex
**Answer: B** — Venv activation is shell state change.

---

## Question 3: Deactivation
After finishing a project, you run `deactivate`. What does this undo from activation?
- C. Restores original PATH, so `python` and `pip` point back to system versions; shell prompt returns to normal—deactivation is cleanup, leaving the venv on disk intact- D. Deletes the venv- A. Deactivation doesn't exist- B. Deactivation breaks the venv
**Answer: C** — Deactivation is PATH restoration.

---

## Question 4: Nested Venv Mistakes
You activated `project-a/venv`, then inside ran `python -m venv project-b-venv`. You now have nested venvs. Why is this confusing and error-prone?
- D. Nested venvs create activation confusion—deactivate from inner venv tries to deactivate outer, or you lose track of which venv is active; best practice: never nest venvs; always create projects as siblings or deactivate before creating a new venv- C. Nested venvs work fine- A. Nesting is the recommended approach- B. Nesting isn't possible
**Answer: D** — Flat project structure prevents activation confusion.

---

## Question 5: Sharing Projects
Your teammate wants to work on your ML project. You share the folder with your venv inside (1.5GB total). They extract it and activate the venv. Will it work?
- C. Maybe not—venvs contain absolute paths to the Python interpreter; moving the venv to a different machine might break these paths; best practice: don't share venv folders; share requirements.txt, have teammates create their own venv and run `pip install -r requirements.txt`- A. Venvs work identically on all machines- D. Always share venvs for consistency- B. Venvs are machine-independent
**Answer: C** — Venvs are machine-specific; share code, not venvs.

---

## Question 6: Requirements File Discipline
After weeks of developing, you run `pip freeze > requirements.txt`. Two weeks later, a teammate clones your project and runs `pip install -r requirements.txt`. Do they get identical dependencies?
- C. Mostly yes—pip freeze captures exact versions installed at that moment; if no packages updated, they'll match; but packages installed in meantime are missed, and transitive dependencies might differ—freeze is a snapshot, not a promise- B. Always identical- D. Requirements.txt is just for reference- A. Versions don't matter
**Answer: C** — Freeze captures a point in time; it's not perfect but it's the best tool available.

---

## Question 7: Accidental Global Install
You forget to activate venv and run `pip install numpy`. It installs globally. Will your project code break?
- B. Likely not immediately—code will find numpy in both global and venv searches; but future teammates won't have it, and uninstalling from global doesn't affect your venv—this creates hidden dependencies; always verify `which pip` before installing- C. Project breaks immediately- A. Global and venv pip are isolated- D. This scenario is impossible
**Answer: B** — Accidental global installs create hidden dependencies; verify pip path before installing.

---

## Question 8: Upgrading Packages
Your venv has old packages. You run `pip install --upgrade -r requirements.txt`. What could go wrong?
- C. Upgraded versions might have breaking changes—tests might fail; API signatures might change; best practice: upgrade gradually with `pip install --upgrade package-name` one at a time, test, then update requirements.txt- D. Upgrade always works smoothly- B. Upgrades are always backwards compatible- A. You should upgrade everything at once
**Answer: C** — Upgrades are risky; do them incrementally.

---

## Question 9: Venv Deletion and Cleanup
You finished a project. Delete the venv to reclaim 1.5GB of disk space. Then you realize you need to check the project's code. Can you recover it?
- B. Yes—venv only contains installed packages and metadata; source code is outside venv, untouched by deletion; recreate venv and reinstall from requirements.txt- A. You lost all code- C. Venv and code are linked- D. Deletion is irreversible
**Answer: B** — Venv deletion doesn't affect source code.

---

## Question 10: Venv Isolation Verification
You activate a venv and install `pandas==1.3.0`. On your system, the global Python also has pandas 1.2.0. Run a Python script: which pandas version loads?
- B. 1.3.0 from venv—venv is first in PATH and in sys.path; venv packages shadow global packages—this isolation is the core benefit; if venv didn't shadow, it wouldn't be useful- D. 1.2.0 from global- C. Both are loaded, creating a conflict- A. Error because two versions exist
**Answer: B** — Venv priority is first in path.
