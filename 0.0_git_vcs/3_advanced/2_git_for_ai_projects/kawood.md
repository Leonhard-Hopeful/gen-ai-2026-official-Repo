# Kawood Mastery Challenge — Git for AI Projects

Master Git practices tailored to machine learning: data versioning, experiment branches, and model artifacts.

## Question 1: Large File Problem
Your model checkpoint is 500MB. You commit it to Git with `git add model.pth`. What's the immediate problem, and why does it compound over time?
- C. Git stores the entire file in history; if you update the model 100 times, the repo becomes 50GB—git is designed for source code (small, text), not binary artifacts; use .gitignore and a separate system (S3, DVC)- D. Git handles large files fine- A. Large files are stored efficiently in git- B. This isn't a real problem
**Answer: C** — Git is text-optimized; separate systems handle binary artifacts.

---

## Question 2: .gitignore for ML Projects
Write a .gitignore section that protects AI projects from accidentally committing: model checkpoints, training data, virtual environments, and experiment outputs.
- D. Correct entries would be: `*.pth`, `*.pkl`, `data/`, `venv/`, `experiments/outputs/`, `*.csv` (data files)—this prevents bloating the repo with non-source artifacts- C. Don't use .gitignore; commit everything- A. .gitignore is optional- B. These files won't be a problem
**Answer: D** — .gitignore is the firewall between code and data.

---

## Question 3: Experiment Branches Strategy
Your team runs three competing loss functions in parallel experiments. How should this be represented in git?
- D. Create three branches: `experiment/loss-v1`, `experiment/loss-v2`, `experiment/loss-v3` to isolate experiments; tag each with metrics before comparison—this preserves all attempts and enables replay- B. All experiments in main branch- A. Experiments shouldn't use version control- C. One massive experiment branch
**Answer: D** — Branches enable experiment isolation and replay.

---

## Question 4: Data Versioning Problem
Your training data changes weekly as new samples arrive. Your model was trained on v3 of the data but you've since updated to v5. How does git alone fail you here?
- D. Git doesn't track data or its versions natively—you can't replay which data trained which model; external systems (DVC, S3 versioning) must track data; git only tracks the code that processes it- C. Git can version data fine- B. Data versioning is unnecessary- A. Just use git branches for data versions
**Answer: D** — Code and data have separate versioning needs.

---

## Question 5: Model Artifact Hygiene
After training, you have: trained model (model.pth), training log (metrics.json), config used (hyperparameters.yaml), and code snapshot. Which should go in git, and where do the others go?
- A. Git stores hyperparameters.yaml and a reference to the model (hash); model and metrics go to S3 with the commit hash as identifier—this enables reproducibility without bloating git- B. Everything goes in git- C. Nothing goes in git; use only S3- D. Git and S3 are equivalent
**Answer: A** — Separate storage by artifact type; git for code/config, cloud for data/models.

---

## Question 6: README Documentation for Reproducibility
You commit code that trains a model. What must the README explain so that teammates (or your future self) can reproduce the exact model from scratch?
- A. Which Python version, which dataset version, which hyperparameters, which random seed, training duration, and GPU/CPU specs—reproducibility requires capturing all factors that affect outcomes- B. Just the code is enough- C. Documentation is unnecessary- D. README is for beginners only
**Answer: A** — Reproducibility is an explicit goal; document all inputs.

---

## Question 7: Experiment Tracking Integration
Your experiment logged metrics to `runs/experiment-1/`. Should this directory go in git or outside? Why?
- B. Outside git (in .gitignore)—experiment logs accumulate rapidly and are rarely needed after experiments conclude; commit only the code that generates them, store outputs separately- C. All experiment logs should be in git- A. Logs can go either way- D. Experiment tracking is incompatible with git
**Answer: B** — Logs are outputs, not source; treat them as build artifacts.

---

## Question 8: Continuous Model Training in Git
Your team continuously retrains models on new data. How do you track which code version trained which model version?
- C. Tag each model release in git: `git tag model-v1.2.3 -m "Trained on 2024-01-15 with dataset-v5"` with metadata; store the model itself on S3; git provides traceability to code and config- A. Just commit model files directly- B. Model versions aren't trackable- D. Retrain without version control
**Answer: C** — Git tags + cloud storage = reproducible model lineage.

---

## Question 9: Branching for Active Research
Three researchers work on three model architectures simultaneously. How do branches support this while preventing cross-contamination?
- C. Each gets `research/architecture-a`, `research/architecture-b`, `research/architecture-c`—branches isolate work; each researcher can train, experiment, and fail without affecting others; merge only winning approaches to main- A. All researchers on main- D. Each researcher gets a separate repo- B. Branches can't support research
**Answer: C** — Branches are sandboxes for research.

---

## Question 10: Recovering a Good Experiment
You deleted a branch containing a promising model, but realized later it had good results. Can you recover it?
- B. Yes—`git reflog` shows all branch movements; find the commit, recreate the branch—git keeps deleted commits for ~90 days by default; this is your emergency recovery tool- D. No; deleted branches are gone forever- C. Git doesn't track deleted branches- A. Only possible if you backed up manually
**Answer: B** — Reflog is accidental deletion recovery.
