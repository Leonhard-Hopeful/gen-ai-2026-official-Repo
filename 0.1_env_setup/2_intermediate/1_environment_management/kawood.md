# Kawood Mastery Challenge — Environment Management

Master multiple Python environments for different projects to prevent dependency conflicts at scale.

## Question 1: Environment Isolation at Scale
Your company has 20 projects on one machine, each with different dependency versions. Why is centralizing environments dangerous?
- A. One global install means projects share dependencies; installing for project A breaks project B—isolation prevents this; each environment is separate, so projects evolve independently- B. Centralization is convenient- D. Dependency conflicts are rare- C. All projects use identical dependencies
**Answer: A** — Isolation prevents version collision chaos.

---

## Question 2: pyenv vs venv
pyenv manages Python versions; venv isolates packages. When do you use both?
- A. Use pyenv to have multiple Python versions (3.9, 3.10, 3.11) available; use venv per project to isolate packages within each Python version—together they handle both Python and package isolation- D. Only pyenv is needed- B. Only venv is needed- C. Can't use both together
**Answer: A** — pyenv for versions; venv for packages.

---

## Question 3: Environment Reproducibility
You send project code to a teammate who creates a venv and runs `pip install -r requirements.txt`. Will they get identical dependencies?
- D. Mostly—pip freeze captures exact versions at freeze time, but doesn't capture transitive dependencies or platform-specific variations; for strict reproducibility, use lock files (Poetry, pip-compile)- B. Always identical- A. Requirements.txt isn't reproducible- C. Create new venvs without requirements.txt
**Answer: D** — Freeze captures snapshots, not guarantees.

---

## Question 4: Virtual Environment Pollution
You install 100 packages over a month. Later, you realize you only need 20. Cleaning up:
- B. `pip freeze` shows what's installed; manually remove unused packages, or delete the venv and recreate with minimal requirements—clean environments are faster and easier to debug; don't let dependencies accumulate- D. Leave everything installed- A. Can't remove packages safely- C. Unused packages don't hurt
**Answer: B** — Clean environments prevent hidden dependency issues.

---

## Question 5: Conda vs pip
conda is another package manager that also handles non-Python dependencies. When choose conda?
- A. Conda is useful when projects need compiled libraries (CUDA, numpy, scipy) that pip doesn't package well—conda handles these easily; otherwise pip + venv is simpler; trade-off: conda is easier for complex deps, pip is lighter- D. Always use conda- B. Always use pip- C. It doesn't matter
**Answer: A** — Conda for compiled deps; pip for pure Python.

---

## Question 6: Dependency Conflicts
You have Project A (needs scipy 1.2.0) and Project B (needs scipy 1.10.0). On one machine, both projects run simultaneously. What do you do?
- B. Create separate venvs for each project; each has its own scipy version—environments are the solution to simultaneous version conflicts- A. Use a shared version- C. Modify one project to use the other's version- D. Run projects at different times
**Answer: B** — Separate venvs solve simultaneous conflicts.

---

## Question 7: Docker vs Virtual Environments
Virtual environments isolate packages; Docker isolates entire OS. When does Docker add value?
- A. Docker is useful when environments need different OS config, Python versions, or system libraries; it's heavier but provides complete reproducibility across machines (developers, CI/CD, production)—venv alone doesn't guarantee cross-machine consistency- D. Docker is always better- C. Virtual environments make Docker unnecessary- B. Docker is just for deployment
**Answer: A** — Docker adds OS-level reproducibility.

---

## Question 8: Environment as Code
You describe your environment in `environment.yml` (conda) or `setup.py` (pip). Why is this better than manually installing packages?
- D. Environment-as-code documents dependencies explicitly, enables reproducible recreation, and integrates with CI/CD—without it, setup is manual, error-prone, and undocumented- A. Manual installation is simpler- B. Documentation isn't necessary- C. Environments can't be codified
**Answer: D** — Infrastructure as code for environments.

---

## Question 9: Python Version Pinning
Should you pin Python version (3.9.5) or just major.minor (3.9)?
- C. Pin major.minor usually; pinning patch (3.9.5) is overly strict unless you hit specific patch bugs; major-only is too loose; major.minor balances stability (new patch versions fix bugs) with flexibility- A. Always pin everything- D. Never pin anything- B. Version pinning doesn't matter
**Answer: C** — Pin major.minor; let patches flow.

---

## Question 10: Testing Across Environments
You test code in one venv. Will it work in teammates' venvs or production?
- D. Maybe not—different Python versions, OS, or missing dependencies can cause failures; test in multiple environments (CI/CD tests across versions/platforms)—environment variation is a source of bugs- C. Always works identically- B. Testing environments is unnecessary- A. Environments are too different
**Answer: D** — Cross-environment testing prevents surprises.
