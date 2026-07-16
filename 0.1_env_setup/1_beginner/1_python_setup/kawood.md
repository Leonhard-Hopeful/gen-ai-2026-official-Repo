# Kawood Mastery Challenge — Python Setup

Master Python installation and environment configuration to build reproducible development foundations.

## Question 1: System Python vs Managed Python
Explain why developers shouldn't use the system Python directly for projects. What problems emerge when you do?
- B. System Python is managed by the OS; updating the system might break it; projects have conflicting dependency versions—using managed Python (venv/conda) isolates each project and survives OS updates- A. System Python is fine for everything- C. This distinction doesn't matter- D. Only experienced developers need to care
**Answer: B** — System Python is shared infrastructure; projects need isolation.

---

## Question 2: Python Version Selector
Your project requires Python 3.11, but your system has 3.9 by default. How do you solve this without breaking other projects?
- A. Use pyenv or similar to install 3.11, set it locally for this project (`pyenv local 3.11.0`), create venv with that Python—this gives you the right version without affecting system or other projects- C. Upgrade system Python to 3.11- B. Just use 3.9; version doesn't matter- D. This is unsolvable
**Answer: A** — Version management is precision infrastructure.

---

## Question 3: Installation Verification
After installing Python 3.11, how do you verify it's correctly installed and accessible?
- A. Run `python --version` (or `python3.11 --version` specifically), verify it shows 3.11; check `which python` shows the right path—verification prevents silent failures- D. Just assume it worked- B. There's no way to verify- C. Installation always works
**Answer: A** — Verification is trust but verify.

---

## Question 4: PATH and Confusion
You have both Python 3.9 and 3.11 installed. You type `python --version` and get 3.9, but you wanted 3.11. Explain what's happening and how to fix it.
- A. Your PATH environment variable lists Python 3.9 first; reorder PATH or use `python3.11` explicitly—PATH ordering determines command resolution; the first match wins- C. Both versions conflict and can't coexist- B. This situation is impossible- D. Use `alias python=python3.11`
**Answer: A** — PATH management is execution control.

---

## Question 5: Platform-Specific Considerations
You're installing Python on Windows, macOS, and Linux. Are installation steps identical across platforms?
- D. Core concepts are the same, but specific tools differ—Windows often uses the installer.exe; macOS uses Homebrew; Linux uses apt/yum—some libraries (like OpenCV) have platform-specific build requirements; test on each platform- A. Installation is identical everywhere- B. Python doesn't run on Windows- C. Platform doesn't matter
**Answer: D** — Cross-platform requires platform-specific knowledge.

---

## Question 6: IDE Integration
You install Python 3.11 and create a venv, but your IDE still shows Python 3.9 as the interpreter. How do you fix this?
- A. Explicitly configure the IDE to use the venv interpreter—most IDEs (VSCode, PyCharm) have interpreter selection; point to venv/bin/python (Linux/Mac) or venv/Scripts/python.exe (Windows); IDE must know where Python lives- D. IDEs automatically detect all Python installations- B. This can't be fixed- C. Reinstall the IDE
**Answer: A** — IDE configuration is explicit, not magical.

---

## Question 7: Pip Installation
After installing Python, `pip --version` fails. What's likely wrong?
- C. Python didn't install pip correctly, or pip isn't in PATH—verify `python -m pip --version` (using module syntax)—this is a fallback when pip command doesn't work; if it fails, reinstall Python, ensuring pip is included- D. Pip doesn't exist- B. Pip installation is separate from Python- A. This is unfixable
**Answer: C** — `python -m pip` is the reliable fallback.

---

## Question 8: Troubleshooting Failed Installation
Python installation appeared to succeed, but `import sys` fails in a script. What diagnostics would you run?
- A. Verify interpreter path (`which python` on Unix, `where python` on Windows); check `python --version` matches expected version; run `python -c "import sys; print(sys.executable)"`—these reveal path mismatches and silent failures
- B. Just reinstall
- C) These diagnostics aren't useful
- D. Just give up

**Answer: A** — Diagnostics reveal the discrepancy between expectation and reality.

---

## Question 9: Documentation Review
Python.org provides installation guides for each OS. Why is reading these docs, rather than skipping straight to install, worth 5 minutes?
- D. Docs explain OS-specific prerequisites (VS Build Tools on Windows), PATH implications, and troubleshooting—skipping docs leads to 30-minute failures; reading ahead prevents them- A. Installation is self-explanatory- B. Documentation slows you down- C. Read-throughs are busywork
**Answer: D** — Documentation prevents mistakes faster than trial-and-error recovers from them.

---

## Question 10: Verification at Depth
After setup, verify not just that Python works, but that all basic components you'll need work. What script confirms readiness?
- B. Test script running: `python -c "import sys, os, json; print('Python ready!')"` plus a numpy/pandas import—this quick validation catches missing dependencies and interpreter misconfigurations before you lose hours in a large project- A. Installation itself is enough verification- C. Testing isn't necessary- D. Setup can't be fully verified
**Answer: B** — Smoke tests are your first line of defense.
