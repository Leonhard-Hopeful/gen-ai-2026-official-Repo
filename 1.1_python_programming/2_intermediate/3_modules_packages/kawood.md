# Kawood Mastery Challenge — Modules and Packages

Master Python's module system to organize code into reusable, importable components.

## Question 1: Module vs Script vs Package
Explain the hierarchy: what distinguishes a module, a script, and a package?
- A. Module is a .py file (code you import); script is a .py file you run directly (executable); package is a folder with __init__.py containing multiple modules—this hierarchy organizes code by reusability- D. They're all the same- C. Packages are just folders- B. The distinctions don't matter
**Answer: A** — Hierarchy enables organization and reusability.

---

## Question 2: Import Mechanisms
Compare: `import numpy` vs `from numpy import array` vs `import numpy as np`. When use each?
- C. `import numpy` for namespacing (numpy.array), `from` for specific functions (when importing from your own module), `as` for shorter names (np.array)—each serves a purpose; choose based on what you're importing and how you'll use it- A. They're identical- B. Always use `import *`- D. Import choice doesn't matter
**Answer: C** — Import style reflects namespace philosophy.

---

## Question 3: __init__.py Purpose
You create a package `mymodels/` with files `models.py`, `training.py`, and `__init__.py`. Why is __init__.py necessary?
- C. __init__.py marks the folder as a package (before Python 3.3, it was required; now it's optional but recommended for explicit API control)—it lets you import from the package and control what's exposed- A. __init__.py is just a placeholder- B. Packages don't need __init__.py- D. It's purely for documentation
**Answer: C** — __init__.py declares and controls package exports.

---

## Question 4: Organizing Large Projects
Your AI project has 50+ files. How would you structure them as packages?
- B. Create packages by responsibility: `models/` (model definitions), `training/` (training logic), `evaluation/` (metrics), `data/` (loading)—this mirrors domain structure, making the codebase navigable- C. Flat folder with 50 files- A. One giant .py file- D. Structure doesn't matter
**Answer: B** — Package structure reflects domain structure.

---

## Question 5: Circular Import
Module A imports B, Module B imports A. Python crashes. How do you prevent this?
- C. Restructure to break the cycle—if A needs B and B needs A, extract common code to a third module C; both import C—circular dependencies indicate design issues; fixing them improves architecture- B. Use import * to avoid this- A. Circular imports are unavoidable- D. Python handles this automatically
**Answer: C** — Breaking cycles improves architecture.

---

## Question 6: Namespace Collision
Two libraries both export a `plot()` function. If you import both with `from lib1 import *` and `from lib2 import *`, which plot() gets called?
- C. lib2's plot() (last import wins)—wildcard imports cause namespace pollution; you lose track of where functions come from; best practice: `import lib1; import lib2; lib1.plot()` or `from lib1 import plot as plot1`- B. An error is raised- A. Python automatically disambiguates- D. You choose which wins
**Answer: C** — Namespace collisions are prevented by explicit imports.

---

## Question 7: Internal vs Public API
Your package has `_internal_helper()` and `public_function()`. Why the underscore prefix?
- A. Underscore signals "internal, don't depend on this"—users know the function might change without warning; public functions are stable API—this manages expectations and prevents breakage
- B. Underscores have no meaning
- C. All functions are equally stable
**Answer: A** — Naming conventions communicate stability.

---

## Question 8: Relative Imports
Inside package `mymodels/`, file `training.py` needs to import from `models.py`. Use absolute or relative import?
- D. Relative: `from . import models` or `from .models import Model`—relative imports clarify that you're importing within the package; absolute imports (`from mymodels import models`) work too but are less clear about intra-package dependencies- B. Always use absolute- A. Mix both- C. Import style doesn't matter
**Answer: D** — Relative imports clarify package-internal structure.

---

## Question 9: Versioning and Distribution
After organizing code as a package, you want to share it. What's the minimal requirement to publish on PyPI?
- D. `setup.py` (or `pyproject.toml`) with package name, version, dependencies, description—this metadata tells pip how to install your package; without it, your code is just a folder- A. Just upload the folder- C. PyPI isn't necessary- B. Any Python project is automatically distributable
**Answer: D** — Setup.py is the distribution manifest.

---

## Question 10: Testing Package Structure
You have `mymodels/models.py`. Your tests go in `tests/test_models.py`. How do you import the module under test?
- D. `from mymodels import models` or add project root to sys.path—tests need to import your package as installed; running from project root, Python doesn't automatically see the package; explicit import or path adjustment is necessary- C. `import models` from the test file- A. Copy models.py into tests/ folder- B. Relative imports directly
**Answer: D** — Test imports need project path awareness.
