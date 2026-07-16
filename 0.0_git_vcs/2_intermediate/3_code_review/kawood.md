# Kawood Mastery Challenge — Code Review and Quality

Master the art and discipline of code review to build reliable AI systems through collaborative scrutiny.

## Question 1: Why Code Review Is Not Optional
A senior developer argues: "Code review slows me down. I'm experienced; my code doesn't need review." Counter this with three reasons why review adds value even for experienced developers.
- D. Fresh eyes catch blind spots; reviewers know code contexts you don't; review documents decisions for future maintenance—even experts benefit from external perspective- C. Code review is busywork for juniors- A. Good developers don't need review- B. Review only catches obvious bugs
**Answer: D** — Expertise is not omniscience; review catches what one mind misses.

---

## Question 2: Building a Review Checklist
Design a checklist for reviewing AI model code. What five categories matter most?
- B. Correctness (logic sound?), testing (new tests added?), performance (will it scale?), documentation (future-readable?), reproducibility (can we rerun with same results?)—these catch the bugs that sink ML projects- C. Just check if it runs- D. Only check for syntax errors- A. Review checklists are unnecessary
**Answer: B** — Checklists transform review from arbitrary to systematic.

---

## Question 3: The Tone Problem
A reviewer comments: "This code is awful. Why would anyone write it this way?" The author becomes defensive. How should the review have been framed?
- B. Same feedback, different tone: "I see why you wrote it this way. Could we consider this alternative because it would handle edge cases better?" Kindness + clarity preserves collaboration- D. Never give critical feedback- C. Feedback doesn't matter; only the code matters- A. Reviewers should be blunt
**Answer: B** — Tone is as important as content in collaborative review.

---

## Question 4: Testing Before Approval
A PR adds a new feature but includes zero new tests. The code logic looks correct. Should you approve? What message does approval send?
- C. Don't approve—new features without tests will break later when they're modified; approving teaches the team that testing is optional—decline and request tests- B. Approve; testing is the developer's problem- A. Approve; trust that it works- D. Tests aren't reviewable concerns
**Answer: C** — Standards enforcement prevents tech debt accumulation.

---

## Question 5: Handling Disagreement in Review
You request changes; the author responds with technical reasons why their approach is better. You're not fully convinced but not certain they're wrong. What's the right move?
- D. Have a real discussion; if they make a coherent case and risks are manageable, approve with notation ("Approved with concerns, noted for future monitoring"); trust trumps uniformity- A. Reject indefinitely- B. Approve immediately to end the conversation- C. Escalate to management
**Answer: D** — Review is dialogue, not autocracy.

---

## Question 6: Large PR Red Flags
A 1,500-line PR hits your queue. What immediate red flags suggest asking for a split, rather than trudging through the review?
- D. Multiple objectives in one PR (refactoring + new feature), deep nesting of changes (hard to test in isolation), long review time (>1 hour estimated)—large reviews hide problems in noise- C. Large PRs are fine; review them anyway- A. PR size never matters- B. Developers are always right about PR structure
**Answer: D** — PR size reflects decomposition quality.

---

## Question 7: Edge Case Spotting
A colleague's PR implements a new data preprocessing step. The code handles normal cases well but doesn't check for empty arrays, NaN values, or mismatched dimensions. How should you frame this?
- A. Request edge case handling: "I see handling for the happy path. What about when datasets are empty or corrupted? These cases will appear in production." This forces thinking about robustness.- B. Don't mention edge cases- C. Assume edge cases won't happen- D. Let it break in production
**Answer: A** — Production teaches harsh lessons; review prevents them.

---

## Question 8: Performance Review
A PR adds a feature. Your rough analysis suggests the added code has O(n²) complexity and will slow model training by 5% on 1M samples. The author says, "It's fine; we're not at that scale yet." How should this be resolved?
- A. Request optimization or documentation of the performance trade-off; leaving known performance cliffs unmarked sets up future surprises; if optimization is truly post-poned, document it explicitly- C. Approve anyway- B. Performance isn't reviewable- D. Ignore the issue
**Answer: A** — Known problems are easier to fix than surprise problems.

---

## Question 9: Documentation as Reviewable
A complex algorithm is implemented with no comments. The code is correct but requires reading carefully to understand. Is this a blocker for approval?
- C. Yes—in AI projects where multiple researchers modify the same model code, undocumented complexity becomes a debugging nightmare; request comments explaining the algorithm's purpose and non-obvious design choices- B. No; if the code runs, it's fine- D. Comments are optional- A. Code should be self-explanatory; comments are cheating
**Answer: C** — Documentation is an investment in team maintenance burden.

---

## Question 10: Rapid Iteration vs Careful Review
Your team operates with strict code review, but someone complains: "Review takes 3 days; we could iterate faster without it." How do you explain the long-term trade-off?
- A. 3 days of review per feature prevents 5-10 days of debugging later when reviewed code breaks production; the upfront time investment saves total time and reduces risk—measure defect escape rate before and after review- B. Drop code review for speed- C. Review speed doesn't matter to outcomes- D. Slow review is inefficient
**Answer: A** — Review is insurance against expensive failures.
