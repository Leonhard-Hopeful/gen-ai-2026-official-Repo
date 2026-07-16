# Kawood Mastery Challenge — IDE Tools

Master IDE configuration to turn your editor into a productivity powerhouse for AI development.

## Question 1: IDE vs Text Editor
What distinguishes an IDE from a text editor, and why do these features matter for AI projects?
- A. IDE provides debugging, code completion, refactoring, linting—these save hours by catching errors before runtime, suggesting fixes, and automating repetitive changes; text editors don't, making development slower and error-prone- D. There's no real difference- C. Text editors are better for coding- B. IDE features are just nice-to-haves
**Answer: A** — IDE features are productivity multipliers.

---

## Question 2: Python Interpreter Configuration
Your IDE shows a red squiggle under `import numpy` even though numpy is installed in your venv. How do you fix this?
- D. Configure IDE to use the venv interpreter (Settings > Python > Interpreter, select venv/bin/python)—IDE must know which Python you're using; without this, it looks in system Python, missing venv packages- A. Reinstall numpy- C. This can't be fixed- B. The IDE is broken
**Answer: D** — IDE interpreter configuration is essential.

---

## Question 3: Debugging Workflow
Your model training script crashes mysteriously on line 47. You could add print statements, or use the debugger. Which is faster for tracking down the bug?
- B. Debugger—set a breakpoint on line 47, inspect variable values, step through execution, watch state change in real-time; print statements require guessing what to print and re-running code- C. Print statements are simpler- D. Debugging tools are overcomplicating- A. Both take equal time
**Answer: B** — Debuggers are surgical; print statements are blunt instruments.

---

## Question 4: Code Completion Benefits
Your IDE autocompletes `model.tra` to `model.train()`, showing you the method exists. What problem does this prevent?
- C. Prevents typos (misspelling method names), exposes available APIs (discovering methods you forgot about), and saves typing—without completion, you type full names from memory and make mistakes- A. Completion slows you down- D. You should memorize all methods- B. Completion causes problems
**Answer: C** — Completion is both error prevention and API discovery.

---

## Question 5: Linting Setup
Your IDE doesn't highlight PEP8 style violations. How do you enable linting?
- D. Install a linter (pylint, flake8), configure IDE to use it (Settings > Linting)—linters automatically flag style violations, unused variables, and common errors without running code- B. Linting is optional- A. Style doesn't matter- C. Linting requires manual checking
**Answer: D** — Linters are automated quality gatekeepers.

---

## Question 6: Terminal Integration
Your IDE has a built-in terminal. Why not just use the system terminal?
- B. IDE terminal has IDE context—opens in project directory, uses project Python/venv automatically, integrates with editor panels—this saves context switching; system terminal requires manual navigation- C. There's no advantage- D. System terminal is always better- A. IDE terminal is less reliable
**Answer: B** — IDE terminal is context-aware convenience.

---

## Question 7: Extensions and Plugins
VSCode has thousands of extensions. Which three matter most for Python/AI development?
- B. Python (language server), Jupyter (notebooks), and Pylance (type checking)—these provide completion, debugging, and notebook support; too many extensions bloat the IDE- A. Install all extensions- D. Extensions are unnecessary- C. Extension choice doesn't matter
**Answer: B** — Selective extensions amplify productivity.

---

## Question 8: Refactoring with IDE
You rename a function `calculate_loss` to `compute_loss`. The IDE can automatically rename all 23 references across the codebase. Why is this better than find-and-replace?
- B. IDE rename is scope-aware—it renames the function and all calls, but not unrelated strings with the same name; find-and-replace would catch false positives—semantic rename is safer and more accurate- C. They're equivalent- A. Find-and-replace is safer- D. Manual rename is most accurate
**Answer: B** — Semantic refactoring is intelligent renaming.

---

## Question 9: Workspace Configuration
Your team uses VSCode. You share a `.vscode/settings.json` in the repo with Python path, linting rules, and formatting standards. Why is shared config important?
- A. Everyone's IDE behaves identically—consistent linting, formatting, and debugging setup; new teammates get the same experience instantly; no "but it works on my machine" excuses- B. Personal config is better- C. Shared config enforces unnecessary rules- D. IDE config is always personal
**Answer: A** — Shared IDE config aligns the team.

---

## Question 10: Debugging Complex AI Code
You're training a model with a custom loss function. It NaNs out after 10 epochs. Debugger or print statements? Why?
- B. Debugger—set breakpoint in loss computation, inspect gradient values at each epoch, step through to find where NaN first appears—print statements would require guessing which variables to print; debugger lets you explore freely- C. Print statements are simpler- A. Can't debug custom loss functions- D. Manual inspection is best
**Answer: B** — Debugger is interactive exploration.
