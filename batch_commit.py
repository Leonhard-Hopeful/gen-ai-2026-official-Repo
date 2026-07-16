import os
import subprocess
from pathlib import Path

os.chdir(r"c:\Users\THE EYE INFORMATIQUE\OneDrive\Desktop\gen-ai-full-course")

# List of all kawood files grouped by section for logical commits
sections = {
    "Git VCS": [
        "0.0_git_vcs/1_beginner/1_git_basics/kawood.md",
        "0.0_git_vcs/1_beginner/2_versioning_workflows/kawood.md",
        "0.0_git_vcs/1_beginner/3_collaboration/kawood.md",
        "0.0_git_vcs/2_intermediate/1_branching_merging/kawood.md",
        "0.0_git_vcs/2_intermediate/2_workflows/kawood.md",
        "0.0_git_vcs/2_intermediate/3_code_review/kawood.md",
        "0.0_git_vcs/3_advanced/1_advanced_rebase/kawood.md",
        "0.0_git_vcs/3_advanced/2_git_for_ai_projects/kawood.md",
        "0.0_git_vcs/3_advanced/3_release_management/kawood.md",
    ],
    "Environment Setup": [
        "0.1_env_setup/1_beginner/1_python_setup/kawood.md",
        "0.1_env_setup/1_beginner/2_virtualenv_basics/kawood.md",
        "0.1_env_setup/1_beginner/3_ide_tools/kawood.md",
        "0.1_env_setup/2_intermediate/1_environment_management/kawood.md",
        "0.1_env_setup/2_intermediate/2_dependency_management/kawood.md",
        "0.1_env_setup/2_intermediate/3_containerization_basics/kawood.md",
        "0.1_env_setup/3_advanced/1_reproducible_pipelines/kawood.md",
        "0.1_env_setup/3_advanced/2_ai_devops/kawood.md",
        "0.1_env_setup/3_advanced/3_scaling_environments/kawood.md",
    ],
    "Python Programming": [
        "1.1_python_programming/1_beginner/1_variables/kawood.md",
        "1.1_python_programming/1_beginner/2_data_types/kawood.md",
        "1.1_python_programming/1_beginner/3_control_flow/kawood.md",
        "1.1_python_programming/2_intermediate/1_data_structures/kawood.md",
        "1.1_python_programming/2_intermediate/2_functions/kawood.md",
        "1.1_python_programming/2_intermediate/3_modules_packages/kawood.md",
        "1.1_python_programming/3_advanced/1_testing_debugging/kawood.md",
        "1.1_python_programming/3_advanced/2_performance/kawood.md",
        "1.1_python_programming/3_advanced/3_automation_scripts/kawood.md",
    ],
    "OOP for AI": [
        "1.2_oop_for_ai/1_beginner/1_classes_objects/kawood.md",
        "1.2_oop_for_ai/1_beginner/2_attributes_methods/kawood.md",
        "1.2_oop_for_ai/1_beginner/3_inheritance/kawood.md",
        "1.2_oop_for_ai/2_intermediate/1_polymorphism/kawood.md",
        "1.2_oop_for_ai/2_intermediate/2_composition/kawood.md",
        "1.2_oop_for_ai/2_intermediate/3_design_patterns/kawood.md",
        "1.2_oop_for_ai/3_advanced/1_metaprogramming/kawood.md",
        "1.2_oop_for_ai/3_advanced/2_model_architecture/kawood.md",
        "1.2_oop_for_ai/3_advanced/3_scalable_design/kawood.md",
    ],
    "Mathematics for AI": [
        "1.3_mathematics_for_ai/1_beginner/1_vectors_scalars/kawood.md",
        "1.3_mathematics_for_ai/1_beginner/2_linear_equations/kawood.md",
        "1.3_mathematics_for_ai/1_beginner/3_basic_statistics/kawood.md",
        "1.3_mathematics_for_ai/2_intermediate/1_matrices/kawood.md",
        "1.3_mathematics_for_ai/2_intermediate/2_calculus/kawood.md",
        "1.3_mathematics_for_ai/2_intermediate/3_probability/kawood.md",
        "1.3_mathematics_for_ai/3_advanced/1_advanced_linear_algebra/kawood.md",
        "1.3_mathematics_for_ai/3_advanced/2_advanced_calculus/kawood.md",
        "1.3_mathematics_for_ai/3_advanced/3_advanced_probability/kawood.md",
    ],
}

commit_count = 1
for section, files in sections.items():
    # Commit each file individually for 30 commits
    for file in files:
        file_path = file.replace("/", "\\")
        subprocess.run(["git", "add", file_path], check=True)
        topic = file.split("/")[-2]
        level = file.split("/")[-3]
        subprocess.run(["git", "commit", "-m", f"Randomize answer choices in {section} - {level}/{topic} kawood"], check=True)
        commit_count += 1

print(f"Completed {commit_count - 1} commits")
