from pathlib import Path

root = Path(__file__).resolve().parent.parent
sections = {
    '0.0_git_vcs': ['1_beginner', '2_intermediate', '3_advanced'],
    '0.1_env_setup': ['1_beginner', '2_intermediate', '3_advanced'],
    '1.1_python_programming': ['1_beginner', '2_intermediate', '3_advanced'],
    '1.2_oop_for_ai': ['1_beginner', '2_intermediate', '3_advanced'],
    '1.3_mathematics_for_ai': ['1_beginner', '2_intermediate', '3_advanced'],
}

meta = {
    'git_basics': {
        'title': 'Git Basics',
        'overview': 'Learn the core Git commands and workflows that every AI developer uses to track code changes, collaborate safely, and recover from mistakes.',
        'key_points': ['Repository initialization and cloning', 'Commit lifecycle and atomic changes', 'Inspecting status and diffs', 'Browsing history and log'],
        'example': 'git init\ngit add .\ngit commit -m "first draft"',
        'questions': ['What does `git commit` do?', 'Why is `git status` useful?', 'When should you create a new repository?']
    },
    'versioning_workflows': {
        'title': 'Versioning Workflows',
        'overview': 'Understand working tree states, branching strategies, and how to structure Git history so teams and learners can evolve AI projects cleanly.',
        'key_points': ['Branch vs main and why branches exist', 'Feature branches and isolated work', 'Commit hygiene and meaningful messages', 'Merge strategies and clean history'],
        'example': 'git checkout -b feature/prompt-engineering',
        'questions': ['What is a feature branch?', 'Why avoid large merge commits?', 'How does a good commit message help?']
    },
    'collaboration': {
        'title': 'Collaboration with Git',
        'overview': 'Discover how to use remotes, pull requests, code review, and shared repositories to turn individual work into team learning.',
        'key_points': ['Adding and using remotes', 'Push and pull workflows', 'Creating and reviewing pull requests', 'Resolving merge conflicts politely'],
        'example': 'git push origin feature/lesson-plan',
        'questions': ['What makes a good pull request description?', 'How can you resolve merge conflicts in Git?']
    },
    'branching_merging': {
        'title': 'Branching and Merging',
        'overview': 'Master branch management so you can prototype AI ideas safely and merge improvements back into the main timeline with confidence.',
        'key_points': ['Creating and switching branches', 'Fast-forward vs merge commits', 'Three-way merges and conflict handling', 'Keeping branches small and focused'],
        'example': 'git merge feature/optimization',
        'questions': ['When does Git perform a fast-forward merge?', 'How should you handle a conflict?']
    },
    'workflows': {
        'title': 'Git Workflows for Teams',
        'overview': 'Compare Git workflows like GitHub Flow, GitLab Flow, and trunk-based development for AI projects that grow in complexity.',
        'key_points': ['Feature branch workflow', 'Trunk-based development', 'Release branches and hotfixes', 'Continuous integration hooks'],
        'example': 'main <- feature <- hotfix',
        'questions': ['What is trunk-based development?', 'Why choose a workflow for your team?']
    },
    'code_review': {
        'title': 'Code Review and Quality',
        'overview': 'Use code review as a learning tool, not just a gate: write clear change descriptions, comment productively, and build trust together.',
        'key_points': ['Review checklist', 'Review etiquette', 'Testing before approval', 'Small focused changes'],
        'example': 'Create a pull request and ask peers to review model evaluation pipeline changes.',
        'questions': ['What should a review focus on first?', 'How can you give constructive feedback?']
    },
    'advanced_rebase': {
        'title': 'Advanced Rebase',
        'overview': 'Learn when and how to rewrite history safely with rebase, including squashing commits and cleaning local feature branches.',
        'key_points': ['Interactive rebase', 'Squashing commits', 'Rebase vs merge', 'Avoiding public history rewrites'],
        'example': 'git rebase -i main',
        'questions': ['Why should you avoid rebasing shared branches?', 'What does squash do in an interactive rebase?']
    },
    'git_for_ai_projects': {
        'title': 'Git for AI Projects',
        'overview': 'Learn Git patterns specifically for AI code, data pipelines, model checkpoints, and experiment tracking.',
        'key_points': ['Large file handling', 'Experiment branches', 'Data versioning', 'Model artifact hygiene'],
        'example': 'Use `.gitignore` for data and add a `README.md` describing model experiments.',
        'questions': ['How do you keep model checkpoints out of Git?', 'What changes when versioning datasets instead of code?']
    },
    'release_management': {
        'title': 'Release Management',
        'overview': 'Structure product releases, tags, and version numbering so your AI course assets and software can be published professionally.',
        'key_points': ['Semantic versioning', 'Git tags and releases', 'Release notes formatting', 'Stable and prerelease branches'],
        'example': 'git tag -a v1.0.0 -m "First stable course release"',
        'questions': ['What are the three parts of semantic versioning?', 'Why keep release notes concise?']
    },
    'python_setup': {
        'title': 'Python Setup',
        'overview': 'Install Python and set up the basic development environment to run AI code with clarity and consistency.',
        'key_points': ['Choosing a Python version', 'Installing Python', 'PATH and version checks', 'pip basics'],
        'example': 'python -m pip install --upgrade pip',
        'questions': ['Why keep Python updated?', 'What is `pip` used for?']
    },
    'virtualenv_basics': {
        'title': 'Virtual Environments',
        'overview': 'Isolate projects with virtual environments so libraries do not conflict and learners can reproduce the setup easily.',
        'key_points': ['Creating venv', 'Activating environments', 'Installing packages locally', 'Saving requirements'],
        'example': 'python -m venv .venv\nsource .venv/Scripts/activate',
        'questions': ['Why use virtual environments?', 'How do you save installed packages?']
    },
    'ide_tools': {
        'title': 'IDE and Editor Tools',
        'overview': 'Choose and configure editors and tools that make Python and AI development fast, readable, and beginner-friendly.',
        'key_points': ['Editor shortcuts', 'Linting and formatting', 'Debugger support', 'Notebooks and previews'],
        'example': 'Open the course folder in VS Code and install the Python extension.',
        'questions': ['What makes an IDE helpful for beginners?', 'How does linting improve code quality?']
    },
    'environment_management': {
        'title': 'Environment Management',
        'overview': 'Manage multiple Python environments and switch between course projects without breaking dependency boundaries.',
        'key_points': ['pyenv and conda basics', 'Per-project environments', 'Dependency isolation', 'Reproducibility practices'],
        'example': 'conda create -n ai-course python=3.11',
        'questions': ['What is the advantage of using `pyenv`?', 'When should you use containers for development?']
    },
    'dependency_management': {
        'title': 'Dependency Management',
        'overview': 'Keep packages organized and reproducible for course work using requirements files, lockfiles, and dependency review.',
        'key_points': ['requirements.txt', 'pip freeze', 'version pinning', 'dependency conflict resolution'],
        'example': 'pip freeze > requirements.txt',
        'questions': ['Why pin package versions?', 'What does a lockfile solve?']
    },
    'containerization_basics': {
        'title': 'Containerization Basics',
        'overview': 'Use lightweight containers to define reproducible environments for AI development and sharing the course setup.',
        'key_points': ['Dockerfile basics', 'Build and run images', 'Image layers', 'Local reproducibility'],
        'example': 'docker build -t ai-course .',
        'questions': ['What is a Docker image?', 'Why use containers for teaching AI?']
    },
    'reproducible_pipelines': {
        'title': 'Reproducible Pipelines',
        'overview': 'Design dependable workflows that produce the same results every time, from environment setup to model evaluation.',
        'key_points': ['Scripted setup', 'Stable environments', 'Data pipeline automation', 'Testing and validation'],
        'example': 'Create a `setup.sh` or `Makefile` for environment setup.',
        'questions': ['What is the value of an automated setup script?', 'How do reproducible pipelines help teams?']
    },
    'ai_devops': {
        'title': 'AI DevOps',
        'overview': 'Bridge development and operations for AI systems by tracking experiments, automating workflows, and deploying responsibly.',
        'key_points': ['CI/CD basics', 'Monitoring model quality', 'Data and model drift', 'Pipeline orchestration'],
        'example': 'Set up a CI workflow that runs tests and lint checks on every push.',
        'questions': ['What should a CI pipeline verify for AI code?', 'Why monitor deployed models?']
    },
    'scaling_environments': {
        'title': 'Scaling Environments',
        'overview': 'Expand from a laptop setup to scalable cloud and team-ready environments for larger AI experiments.',
        'key_points': ['Cloud development workspaces', 'GPU support', 'Shared developer environments', 'Cost-aware scaling'],
        'example': 'Use a remote environment or cloud notebook for larger model training.',
        'questions': ['When is cloud development preferable to local?', 'How can teams share a consistent environment?']
    },
    'variables': {
        'title': 'Variables and Assignment',
        'overview': 'Learn how Python stores values in named variables and how to use them as the foundation for every program.',
        'key_points': ['Assignment statements', 'Naming conventions', 'Mutable vs immutable values', 'Basic types in variables'],
        'example': 'message = "Hello AI"\ncount = 3\nprint(message, count)',
        'questions': ['What is a variable?', 'Why are clear names important in code?']
    },
    'data_types': {
        'title': 'Python Data Types',
        'overview': 'Understand the basic data types in Python and how each type shapes the way data is stored and manipulated.',
        'key_points': ['int, float, str, bool', 'Dynamic typing', 'Type conversion', 'Inspecting types'],
        'example': 'score = 95\npassed = score >= 50\nprint(type(score), type(passed))',
        'questions': ['Why distinguish between `int` and `float`?', 'What does `type()` tell you?']
    },
    'control_flow': {
        'title': 'Control Flow',
        'overview': 'Use conditionals and loops to make Python programs make decisions and repeat actions intelligently.',
        'key_points': ['if / elif / else', 'for loops', 'while loops', 'loop control with break/continue'],
        'example': 'score = 72\nif score >= 50:\n    print("pass")\nelse:\n    print("fail")',
        'questions': ['What is the difference between `for` and `while`?', 'When use `elif` instead of nested `if`?']
    },
    'data_structures': {
        'title': 'Data Structures',
        'overview': 'Explore lists, tuples, sets, and dictionaries to organize complex information in Python programs.',
        'key_points': ['Lists for ordered collections', 'Dictionaries for key-value data', 'Sets for uniqueness', 'Tuples for fixed groups'],
        'example': 'students = ["Ada", "Grace"]\nconfig = {"lr": 0.01}',
        'questions': ['When use a dictionary over a list?', 'What makes a tuple different from a list?']
    },
    'functions': {
        'title': 'Functions and Modular Code',
        'overview': 'Build reusable code blocks with functions that simplify AI pipelines and preserve design clarity.',
        'key_points': ['def syntax', 'arguments and return values', 'docstrings', 'calling functions'],
        'example': 'def greet(name):\n    """Return a greeting message."""\n    return f"Hello {name}!"',
        'questions': ['Why modularize code with functions?', 'How do default arguments help?']
    },
    'modules_packages': {
        'title': 'Modules and Packages',
        'overview': 'Structure Python projects with modules and packages so your AI course code remains maintainable and shareable.',
        'key_points': ['Import statements', 'Package layout', '__init__.py files', 'Reusing code across files'],
        'example': 'from math import sqrt\nprint(sqrt(16))',
        'questions': ['What is a Python package?', 'Why avoid circular imports?']
    },
    'testing_debugging': {
        'title': 'Testing and Debugging',
        'overview': 'Develop habits for catching bugs early, writing tests, and using debugging tools to understand program behavior.',
        'key_points': ['Assertions and unit tests', 'Debugging techniques', 'Reading error messages', 'Exception handling'],
        'example': 'assert add(2, 2) == 4',
        'questions': ['What is a unit test?', 'How do assertions help?']
    },
    'performance': {
        'title': 'Performance and Optimization',
        'overview': 'Analyze and improve Python performance with profiling, efficient data handling, and thoughtful algorithm choice.',
        'key_points': ['Profiling code', 'Efficient loops', 'Algorithmic complexity', 'Optimizing data structures'],
        'example': 'squares = [x*x for x in range(10)]',
        'questions': ['Why measure performance before optimizing?', 'What makes list comprehensions faster than loops?']
    },
    'automation_scripts': {
        'title': 'Automation Scripts',
        'overview': 'Turn manual tasks into reliable scripts so course workflows like data preparation and report generation run automatically.',
        'key_points': ['Script entry points', 'Argument parsing', 'Command-line tools', 'Automated tasks'],
        'example': 'if __name__ == "__main__":\n    print("Run as a script")',
        'questions': ['Why automate repetitive tasks?', 'What is the purpose of the main guard?']
    },
    'classes_objects': {
        'title': 'Classes and Objects',
        'overview': 'Meet the building block of object-oriented programming: classes define structure and objects bring them to life.',
        'key_points': ['Class syntax', 'Creating instances', 'The role of self', 'Constructors'],
        'example': 'class Student:\n    def __init__(self, name):\n        self.name = name',
        'questions': ['What is an object?', 'Why use classes?']
    },
    'attributes_methods': {
        'title': 'Attributes and Methods',
        'overview': 'Explore how classes store state in attributes and behavior in methods, making AI components reusable and readable.',
        'key_points': ['Instance attributes', 'Class attributes', 'Instance methods', 'Method calls'],
        'example': 'def greet(self):\n    print(f"Hello {self.name}")',
        'questions': ['What is the difference between an attribute and a method?', 'When use a class attribute?']
    },
    'inheritance': {
        'title': 'Inheritance',
        'overview': 'Create hierarchical relationships with inheritance so new AI components can extend existing behavior cleanly.',
        'key_points': ['Base classes', 'Derived classes', 'super()', 'Method overriding'],
        'example': 'class Model(BaseModel):\n    pass',
        'questions': ['How does inheritance promote reuse?', 'What is method overriding?']
    },
    'polymorphism': {
        'title': 'Polymorphism',
        'overview': 'Use polymorphism to write code that works with multiple object types through consistent interfaces.',
        'key_points': ['Duck typing', 'Common interfaces', 'Method interchangeability', 'Flexible design'],
        'example': 'for model in models:\n    model.predict(data)',
        'questions': ['What is duck typing?', 'Why is polymorphism useful?']
    },
    'composition': {
        'title': 'Composition',
        'overview': 'Build AI systems by combining objects rather than inheriting from them, enabling easier change and better modularity.',
        'key_points': ['Has-a relationships', 'Delegation', 'Object collaboration', 'Reusability'],
        'example': 'self.preprocessor = Preprocessor()',
        'questions': ['How is composition different from inheritance?', 'Why is composition often preferred?']
    },
    'design_patterns': {
        'title': 'Design Patterns',
        'overview': 'Learn reusable object-oriented patterns like factory and adapter that solve common AI architecture problems elegantly.',
        'key_points': ['Factory pattern', 'Strategy pattern', 'Adapter pattern', 'Why patterns matter'],
        'example': 'def model_factory(name):\n    if name == "linear":\n        return LinearModel()',
        'questions': ['What problem does the strategy pattern solve?', 'When do you use a factory?']
    },
    'metaprogramming': {
        'title': 'Metaprogramming',
        'overview': 'Explore Python metaprogramming techniques that let you generate classes, modify behavior, and build higher-level frameworks.',
        'key_points': ['Decorators', 'Metaclasses', 'Dynamic attributes', 'Reflection'],
        'example': '@dataclass\nclass Config: ...',
        'questions': ['What is a decorator?', 'When use metaclasses?']
    },
    'model_architecture': {
        'title': 'Model Architecture',
        'overview': 'Design AI model classes that encapsulate data flow, training loops, and evaluation in a clean, maintainable package.',
        'key_points': ['Model interfaces', 'Training loops', 'Prediction APIs', 'Separation of concerns'],
        'example': 'class NeuralModel:\n    def train(self, data): ...',
        'questions': ['What should a model class own?', 'Why separate training and prediction?']
    },
    'scalable_design': {
        'title': 'Scalable Design',
        'overview': 'Architect AI software for scale, making it easier to extend components and support larger datasets or teams.',
        'key_points': ['Modular package structure', 'Clean APIs', 'Configuration objects', 'Service boundaries'],
        'example': 'organize code into `data`, `models`, and `evaluation` packages',
        'questions': ['How does modular design help growth?', 'What is a clean API?']
    },
    'vectors_scalars': {
        'title': 'Vectors and Scalars',
        'overview': 'Understand the core mathematical objects of AI: scalars for magnitude and vectors for direction and data representation.',
        'key_points': ['Scalars and vectors', 'Vector notation', 'Vector magnitude', 'Coordinate systems'],
        'example': 'vector = [3, 4]  # length is 5',
        'questions': ['How compute vector magnitude?', 'Why are vectors essential in AI?']
    },
    'linear_equations': {
        'title': 'Linear Equations',
        'overview': 'Master linear equations and systems, which underpin regression, dimensionality reduction, and many machine learning algorithms.',
        'key_points': ['Equation form', 'Solutions of linear equations', 'Slope-intercept form', 'Applied linear models'],
        'example': 'y = 2*x + 1',
        'questions': ['What is a solution to a linear equation?', 'How does a line represent a linear model?']
    },
    'basic_statistics': {
        'title': 'Basic Statistics',
        'overview': 'Build statistical intuition with mean, median, variance, and distributions so learners can interpret data effectively.',
        'key_points': ['Central tendency', 'Spread of data', 'Outliers', 'Simple distributions'],
        'example': 'mean = sum(values) / len(values)',
        'questions': ['How does variance measure spread?', 'What does a histogram show?']
    },
    'matrices': {
        'title': 'Matrices',
        'overview': 'Learn matrices as 2D arrays that encode data, transformations, and linear maps used throughout AI and deep learning.',
        'key_points': ['Matrix shape', 'Matrix multiplication', 'Transpose', 'Identity matrix'],
        'example': 'A = [[1, 2], [3, 4]]',
        'questions': ['How do you multiply matrices?', 'What is the identity matrix?']
    },
    'calculus': {
        'title': 'Calculus Foundations',
        'overview': 'Understand derivatives and gradients, the calculus concepts that power optimization and training in machine learning.',
        'key_points': ['Derivative meaning', 'Gradient', 'Chain rule', 'Rate of change'],
        'example': 'd/dx x**2 = 2*x',
        'questions': ['What is a gradient?', 'Why does optimization use derivatives?']
    },
    'probability': {
        'title': 'Probability',
        'overview': 'Build probability intuition for uncertainty, random events, distributions, and how AI makes predictions under uncertainty.',
        'key_points': ['Probability rules', 'Events and outcomes', 'Discrete vs continuous', 'Conditional probability'],
        'example': 'P(A or B) = P(A) + P(B) - P(A and B)',
        'questions': ['What does conditional probability describe?', 'How do distributions model uncertainty?']
    },
    'linear_algebra': {
        'title': 'Advanced Linear Algebra',
        'overview': 'Dive deeper into eigenvalues, eigenvectors, and matrix decompositions that make higher-level AI math possible.',
        'key_points': ['Eigenvalues and eigenvectors', 'Matrix rank', 'Inverse matrices', 'Linear independence'],
        'example': 'A @ v == lambda * v',
        'questions': ['What does an eigenvector represent?', 'Why is matrix rank important?']
    },
    'optimization': {
        'title': 'Optimization',
        'overview': 'Learn optimization methods such as gradient descent and how they help AI systems find the best solution iteratively.',
        'key_points': ['Objective functions', 'Gradient descent', 'Learning rate', 'Convergence'],
        'example': 'w = w - lr * gradient',
        'questions': ['What is a loss function?', 'How does learning rate affect training?']
    },
    'statistics_models': {
        'title': 'Statistical Models',
        'overview': 'Connect statistics to machine learning by studying models, inference, and how data informs predictions.',
        'key_points': ['Regression models', 'Likelihood', 'Inference', 'Model evaluation'],
        'example': 'y = beta0 + beta1*x + epsilon',
        'questions': ['What is a statistical model?', 'Why are confidence intervals useful?']
    }
}

exercise_prompts = {
    'git_basics': 'Initialize a local Git repository, add a file, commit it with a clear message, and explain the three file states in your own words.',
    'versioning_workflows': 'Create a branch and describe a simple workflow for developing a course module without disturbing main. Sketch the branch purpose.',
    'collaboration': 'Write the steps to clone a repository, pull the latest changes, and submit a pull request to a teammate.',
    'branching_merging': 'Create a branch, make a small change, and merge it back. Then explain a merge conflict scenario and how to resolve it.',
    'workflows': 'Compare GitHub Flow and trunk-based development in one sentence each, then choose which fits an AI course team and why.',
    'code_review': 'Draft a short code review checklist for reviewing another student’s AI code change.',
    'advanced_rebase': 'Perform an interactive rebase locally to squash two commits, then explain when it is safe to use rebase.',
    'git_for_ai_projects': 'Describe how you would manage model checkpoints and dataset versions in an AI repository.',
    'release_management': 'Outline a versioning scheme for a course release and create a sample release note entry.',
    'python_setup': 'Install Python, verify the version, and write one paragraph describing your environment setup steps.',
    'virtualenv_basics': 'Create, activate, and deactivate a virtual environment. Install one package and record the commands.',
    'ide_tools': 'Choose an editor, enable Python support, and list three features that help with your AI lesson development.',
    'environment_management': 'Create or describe a second isolated environment for a new AI project and explain why isolation matters.',
    'dependency_management': 'Install a package, freeze the environment, and explain the purpose of the generated requirements file.',
    'containerization_basics': 'Write a minimal Dockerfile for a Python project and explain why containers improve reproducibility.',
    'reproducible_pipelines': 'Create a simple shell or Python script that sets up the project dependencies and describe why it is reproducible.',
    'ai_devops': 'Sketch a CI pipeline for an AI course that runs tests and linting on every push.',
    'scaling_environments': 'Describe when a team should switch from a local environment to a cloud environment for AI development.',
    'variables': 'Declare three variables of different types and print a sentence using those variables.',
    'data_types': 'Identify types for several values and convert one integer to a string and one string to a number.',
    'control_flow': 'Write a program that prints "Pass" or "Fail" depending on a score using if/else.',
    'data_structures': 'Create a list of items, a dictionary of settings, and a set of unique values. Explain when each makes sense.',
    'functions': 'Write a function that computes the average of a list of numbers and include a docstring.',
    'modules_packages': 'Split a simple script into two modules and import one function from the other.',
    'testing_debugging': 'Introduce a bug into a simple function, use assertions to catch it, and then fix the bug.',
    'performance': 'Compare the runtime of two methods that do the same task and explain which is faster and why.',
    'automation_scripts': 'Write a small script that accepts a command-line argument and prints a message based on that argument.',
    'classes_objects': 'Define a class for an AI experiment with name and status, then create an instance and print its state.',
    'attributes_methods': 'Add a method to a class that updates its status and prints a summary message.',
    'inheritance': 'Create a base class and subclass it with one new method or property.',
    'polymorphism': 'Write a loop that calls the same method on two different object types and prints results.',
    'composition': 'Build a class that contains another object and uses it to perform a task.',
    'design_patterns': 'Choose one design pattern and explain how it helps structure code in an AI project.',
    'metaprogramming': 'Create a decorator that logs when a function runs and apply it to a simple function.',
    'model_architecture': 'Design a simple AI model class interface with train and predict methods.',
    'scalable_design': 'Outline a package structure for an AI project that separates data, models, and evaluation code.',
    'vectors_scalars': 'Define a vector and compute its magnitude using Python. Explain what the result means.',
    'linear_equations': 'Solve a simple linear equation manually and confirm the solution with Python.',
    'basic_statistics': 'Compute the mean, median, and variance for a small dataset in Python.',
    'matrices': 'Construct two small matrices and compute their product using Python or by hand.',
    'calculus': 'Differentiate a simple polynomial and explain the meaning of the slope at one point.',
    'probability': 'Calculate the probability of drawing a red ball from a bag with known colors.',
    'linear_algebra': 'Explain what an eigenvector is and compute a simple example for a 2x2 matrix.',
    'optimization': 'Write one step of gradient descent in pseudocode and describe how it changes the parameter.',
    'statistics_models': 'Describe a simple linear regression model and identify what the coefficients represent.'
}

kawood_options = {
    'git_basics': {'A': 'Track snapshots of file changes in the repository.', 'B': 'Deploy the project to production.', 'C': 'Install Git on a new machine.', 'D': 'Run code quality checks automatically.', 'correct': 'A'},
    'versioning_workflows': {'A': 'Plan how branches and commits flow through the team.', 'B': 'Encrypt repository files for security.', 'C': 'Automatically generate a release note.', 'D': 'Run unit tests before deployment.', 'correct': 'A'},
    'collaboration': {'A': 'Use remotes, pushes, and pull requests to work together.', 'B': 'Manage database migrations for shared data.', 'C': 'Train machine learning models collaboratively.', 'D': 'Archive old project folders.', 'correct': 'A'},
    'branching_merging': {'A': 'Combine work from two different branches safely.', 'B': 'Store large model files in Git.', 'C': 'Run branch performance tests.', 'D': 'Use a single main branch only.', 'correct': 'A'},
    'workflows': {'A': 'Choose a team process for handling feature development.', 'B': 'Write code review comments automatically.', 'C': 'Execute a Docker workflow.', 'D': 'Manage Python packages.', 'correct': 'A'},
    'code_review': {'A': 'Review small changes and share feedback before merge.', 'B': 'Publish code to a public website.', 'C': 'Create a new branch for each commit.', 'D': 'Delete merged branches immediately.', 'correct': 'A'},
    'advanced_rebase': {'A': 'Rewrite commit history to make it cleaner before sharing.', 'B': 'Delete old branches safely.', 'C': 'Resolve merge conflicts with a GUI tool.', 'D': 'Automatically generate release tags.', 'correct': 'A'},
    'git_for_ai_projects': {'A': 'Keep code and data versioning practices aligned with AI work.', 'B': 'Train AI models inside Git commits.', 'C': 'Use Git to store raw dataset files directly.', 'D': 'Deploy AI models with Git tags.', 'correct': 'A'},
    'release_management': {'A': 'Create a clear version and release note for users.', 'B': 'Optimize model performance for release.', 'C': 'Remove deprecated code automatically.', 'D': 'Track active users on release day.', 'correct': 'A'},
    'python_setup': {'A': 'Install Python and confirm the runtime environment.', 'B': 'Write the first AI algorithm in Python.', 'C': 'Deploy the Python app to the cloud.', 'D': 'Create a Git repository for Python code.', 'correct': 'A'},
    'virtualenv_basics': {'A': 'Isolate project libraries so dependencies do not conflict.', 'B': 'Install Python packages globally for all projects.', 'C': 'Run Python in a web browser.', 'D': 'Create a backup of your virtual environment.', 'correct': 'A'},
    'ide_tools': {'A': 'Use editor features like linting, debugging, and notebooks to code efficiently.', 'B': 'Install Python packages from the editor only.', 'C': 'Run a Python web server inside the IDE.', 'D': 'Use the editor to write only markdown files.', 'correct': 'A'},
    'environment_management': {'A': 'Manage separate environments for separate projects.', 'B': 'Install all tools globally with one command.', 'C': 'Use Git for environment management.', 'D': 'Store environment variables in the code.', 'correct': 'A'},
    'dependency_management': {'A': 'Track and pin package versions for reproducible installs.', 'B': 'Delete unused packages immediately.', 'C': 'Install packages from multiple sources without restrictions.', 'D': 'Use Docker instead of package managers.', 'correct': 'A'},
    'containerization_basics': {'A': 'Define a reproducible environment using containers.', 'B': 'Run Python scripts faster than native execution.', 'C': 'Store data files inside Git repositories.', 'D': 'Automatically scale AI models.', 'correct': 'A'},
    'reproducible_pipelines': {'A': 'Automate the same setup and training sequence reliably.', 'B': 'Build a pipeline that only runs once.', 'C': 'Push data directly to production without checks.', 'D': 'Use random settings for each experiment.', 'correct': 'A'},
    'ai_devops': {'A': 'Combine AI development and operations through pipelines and monitoring.', 'B': 'Build models only for deployment.', 'C': 'Store all experiments in Git branches.', 'D': 'Create frequent manual releases.', 'correct': 'A'},
    'scaling_environments': {'A': 'Expand development from local machines to shared cloud environments.', 'B': 'Only work on small datasets to avoid scaling issues.', 'C': 'Replace Python with a faster language when scaling.', 'D': 'Store all logs locally to reduce costs.', 'correct': 'A'},
    'variables': {'A': 'Store values under names so code can reuse them.', 'B': 'Run code inside variables automatically.', 'C': 'Use variables to control Git branches.', 'D': 'Encrypt data with Python variables.', 'correct': 'A'},
    'data_types': {'A': 'Use the right kind of data for correct operations in Python.', 'B': 'Store every value as text only.', 'C': 'Convert every value to a dictionary.', 'D': 'Use data types only in comments.', 'correct': 'A'},
    'control_flow': {'A': 'Make code choose different actions or repeat work.', 'B': 'Store data in loops permanently.', 'C': 'Only use code once per run.', 'D': 'Run code without conditions ever.', 'correct': 'A'},
    'data_structures': {'A': 'Organize data in lists, dictionaries, sets, or tuples depending on the need.', 'B': 'Always store data as text strings.', 'C': 'Use dictionaries for sequential indexing only.', 'D': 'Use tuples when data must change frequently.', 'correct': 'A'},
    'functions': {'A': 'Encapsulate reusable behavior and simplify code.', 'B': 'Make code run faster automatically.', 'C': 'Replace all comments with function names.', 'D': 'Store variables inside functions only.', 'correct': 'A'},
    'modules_packages': {'A': 'Break code into separate files and reuse it across the project.', 'B': 'Run code only from the root folder.', 'C': 'Use a package for each variable type.', 'D': 'Avoid importing any libraries.', 'correct': 'A'},
    'testing_debugging': {'A': 'Catch mistakes early with tests and use errors to understand problems.', 'B': 'Skip tests and fix bugs later.', 'C': 'Deploy code without checking it first.', 'D': 'Write tests only after the project is finished.', 'correct': 'A'},
    'performance': {'A': 'Measure and improve code efficiency using better tools and structures.', 'B': 'Write code as quickly as possible without checking speed.', 'C': 'Always use complex algorithms first.', 'D': 'Delay performance work until after deployment only.', 'correct': 'A'},
    'automation_scripts': {'A': 'Automate repetitive tasks with scripts so work is faster and less error-prone.', 'B': 'Run manual commands each time instead of scripts.', 'C': 'Use scripts only for documentation.', 'D': 'Avoid writing scripts in Python.', 'correct': 'A'},
    'classes_objects': {'A': 'Model real-world entities with classes and objects.', 'B': 'Store all code in one function.', 'C': 'Use classes only for GUIs.', 'D': 'Avoid objects in Python completely.', 'correct': 'A'},
    'attributes_methods': {'A': 'Give objects state and behavior with attributes and methods.', 'B': 'Store functions outside classes only.', 'C': 'Use attributes as separate functions.', 'D': 'Avoid defining methods altogether.', 'correct': 'A'},
    'inheritance': {'A': 'Share common behavior across related classes safely.', 'B': 'Duplicate code between classes for clarity.', 'C': 'Use inheritance for all data storage needs.', 'D': 'Avoid using any base class.', 'correct': 'A'},
    'polymorphism': {'A': 'Write code that works with different object types through a common interface.', 'B': 'Use the same variable names for all objects.', 'C': 'Convert all classes into functions.', 'D': 'Use a single class only for all tasks.', 'correct': 'A'},
    'composition': {'A': 'Combine objects to build complex systems without deep inheritance.', 'B': 'Use inheritance in every design.', 'C': 'Avoid objects and use only functions.', 'D': 'Store all dependencies in a global scope.', 'correct': 'A'},
    'design_patterns': {'A': 'Apply proven structures to solve common design problems.', 'B': 'Write design rules in comments only.', 'C': 'Use design patterns only for UI code.', 'D': 'Use patterns to avoid testing code.', 'correct': 'A'},
    'metaprogramming': {'A': 'Write code that can modify behavior or generate classes automatically.', 'B': 'Make code run without any functions.', 'C': 'Avoid decorators and dynamic features entirely.', 'D': 'Store program logic only in data files.', 'correct': 'A'},
    'model_architecture': {'A': 'Organize training and prediction behavior into a clean class interface.', 'B': 'Put all model code in one file only.', 'C': 'Use a class only for data storage.', 'D': 'Ignore design when building models.', 'correct': 'A'},
    'scalable_design': {'A': 'Design code so it can grow and adapt as the project expands.', 'B': 'Write code for only one small use case.', 'C': 'Avoid separating concerns in a large project.', 'D': 'Keep all configuration inside code comments.', 'correct': 'A'},
    'vectors_scalars': {'A': 'Represent data points and compute their size using vectors.', 'B': 'Use scalars only for strings.', 'C': 'Avoid vectors in AI entirely.', 'D': 'Store coordinates as booleans.', 'correct': 'A'},
    'linear_equations': {'A': 'Solve simple linear relationships that form the basis of many models.', 'B': 'Use equations only for algebra class.', 'C': 'Avoid equations in AI modeling.', 'D': 'Treat every function as non-linear.', 'correct': 'A'},
    'basic_statistics': {'A': 'Summarize data with mean, median, and spread to understand patterns.', 'B': 'Use random numbers only.', 'C': 'Ignore data distributions completely.', 'D': 'Always choose the same statistic for every dataset.', 'correct': 'A'},
    'matrices': {'A': 'Use matrices to represent and transform multi-dimensional data.', 'B': 'Store images as text instead of arrays.', 'C': 'Use matrices only for spreadsheets.', 'D': 'Avoid matrix multiplication in AI.', 'correct': 'A'},
    'calculus': {'A': 'Use derivatives and gradients to understand how values change in models.', 'B': 'Compute only integrals for AI training.', 'C': 'Ignore rates of change in learning.', 'D': 'Use calculus only for geometry problems.', 'correct': 'A'},
    'probability': {'A': 'Model uncertainty and event likelihood mathematically.', 'B': 'Treat random events as impossible.', 'C': 'Ignore probability when evaluating predictions.', 'D': 'Use probability only in games.', 'correct': 'A'},
    'linear_algebra': {'A': 'Work with eigenvectors, rank, and matrix structure for advanced AI math.', 'B': 'Avoid matrices in machine learning.', 'C': 'Use linear algebra only for graphics.', 'D': 'Never compute matrix inverses.', 'correct': 'A'},
    'optimization': {'A': 'Minimize loss functions by iteratively improving parameters.', 'B': 'Maximize errors on purpose.', 'C': 'Avoid gradients in training.', 'D': 'Use only brute-force search for all problems.', 'correct': 'A'},
    'statistics_models': {'A': 'Connect statistical ideas to predictive models and inference.', 'B': 'Treat models as purely deterministic formulas.', 'C': 'Use statistics only for plotting charts.', 'D': 'Ignore uncertainty in predictions.', 'correct': 'A'},
}


def write_lesson(path, data):
    lines = [
        f'# {data["title"]}',
        '',
        '## Overview',
        '',
        data['overview'],
        '',
        '## Why this matters',
        '',
        'This lesson explains a key concept and connects it to real AI course design and student success.',
        '',
        '## Key concepts',
        '',
    ]
    for point in data['key_points']:
        lines.append(f'- {point}')
    lines.extend([
        '',
        '## Example',
        '',
        '```python',
        data['example'],
        '```',
        '',
        '## Tutor guide',
        '',
        'Use this section to keep the lesson interactive and clear:',
        '',
        '- Explain the concept with a simple analogy.',
        '- Demonstrate code live and ask students to predict the result.',
        '- Ask learners to make one small modification.',
        '- Pause for questions and reinforce the main idea.',
        '',
        '### Tutor workflow',
        '',
        '1. Introduce the concept in 2-3 minutes.',
        '2. Open the lesson markdown and read the overview together.',
        '3. Run the example live or in the notebook.',
        '4. Encourage learners to write the same example with their own data.',
        '5. End with the review questions and connect to the next topic.',
        '',
        '## Reflection questions',
        '',
    ])
    for question in data['questions']:
        lines.append(f'- {question}')
    lines.append('')
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_exercises(path, title, topic_data):
    lines = [
        f'# Exercises — {title}',
        '',
        'Complete these challenges to strengthen your understanding and build confidence.',
        '',
    ]
    for idx, item in enumerate(topic_data, start=1):
        lines.extend([
            f'## {idx}. {item["title"]}',
            '',
            item['exercise'],
            '',
        ])
    lines.extend([
        '## Bonus exercise',
        'Create a short notebook or lesson outline that connects all three topics in this module. Include one real-world example and one teaching tip.',
        '',
    ])
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_kawood(path, title, topic_data):
    lines = [
        f'# Kawood Quiz — {title}',
        '',
        'Answer these multiple-choice questions to unlock the next course challenge.',
        '',
    ]
    for idx, item in enumerate(topic_data, start=1):
        lines.extend([
            f'## Question {idx}: {item["title"]}',
            '',
            f'Which statement best describes the primary purpose of {item["title"]}?',
            '',
            f'- A. {item["options"]["A"]}',
            f'- B. {item["options"]["B"]}',
            f'- C. {item["options"]["C"]}',
            f'- D. {item["options"]["D"]}',
            '',
            f'Answer: {item["correct_answer"]}',
            '',
        ])
    path.write_text('\n'.join(lines), encoding='utf-8')


def normalize_topic_key(directory_name):
    return directory_name.split('_', 1)[1] if '_' in directory_name else directory_name


for section, levels in sections.items():
    for level in levels:
        level_dir = root / section / level
        if not level_dir.exists():
            continue
        topic_dirs = [p for p in level_dir.iterdir() if p.is_dir() and p.name not in ('exercises', '__pycache__')]
        topic_data = []
        for topic_dir in sorted(topic_dirs, key=lambda p: p.name):
            key = normalize_topic_key(topic_dir.name)
            if key not in meta:
                print(f'Warning: missing metadata for topic {key} in {topic_dir}')
                continue
            data = meta[key]
            write_lesson(topic_dir / 'lesson.md', data)
            prompt = exercise_prompts.get(key, 'Practice the concept and describe what you learned.')
            options = kawood_options.get(key, {'A': 'Correct concept', 'B': 'Distractor', 'C': 'Distractor', 'D': 'Distractor', 'correct': 'A'})
            topic_data.append({'title': data['title'], 'exercise': prompt, 'options': options, 'correct_answer': options['correct']})
        if topic_data:
            title = f'{section.replace("_", " ").title()} {level.replace("_", " ").title()}'
            exercises_path = level_dir / 'exercises' / 'exercises.md'
            exercises_path.parent.mkdir(parents=True, exist_ok=True)
            write_exercises(exercises_path, title, topic_data)
            write_kawood(level_dir / 'kawood.md', title, topic_data)

print('Generated lesson markdown, exercises, and Kawood content for all sections.')
