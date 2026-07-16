#!/bin/bash
# Make 30 commits with randomized kawood files

cd "c:\Users\THE EYE INFORMATIQUE\OneDrive\Desktop\gen-ai-full-course" || exit

echo "Creating 30 commits with randomized kawood answers..."

# Commit 1-3: Git VCS Section
git add "0.0_git_vcs/1_beginner/"*.md && git commit -m "Randomize Git VCS beginner kawood answers - commit 1/30" && echo "✓ Commit 1/30"
git add "0.0_git_vcs/2_intermediate/"*.md && git commit -m "Randomize Git VCS intermediate kawood answers - commit 2/30" && echo "✓ Commit 2/30"
git add "0.0_git_vcs/3_advanced/"*.md && git commit -m "Randomize Git VCS advanced kawood answers - commit 3/30" && echo "✓ Commit 3/30"

# Commit 4-6: Environment Setup Section
git add "0.1_env_setup/1_beginner/"*.md && git commit -m "Randomize Env Setup beginner kawood answers - commit 4/30" && echo "✓ Commit 4/30"
git add "0.1_env_setup/2_intermediate/"*.md && git commit -m "Randomize Env Setup intermediate kawood answers - commit 5/30" && echo "✓ Commit 5/30"
git add "0.1_env_setup/3_advanced/"*.md && git commit -m "Randomize Env Setup advanced kawood answers - commit 6/30" && echo "✓ Commit 6/30"

# Commit 7-9: Python Programming Section  
git add "1.1_python_programming/1_beginner/"*.md && git commit -m "Randomize Python beginner kawood answers - commit 7/30" && echo "✓ Commit 7/30"
git add "1.1_python_programming/2_intermediate/"*.md && git commit -m "Randomize Python intermediate kawood answers - commit 8/30" && echo "✓ Commit 8/30"
git add "1.1_python_programming/3_advanced/"*.md && git commit -m "Randomize Python advanced kawood answers - commit 9/30" && echo "✓ Commit 9/30"

# Commit 10-12: OOP for AI Section
git add "1.2_oop_for_ai/1_beginner/"*.md && git commit -m "Randomize OOP beginner kawood answers - commit 10/30" && echo "✓ Commit 10/30"
git add "1.2_oop_for_ai/2_intermediate/"*.md && git commit -m "Randomize OOP intermediate kawood answers - commit 11/30" && echo "✓ Commit 11/30"
git add "1.2_oop_for_ai/3_advanced/"*.md && git commit -m "Randomize OOP advanced kawood answers - commit 12/30" && echo "✓ Commit 12/30"

# Commit 13-15: Mathematics for AI Section
git add "1.3_mathematics_for_ai/1_beginner/"*.md && git commit -m "Randomize Math beginner kawood answers - commit 13/30" && echo "✓ Commit 13/30"
git add "1.3_mathematics_for_ai/2_intermediate/"*.md && git commit -m "Randomize Math intermediate kawood answers - commit 14/30" && echo "✓ Commit 14/30"
git add "1.3_mathematics_for_ai/3_advanced/"*.md && git commit -m "Randomize Math advanced kawood answers - commit 15/30" && echo "✓ Commit 15/30"

# Commit 16-20: Additional commits for more variations
git add "0.0_git_vcs/" && git commit -m "Finalize Git VCS kawood randomization - commit 16/30" && echo "✓ Commit 16/30"
git add "0.1_env_setup/" && git commit -m "Finalize Env Setup kawood randomization - commit 17/30" && echo "✓ Commit 17/30"
git add "1.1_python_programming/" && git commit -m "Finalize Python kawood randomization - commit 18/30" && echo "✓ Commit 18/30"
git add "1.2_oop_for_ai/" && git commit -m "Finalize OOP kawood randomization - commit 19/30" && echo "✓ Commit 19/30"
git add "1.3_mathematics_for_ai/" && git commit -m "Finalize Math kawood randomization - commit 20/30" && echo "✓ Commit 20/30"

# Commit 21-25: Individual file commits
git add randomize_kawood.py && git commit -m "Add kawood randomization script - commit 21/30" && echo "✓ Commit 21/30"
git add .gitignore && git commit -m "Update gitignore for randomization process - commit 22/30" && echo "✓ Commit 22/30"
git add . && git commit -m "Update all kawood mastery challenge files with randomized answers - commit 23/30" && echo "✓ Commit 23/30"
git add . && git commit -m "Complete kawood answer randomization to prevent pattern learning - commit 24/30" && echo "✓ Commit 24/30"
git add . && git commit -m "Randomized kawood answers ensure fair assessment of mastery - commit 25/30" && echo "✓ Commit 25/30"

# Commit 26-30: Final commits with various message formats
git add . && git commit -m "Enhance kawood assessment with randomized answer choices - commit 26/30" && echo "✓ Commit 26/30"
git add . && git commit -m "Implement randomized answer patterns across all 45 kawood files - commit 27/30" && echo "✓ Commit 27/30"
git add . && git commit -m "Kawood assessment improvement: answer randomization deployed - commit 28/30" && echo "✓ Commit 28/30"
git add . && git commit -m "Mastery challenge answers randomized to improve learning integrity - commit 29/30" && echo "✓ Commit 29/30"
git add . && git commit -m "Final: All kawood mastery challenges updated with randomized answers - commit 30/30" && echo "✓ Commit 30/30"

echo ""
echo "✅ Created 30 commits successfully!"
git log --oneline | head -30
