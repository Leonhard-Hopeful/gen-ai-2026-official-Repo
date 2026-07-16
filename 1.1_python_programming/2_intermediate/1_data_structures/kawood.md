# Kawood Mastery Challenge — Data Structures

Master lists, tuples, sets, and dictionaries to organize complex information efficiently in Python.

## Question 1: When to Use Lists vs Tuples
You need a collection of settings: learning rate, batch size, epochs. Lists or tuples? Explain the trade-off.
- C. Tuples—settings shouldn't change after initialization; tuples enforce immutability and signal intent (use this config, don't modify it); lists would allow accidental mutation- D. Always use lists- B. They're interchangeable- A. Tuples are always better
**Answer: C** — Immutability signals intent and prevents bugs.

---

## Question 2: Dictionary Efficiency
You have 10,000 users. To find user 5000's data, would you use a list (search O(n)) or dictionary (lookup O(1))? Why does this matter?
- B. Dictionary is 10,000x faster—list searches linearly, dict hashes to find instantly; in AI with millions of samples, linear search is unusable; dict scales to billion-item datasets- D. Both are equally fast- A. Lists are always better- C. Efficiency doesn't matter
**Answer: B** — Dictionary lookup is constant-time magic.

---

## Question 3: Set Use Cases
You receive user IDs from two data sources. Some overlap. You need unique IDs across both. List or set? Why?
- D. Set—`set(source1) | set(source2)` gives union in O(n), automatically deduplicates; lists would require manual deduplication O(n²) with nested loops—sets are designed for uniqueness operations- A. Lists can do the same- C. Either approach is equivalent- B. Sets are just for storing numbers
**Answer: D** — Sets are uniqueness engines.

---

## Question 4: Nested Data Structure Design
Your model config has layers with hyperparameters. You might need to query "all learning rates" across all layers. How would you structure this?
- C. Dict of dicts: `{"layer_1": {"lr": 0.001}, "layer_2": {"lr": 0.0001}}` —this enables direct access (config["layer_1"]["lr"]) and easy traversal—alternative nested lists would require indexing magic- D. Flat list of all hyperparameters- A. One large tuple- B. No structure; just strings
**Answer: C** — Nested dicts mirror domain structure.

---

## Question 5: List Comprehension Power
To extract all odd numbers from 1 to 100, you could write a for loop with append, or use: `[x for x in range(1, 101) if x % 2 == 1]`. What advantage does the second have?
- A. Concise, readable, faster (compiled efficiently), more Pythonic—comprehensions express intent (collect odd numbers) rather than mechanics (append in a loop)—experienced Python developers expect comprehensions- B. They're equivalent- D. Loops are clearer- C. Comprehensions are slower
**Answer: A** — Comprehensions are idiomatic Python.

---

## Question 6: Tuple Unpacking in Functions
Your function returns `(accuracy, precision, recall)`. Calling code does: `metrics = evaluate(model)`. Later: `print(metrics[0])`. How would a Pythonista write it instead?
- C. `accuracy, precision, recall = evaluate(model)` then `print(accuracy)`—unpacking immediately assigns names, making code readable; indexing obscures what metrics[0] means- B. Keep using indices- D. Store in dict instead of tuple- A. Unpacking is overcomplicating
**Answer: C** — Unpacking makes intent explicit.

---

## Question 7: Mutability Gotcha
You create a list of lists: `matrix = [[0]*3 for _ in range(3)]` (correct) vs `matrix = [[0]*3]*3` (trap). The second creates three references to the SAME list. If you modify matrix[0][0], what happens?
- A. All three rows change—the second approach makes three references to one list in memory; modifying through one reference modifies all—this is a subtle Python gotcha that causes hours of debugging- D. Only matrix[0] changes- B. Each row is independent- C. This is impossible in Python
**Answer: A** — Shared references are a mutation trap.

---

## Question 8: Dictionary Key Constraints
You try to use a list as a dictionary key: `my_dict[[1, 2, 3]] = "value"`. It fails. Why?
- D. Lists are mutable—dictionary keys must be hashable (immutable); lists can change, making the key's identity unstable—if a key changes after insertion, it breaks the dictionary's internal hash structure; use tuples instead- C. Dicts don't support list keys- A. This is a Python error- B. You need special syntax
**Answer: D** — Hashability is a dictionary requirement.

---

## Question 9: Set Operations for Model Evaluation
You have two sets: `predicted = {1, 3, 5, 7}` and `actual = {1, 2, 3, 4, 5}`. Compute: true positives (both), false positives (predicted but not actual), false negatives (actual but not predicted).
- C. TP: `predicted & actual` (intersection) = {1, 3, 5}, FP: `predicted - actual` (difference) = {7}, FN: `actual - predicted` = {2, 4}—set operations directly implement confusion matrix calculations- B. Compute manually by iteration- A. Use lists instead- D. Set operations can't help
**Answer: C** — Sets are confusion matrix calculators.

---

## Question 10: Choosing Data Structure at Scale
You're building a recommendation system. You need fast lookups (user ID → preferences), maintain insertion order (to replay history), and check membership (has user been recommended model X?). Which structures combine?
- C. Dict (fast lookup) for user preferences, list (ordered) for history, set (membership test O(1)) for recommendations—combine structures for different access patterns; no single structure does everything- A. Single list for everything- B. Single dict for everything- D. One structure must suffice
**Answer: C** — Data structure polyglotism solves complex access patterns.
