# Kawood Mastery Challenge — Release Management

Master versioning, release tagging, and deployment processes to ship AI systems with confidence.

## Question 1: Semantic Versioning
Your model API is at version 1.2.3. You add a new prediction endpoint (backward compatible). A week later, you optimize inference (no API changes). Two weeks later, you change the output format (breaking change). What versions should these be, and why?
- B. 1.3.0 (new feature), 1.3.1 (patch/performance), 2.0.0 (breaking)—semantic versioning signals impact to users: patch for safe updates, minor for features, major for breaking changes- C. Always increment to the next version- A. Version numbers are arbitrary- D. Versioning doesn't matter
**Answer: B** — Semantic versioning is a contract with your users.

---

## Question 2: Tagging Releases
Before shipping model v2.1.0, you create `git tag v2.1.0 -m "Release notes: improved inference latency by 15%"`. Why is this better than committing with message "v2.1.0"?
- A. Tags are immutable pointers to specific commits, enabling precise rollbacks; commits can be rewritten or deleted, but tags persist—releases need immutable anchors- C. Tags and commit messages are equivalent- D. Tagging is unnecessary busywork- B. Tags are only for public projects
**Answer: A** — Tags are release checkpoints; commits are not.

---

## Question 3: Release Branch Process
You're preparing v3.0.0 for shipment next Friday. You create `release/v3.0.0` from main today. Over the next week, what goes in this branch vs main?
- D. Release branch gets only bug fixes, version bumps, release notes; main continues feature development—this allows stabilization without blocking new work- B. Everything goes everywhere- A. Release branches stop main development- C. This process is too complex
**Answer: D** — Release branches decouple stability from progress.

---

## Question 4: Hotfix Emergency
Production inference pipeline crashes on 5% of requests. You need to ship a fix TODAY without waiting for next Monday's planned release. Walk through the hotfix workflow.
- C. Create `hotfix/crash-fix` from production tag (e.g., v2.1.0), fix bug urgently, test with production data sample, tag as v2.1.1, merge into main and active release branches, deploy to production—this ensures the fix reaches all code paths- D. Patch production directly without version control- B. Wait for next scheduled release- A. Hotfixes are not recommended
**Answer: C** — Hotfixes are the emergency response system.

---

## Question 5: Canary Deployment Integration
Before releasing v3.0.0 to all users, you deploy it to 5% of traffic and monitor metrics. What in git supports this practice?
- C. Feature flags in the code (toggled by configuration, not git branches) allow deploy without deploy—but git tracks which version (via tags) is running where; monitor metrics before scaling to 100%- B. Version control directly controls deployment percentage- A. Canary deployments are independent of version control- D. Git can't support canary deployments
**Answer: C** — Git provides version identity; feature flags provide deployment control.

---

## Question 6: Rollback Protocol
A production model crashed shortly after shipping v2.5.0. You need to rollback to v2.4.3 within 5 minutes. What must be prepared in advance?
- C. Pre-stage the v2.4.3 container/deployment, document rollback steps, test rollback procedure in staging beforehand—speed demands preparation; winging it takes 30+ minutes- A. Rollback can happen on-the-fly- D. No preparation is needed- B. Rollbacks are too dangerous to practice
**Answer: C** — Rehearsed rollbacks are fast; improvised rollbacks are slow.

---

## Question 7: Changelog Maintenance
Your CHANGELOG.md should document what went into v2.5.0. Should you write it while coding, before release, or after?
- D. Throughout development—update CHANGELOG for each significant change; doing it at release time means hunting through commits to remember what was important; contemporaneous documentation is accurate- C. Write it at release time- B. Don't maintain a changelog- A. Changelog is busywork
**Answer: D** — Changelog maintenance is a development discipline.

---

## Question 8: Version Support Window
You've released v1.0, v2.0, and v3.0 (current). Users running v1.0 report a critical bug. Should you patch v1.0 or insist they upgrade to v3.0?
- C. Decision depends on support policy—define "support window" (e.g., support last 2 versions for 1 year); for v1.0 in window, patch it; outside window, require upgrade—clear policy prevents endless patching- A. Always support all versions forever- D. Never support old versions- B. Support policy doesn't matter
**Answer: C** — Support windows are economic boundaries.

---

## Question 9: API Deprecation Strategy
Your model API v1.0 is used by 100+ applications. You want to introduce breaking changes in v2.0 but can't abandon v1.0 users. How?
- A. Run both APIs in parallel for 6-12 months; warn users to upgrade; eventually sunset v1.0—this gives users time; maintain both git tags as active; gradually migrate load to v2.0- D. Force all users to v2.0 immediately- C. Keep v1.0 forever- B. Don't ever introduce breaking changes
**Answer: A** — Deprecation windows are migration assistance.

---

## Question 10: Release Notes Quality
Compare two release notes: (1) "Bug fixes and improvements." (2) "Fixed model evaluation timeout on datasets >1M rows (users saw 504 errors); improved inference latency by 12%; deprecated v1.0 API (sunset date: 2025-03-31)." What does the second accomplish that the first doesn't?
- D. The detailed notes tell users whether they should upgrade and what to prepare for—vague notes make adoption guesswork; specific release notes drive adoption decisions- B. Both are equivalent- C. Verbose notes are just busywork- A. Users don't read release notes
**Answer: D** — Release notes are user decision-making tools.
