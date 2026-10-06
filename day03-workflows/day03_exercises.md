# Day 3 Exercises: Development Tools & Workflows
_PhD Course in Integrative Neurosciences - Introduction to Scientific Programming_
## Overview
This document contains hands-on exercises to practice the development tools and workflows covered in the course. Complete these exercises in order, as later exercises build on earlier ones. Note that this is very comprehensive and is meant to make you familiar and proficient with the contents discussed. It is highly advisable that you try to do as much as possible, but you are not required to complete, nor do you strictly need this to understand the remainder of the course.

---
## Table of Contents
1. [Jupyter Notebooks Exercises](#exercise-1-jupyter-notebooks)
2. [Virtual Environments Exercises](#exercise-2-virtual-environments)
3. [Git Fundamentals Exercises](#exercise-3-git-fundamentals)
4. [GitHub Workflows Exercises](#exercise-4-github-workflows)
5. [Integrated Workflow Project](#exercise-5-integrated-workflow-project)
---
## Exercise 1: Jupyter Notebooks

**Learning Objectives:**
- Create and navigate Jupyter notebooks
- Use Markdown for documentation
- Execute code cells and understand kernel state
- Create visualizations
- Use magic commands
### Part A: Your First Notebook
1. **Launch Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Create a new notebook**
   - Name it `01_introduction.ipynb`

3. **Add a title cell** (Markdown):
   ```markdown
   # My First Scientific Notebook
   ## Introduction to Data Analysis
   
   **Author**: Your Name  
   **Date**: YYYY-MM-DD
   
   This notebook demonstrates basic data analysis techniques.
   ```

4. **Import libraries** (Code cell):
   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   %matplotlib inline
   ```

5. **Test cell execution order**:
   
   In cell 1:
   ```python
   x = 10
   print(f"x is set to {x}")
   ```
   
   In cell 2:
   ```python
   print(f"x is still {x}")
   ```
   
   In cell 3:
   ```python
   x = 20
   print(f"x is now {x}")
   ```
   
   Execute cells in order: 1, 2, 3, then re-execute cell 2. What happens?

6. **Add an explanation** (Markdown):
   ```markdown
   ## Understanding Kernel State
   
   The kernel maintains variables across cells. When we changed `x` to 20,
   re-running cell 2 showed the new value because the kernel remembers
   the latest value.
   
   **Key insight**: Cell order in the notebook file doesn't matter—
   execution order does!
   ```

### Part B: Data Analysis Practice 

Continue in the same notebook:

7. **Add a section header** (Markdown):
   ```markdown
   ## Data Generation and Analysis
   ```

8. **Generate sample data** (Code):
   ```python
   # Set random seed for reproducibility
   np.random.seed(42)
   
   # Generate sample data: temperature measurements
   days = np.arange(1, 31)  # 30 days
   temperature = 20 + 5 * np.sin(days / 5) + np.random.normal(0, 1, 30)
   
   print(f"Generated {len(days)} temperature measurements")
   print(f"Temperature range: {temperature.min():.1f}°C to {temperature.max():.1f}°C")
   ```

9. **Basic statistics** (Code):
   ```python
   mean_temp = temperature.mean()
   std_temp = temperature.std()
   
   print(f"Mean temperature: {mean_temp:.2f}°C")
   print(f"Standard deviation: {std_temp:.2f}°C")
   ```

10. **Create a visualization** (Code):
    ```python
    plt.figure(figsize=(10, 6))
    plt.plot(days, temperature, 'bo-', label='Measured')
    plt.axhline(y=mean_temp, color='r', linestyle='--', label=f'Mean: {mean_temp:.1f}°C')
    plt.fill_between(days, mean_temp - std_temp, mean_temp + std_temp, 
                      alpha=0.2, color='red', label='±1 std dev')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Measurements Over 30 Days')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

11. **Document findings** (Markdown):
    ```markdown
    ## Results
    
    The temperature data shows:
    - A sinusoidal pattern with a period of approximately 10 days
    - Random fluctuations around the trend (±1-2°C)
    - Mean temperature of approximately 20°C
    
    This pattern could represent:
    - Daily temperature cycles
    - Weekly weather patterns
    - Measurement noise superimposed on a trend
    ```

### Part C: Magic Commands

12. **Add a section** (Markdown):
    ```markdown
    ## Exploring Magic Commands
    ```

13. **Time a computation**:
    ```python
    # Time a single execution
    %timeit sum(range(10000))
    ```
    
    ```python
    # Time a code block
    %%timeit
    total = 0
    for i in range(10000):
        total += i
    ```

14. **View variables**:
    ```python
    %whos
    ```

15. **Save variables**:
    ```python
    # Save data to file
    %store temperature
    %store days
    
    # List stored variables
    %store
    ```

16. **System commands**:
    ```python
    # List current directory (Unix/Mac)
    !ls -la
    
    # Or on Windows
    !dir
    ```

### Part D: Interactive Widgets 

17. **Install ipywidgets** (if not installed):
    ```python
    # Run in terminal:
    # pip install ipywidgets
    ```

18. **Create interactive plot**:
    ```python
    import ipywidgets as widgets
    from IPython.display import display
    
    def plot_sine(frequency, amplitude):
        x = np.linspace(0, 10, 1000)
        y = amplitude * np.sin(frequency * x)
        
        plt.figure(figsize=(10, 4))
        plt.plot(x, y)
        plt.ylim(-10, 10)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Sine wave: amplitude={amplitude}, frequency={frequency}')
        plt.grid(True, alpha=0.3)
        plt.show()
    
    widgets.interact(plot_sine, 
                     frequency=(0.1, 5.0, 0.1),
                     amplitude=(0.1, 10.0, 0.5))
    ```

### Part E: Best Practices 

19. **Clean up and prepare for sharing**:
    - Click **Kernel → Restart & Clear Output**
    - Click **Kernel → Restart & Run All**
    - Check that all cells execute without errors
    - Save the notebook: **Ctrl+S**

20. **Export notebook**:
    - **File → Download as → HTML**
    - Open the HTML file in a browser to see the static version

### Questions to Answer:

1. What happens to variables when you restart the kernel?
2. Why is it important to run "Restart & Run All" before sharing?
3. What's the difference between `%timeit` and `%%timeit`?
4. When should you use Markdown cells vs code cells with comments?

---

## Exercise 2: Virtual Environments

**Learning Objectives:**
- Create and manage virtual environments
- Install and manage packages
- Export and recreate environments
- Compare venv and conda

### Part A: Python venv 

1. **Create a project directory**:
   ```bash
   mkdir data_project
   cd data_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv_data
   ```
   
   **Question**: What directories and files were created?

3. **Activate the environment**:
   
   **Linux/Mac**:
   ```bash
   source venv_data/bin/activate
   ```
   
   **Windows**:
   ```bash
   venv_data\Scripts\activate
   ```
   
   Your prompt should now show `(venv_data)`.

4. **Check Python location**:
   ```bash
   which python    # Linux/Mac
   where python    # Windows
   ```
   
   **Question**: Is this the system Python or the venv Python?

5. **Install packages**:
   ```bash
   pip install numpy pandas matplotlib
   ```

6. **List installed packages**:
   ```bash
   pip list
   ```
   
   **Question**: How many packages are installed? (Note: dependencies are included)

7. **Create requirements file**:
   ```bash
   pip freeze > requirements.txt
   ```
   
   Open `requirements.txt` and examine the contents.

8. **Test the environment**:
   ```bash
   python -c "import numpy; print(numpy.__version__)"
   ```

9. **Deactivate**:
   ```bash
   deactivate
   ```
   
   Your prompt should return to normal.

10. **Try importing numpy now**:
    ```bash
    python -c "import numpy"
    ```
    
    **Question**: What happens? Why?

### Part B: Reproducing an Environment 

11. **Create a second environment**:
    ```bash
    python -m venv venv_test
    source venv_test/bin/activate  # or activate on Windows
    ```

12. **Install from requirements**:
    ```bash
    pip install -r requirements.txt
    ```

13. **Verify identical packages**:
    ```bash
    pip list
    ```
    
    **Question**: Is this list identical to the first environment?

14. **Test imports**:
    ```bash
    python -c "import numpy, pandas, matplotlib; print('Success!')"
    ```

15. **Clean up**:
    ```bash
    deactivate
    ```

### Part C: Conda Environments

16. **Verify conda installation**:
    ```bash
    conda --version
    ```
    
    If not installed, download Miniconda: https://docs.conda.io/en/latest/miniconda.html

17. **Create conda environment**:
    ```bash
    conda create -n analysis_env python=3.10
    ```
    
    Type `y` when prompted.

18. **Activate environment**:
    ```bash
    conda activate analysis_env
    ```

19. **Install packages with conda**:
    ```bash
    conda install numpy pandas matplotlib scipy scikit-learn
    ```

20. **List installed packages**:
    ```bash
    conda list
    ```
    
    **Question**: Compare the output to `pip list`. What differences do you notice?

21. **Export environment**:
    ```bash
    conda env export > environment.yml
    ```
    
    Open `environment.yml` and examine the structure.

22. **Create environment from file**:
    ```bash
    conda deactivate
    conda env create -f environment.yml -n analysis_clone
    conda activate analysis_clone
    conda list
    ```
    
    **Question**: Is the package list identical to `analysis_env`?

23. **Test different Python versions**:
    ```bash
    conda deactivate
    conda create -n py39 python=3.9
    conda activate py39
    python --version
    ```
    
    ```bash
    conda create -n py311 python=3.11
    conda activate py311
    python --version
    ```

24. **List all environments**:
    ```bash
    conda env list
    ```

25. **Clean up**:
    ```bash
    conda deactivate
    conda env remove -n analysis_clone
    conda env remove -n py39
    conda env remove -n py311
    ```

### Part D: Comparison Exercise

26. **Create a curated `requirements.txt`**:
    
    Create a file named `requirements_minimal.txt`:
    ```
    numpy>=1.24.0
    pandas>=2.0.0
    matplotlib>=3.7.0
    scipy>=1.10.0
    jupyter>=1.0.0
    ```

27. **Create environments with both tools**:
    
    **venv**:
    ```bash
    python -m venv venv_minimal
    source venv_minimal/bin/activate
    pip install -r requirements_minimal.txt
    pip list > venv_packages.txt
    deactivate
    ```
    
    **conda**:
    ```bash
    conda create -n conda_minimal python=3.10
    conda activate conda_minimal
    conda install numpy pandas matplotlib scipy jupyter
    conda list > conda_packages.txt
    conda deactivate
    ```

28. **Compare package lists**:
    ```bash
    wc -l venv_packages.txt conda_packages.txt
    ```
    
    **Question**: Which has more packages? Why?

### Part E: Real-World Scenario 

29. **Scenario**: A colleague shares a project with this `environment.yml`:
    
    Create `project_environment.yml`:
    ```yaml
    name: genomics_analysis
    channels:
      - conda-forge
      - bioconda
      - defaults
    dependencies:
      - python=3.10
      - numpy=1.24
      - pandas=2.0
      - matplotlib=3.7
      - biopython=1.81
      - scikit-learn=1.3
      - jupyter=1.0
      - pip
      - pip:
        - genomics-toolkit==2.1.0
    ```

30. **Set up the environment**:
    ```bash
    conda env create -f project_environment.yml
    conda activate genomics_analysis
    ```

31. **Verify installation**:
    ```bash
    python -c "import Bio; print(f'Biopython version: {Bio.__version__}')"
    ```

32. **Document the setup**:
    
    Create `SETUP.md`:
    ```markdown
    # Environment Setup
    
    ## Prerequisites
    - Miniconda or Anaconda
    
    ## Installation
    1. Create environment:
       ```bash
       conda env create -f project_environment.yml
       ```
    
    2. Activate environment:
       ```bash
       conda activate genomics_analysis
       ```
    
    3. Verify installation:
       ```bash
       python -c "import Bio; print('Success!')"
       ```
    
    ## Updating
    To update the environment file after installing new packages:
    ```bash
    conda env export > project_environment.yml
    ```
    ```

### Questions to Answer:

1. When would you use `venv` vs `conda`?
2. What's the difference between `pip freeze` and a curated `requirements.txt`?
3. Why include version numbers in requirements files?
4. How do you handle platform-specific dependencies?
5. What's the purpose of the `channels` section in `environment.yml`?

---

## Exercise 3: Git Fundamentals

**Learning Objectives:**
- Initialize repositories
- Make commits
- View history
- Use branches
- Merge changes
- Resolve conflicts

### Part A: Basic Git Operations 

1. **Configure Git** (if not already done):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   git config --global init.defaultBranch main
   ```

2. **Create a new project**:
   ```bash
   mkdir gene_analysis
   cd gene_analysis
   ```

3. **Initialize Git repository**:
   ```bash
   git init
   git status
   ```
   
   **Question**: What does `git status` tell you?

4. **Create a Python script**:
   
   Create `sequence_analyzer.py`:
   ```python
   """
   DNA Sequence Analyzer
   Simple tools for analyzing DNA sequences.
   """
   
   def gc_content(sequence):
       """Calculate GC content of DNA sequence."""
       sequence = sequence.upper()
       gc_count = sequence.count('G') + sequence.count('C')
       return gc_count / len(sequence) * 100
   
   if __name__ == "__main__":
       test_seq = "ATGCATGCATGC"
       print(f"GC content: {gc_content(test_seq):.1f}%")
   ```

5. **Check status**:
   ```bash
   git status
   ```
   
   **Question**: What is the file's status?

6. **Stage the file**:
   ```bash
   git add sequence_analyzer.py
   git status
   ```
   
   **Question**: How did the status change?

7. **Make first commit**:
   ```bash
   git commit -m "Add basic GC content calculator"
   ```

8. **View commit history**:
   ```bash
   git log
   git log --oneline
   ```

9. **Create README**:
   
   Create `README.md`:
   ```markdown
   # Gene Analysis Tools
   
   Tools for analyzing DNA sequences.
   
   ## Features
   - GC content calculation
   
   ## Usage
   ```python
   from sequence_analyzer import gc_content
   
   seq = "ATGCATGC"
   gc = gc_content(seq)
   print(f"GC content: {gc:.1f}%")
   ```
   ```

10. **Stage and commit**:
    ```bash
    git add README.md
    git commit -m "Add README with usage instructions"
    ```

11. **Create .gitignore**:
    
    Create `.gitignore`:
    ```
    __pycache__/
    *.pyc
    .ipynb_checkpoints/
    *.egg-info/
    .venv/
    venv/
    data/
    results/
    ```

12. **Stage and commit**:
    ```bash
    git add .gitignore
    git commit -m "Add gitignore for Python project"
    ```

13. **View history**:
    ```bash
    git log --oneline --graph
    ```

### Part B: Making Changes

14. **Add a new function**:
    
    Edit `sequence_analyzer.py`, add before `if __name__`:
    ```python
    
    def reverse_complement(sequence):
        """Return the reverse complement of a DNA sequence."""
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        sequence = sequence.upper()
        rev_comp = ''.join([complement[base] for base in sequence[::-1]])
        return rev_comp
    ```

15. **Check what changed**:
    ```bash
    git diff
    ```
    
    **Question**: What do the `+` and `-` symbols mean?

16. **Stage and commit**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add reverse complement function"
    ```

17. **Add test in main block**:
    
    Modify the `if __name__` block:
    ```python
    if __name__ == "__main__":
        test_seq = "ATGCATGCATGC"
        print(f"Original: {test_seq}")
        print(f"GC content: {gc_content(test_seq):.1f}%")
        print(f"Reverse complement: {reverse_complement(test_seq)}")
    ```

18. **View diff and commit**:
    ```bash
    git diff
    git add sequence_analyzer.py
    git commit -m "Add test for reverse complement"
    ```

19. **View history**:
    ```bash
    git log --oneline
    ```

### Part C: Branches

20. **Create a feature branch**:
    ```bash
    git branch feature-translate
    git branch
    ```
    
    **Question**: Which branch are you currently on?

21. **Switch to the branch**:
    ```bash
    git switch feature-translate
    # or older syntax: git checkout feature-translate
    git branch
    ```

22. **Add translation function**:
    
    Add to `sequence_analyzer.py`:
    ```python
    
    def translate(sequence):
        """Translate DNA sequence to protein."""
        codon_table = {
            'ATG': 'M', 'TGG': 'W',
            'TTT': 'F', 'TTC': 'F',
            'TAA': '*', 'TAG': '*', 'TGA': '*',
            # Add more codons as needed
        }
        
        protein = []
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i+3].upper()
            aa = codon_table.get(codon, 'X')  # X for unknown
            protein.append(aa)
            if aa == '*':  # Stop codon
                break
        
        return ''.join(protein)
    ```

23. **Commit the change**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add basic translation function"
    ```

24. **Add test for translation**:
    
    Update `if __name__`:
    ```python
    if __name__ == "__main__":
        test_seq = "ATGTTTTAA"
        print(f"Original: {test_seq}")
        print(f"GC content: {gc_content(test_seq):.1f}%")
        print(f"Reverse complement: {reverse_complement(test_seq)}")
        print(f"Translation: {translate(test_seq)}")
    ```

25. **Commit**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add translation test"
    ```

26. **View branch history**:
    ```bash
    git log --oneline --graph
    ```

27. **Switch back to main**:
    ```bash
    git switch main
    ```
    
    Open `sequence_analyzer.py` - the `translate` function is gone!
    
    **Question**: Why is the function missing?

28. **Merge the feature**:
    ```bash
    git merge feature-translate
    ```
    
    Open `sequence_analyzer.py` - now the function is there!

29. **View history graph**:
    ```bash
    git log --oneline --graph --all
    ```

30. **Delete the feature branch**:
    ```bash
    git branch -d feature-translate
    git branch
    ```

### Part D: Merge Conflicts

31. **Create two conflicting branches**:
    ```bash
    git branch improve-gc
    git branch improve-revcomp
    ```

32. **Make change in improve-gc**:
    ```bash
    git switch improve-gc
    ```
    
    Modify the `gc_content` function:
    ```python
    def gc_content(sequence):
        """Calculate GC content of DNA sequence."""
        sequence = sequence.upper()
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        total = len(sequence)
        return (g_count + c_count) / total * 100
    ```
    
    Commit:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Improve GC content calculation clarity"
    ```

33. **Make different change in improve-revcomp**:
    ```bash
    git switch improve-revcomp
    ```
    
    Modify the `gc_content` function differently:
    ```python
    def gc_content(sequence):
        """Calculate GC content percentage of DNA sequence.
        
        Returns value between 0 and 100.
        """
        sequence = sequence.upper()
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0
    ```
    
    Commit:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add safety check for empty sequences"
    ```

34. **Merge first branch into main**:
    ```bash
    git switch main
    git merge improve-gc
    ```
    
    This should merge without issues.

35. **Try to merge second branch**:
    ```bash
    git merge improve-revcomp
    ```
    
    **Conflict!** You should see:
    ```
    CONFLICT (content): Merge conflict in sequence_analyzer.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```

36. **View the conflict**:
    ```bash
    git status
    ```
    
    Open `sequence_analyzer.py` and find:
    ```python
    <<<<<<< HEAD
    def gc_content(sequence):
        """Calculate GC content of DNA sequence."""
        sequence = sequence.upper()
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        total = len(sequence)
        return (g_count + c_count) / total * 100
    =======
    def gc_content(sequence):
        """Calculate GC content percentage of DNA sequence.
        
        Returns value between 0 and 100.
        """
        sequence = sequence.upper()
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0
    >>>>>>> improve-revcomp
    ```

37. **Resolve the conflict**:
    
    Edit the function to combine both improvements:
    ```python
    def gc_content(sequence):
        """Calculate GC content percentage of DNA sequence.
        
        Returns value between 0 and 100.
        """
        if len(sequence) == 0:
            return 0
        
        sequence = sequence.upper()
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        total = len(sequence)
        return (g_count + c_count) / total * 100
    ```
    
    Remove all conflict markers (`<<<<<<<`,  `>>>>>>>`).

38. **Complete the merge**:
    ```bash
    git add sequence_analyzer.py
    git status  # Should say "All conflicts fixed"
    git commit -m "Merge improve-revcomp: combine both improvements"
    ```

39. **View final history**:
    ```bash
    git log --oneline --graph --all
    ```

40. **Clean up branches**:
    ```bash
    git branch -d improve-gc improve-revcomp
    ```

### Questions to Answer:

1. What's the difference between `git add` and `git commit`?
2. Why use branches instead of committing directly to main?
3. What causes merge conflicts?
4. Can you prevent all merge conflicts? How?
5. What does `git log --oneline --graph --all` show?

---

## Exercise 4: GitHub Workflows

**Learning Objectives:**
- Create GitHub repositories
- Push and pull changes
- Create and review pull requests
- Collaborate using forks
- Use GitHub features (Issues, Releases)

### Part A: Creating a GitHub Repository 

1. **Go to GitHub**: https://github.com

2. **Create new repository**:
   - Click "New repository"
   - Name: `gene-analysis-tools`
   - Description: "Tools for analyzing DNA sequences"
   - Public
   - **Don't** initialize with README (we already have one)
   - Click "Create repository"

3. **Connect local repository**:
   
   Use the commands GitHub shows you:
   ```bash
   # In your gene_analysis directory
   git remote add origin https://github.com/YOUR_USERNAME/gene-analysis-tools.git
   git branch -M main
   git push -u origin main
   ```

4. **Verify on GitHub**:
   - Refresh your repository page
   - You should see all your files
   - Click through to view `README.md` and `sequence_analyzer.py`

5. **Add a better README on GitHub**:
   - Click `README.md`
   - Click pencil icon to edit
   - Add:
   ```markdown
   ## Installation
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/gene-analysis-tools.git
   cd gene-analysis-tools
   ```
   
   ## Testing
   
   ```bash
   python sequence_analyzer.py
   ```
   ```
   - Scroll down
   - Add commit message: "Improve README"
   - Click "Commit changes"

6. **Pull changes to local**:
   ```bash
   git pull origin main
   ```
   
   Check `README.md` - it now has your changes!

### Part B: Branch and Pull Request Workflow 

7. **Create issue on GitHub**:
   - Go to "Issues" tab
   - Click "New issue"
   - Title: "Add AT/GC ratio calculation"
   - Comment: "Add function to calculate ratio of AT to GC content"
   - Click "Submit new issue"
   - Note the issue number (e.g., #1)

8. **Create feature branch locally**:
   ```bash
   git switch -c add-at-gc-ratio
   ```

9. **Implement feature**:
   
   Add to `sequence_analyzer.py`:
   ```python
   
   def at_gc_ratio(sequence):
       """Calculate ratio of AT content to GC content."""
       sequence = sequence.upper()
       at_count = sequence.count('A') + sequence.count('T')
       gc_count = sequence.count('G') + sequence.count('C')
       
       if gc_count == 0:
           return float('inf') if at_count > 0 else 0
       
       return at_count / gc_count
   ```
   
   Add test:
   ```python
   if __name__ == "__main__":
       test_seq = "ATGTTTTAA"
       print(f"Original: {test_seq}")
       print(f"GC content: {gc_content(test_seq):.1f}%")
       print(f"AT/GC ratio: {at_gc_ratio(test_seq):.2f}")
       print(f"Reverse complement: {reverse_complement(test_seq)}")
       print(f"Translation: {translate(test_seq)}")
   ```

10. **Commit changes**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add AT/GC ratio calculation

    Implements #1: Calculate ratio of AT to GC content
    Includes handling for edge cases (no GC content)"
    ```
    
    **Note**: "Implements #1" links commit to issue!

11. **Push branch to GitHub**:
    ```bash
    git push -u origin add-at-gc-ratio
    ```

12. **Create Pull Request on GitHub**:
    - GitHub should show a banner "Compare & pull request"
    - Click it (or go to "Pull requests" → "New pull request")
    - Base: `main`, Compare: `add-at-gc-ratio`
    - Title: "Add AT/GC ratio calculation"
    - Description:
    ```markdown
    ## Changes
    - Added `at_gc_ratio()` function
    - Handles edge cases (empty sequence, no GC)
    - Added test in main block
    
    ## Testing
    Tested with various sequences:
    - Normal: ATGC... (works)
    - AT-only: ATAT... (returns inf)
    - Empty: "" (returns 0)
    
    Closes #1
    ```
    - Click "Create pull request"

13. **Review your own PR**:
    - Click "Files changed" tab
    - Hover over lines - you can comment
    - Add a comment: "Should we add more comprehensive tests?"
    - Click "Review changes" → "Approve" → "Submit review"

14. **Merge the PR**:
    - Click "Merge pull request"
    - Click "Confirm merge"
    - Click "Delete branch" (on GitHub)

15. **Update local repository**:
    ```bash
    git switch main
    git pull origin main
    git branch -d add-at-gc-ratio  # Delete local branch
    ```

16. **Check issue**:
    - Go to Issues tab
    - Issue #1 should be closed!
    - The PR is linked automatically

### Part C: Collaboration Workflow

**Note**: You'll need a partner for this, or create a second GitHub account. If working alone, simulate both roles.

**Person A (Repository Owner)**:

17. **Add collaborator**:
    - Go to repository Settings
    - Click "Collaborators"
    - Click "Add people"
    - Enter partner's GitHub username
    - Click "Add [username] to this repository"

**Person B (Collaborator)**:

18. **Accept invitation**:
    - Check email or GitHub notifications
    - Accept collaboration invitation

19. **Clone repository**:
    ```bash
    git clone https://github.com/PERSON_A_USERNAME/gene-analysis-tools.git
    cd gene-analysis-tools
    ```

20. **Create feature branch**:
    ```bash
    git switch -c add-sequence-validator
    ```

21. **Add validation function**:
    
    Add to `sequence_analyzer.py`:
    ```python
    
    def is_valid_dna(sequence):
        """Check if sequence contains only valid DNA bases."""
        valid_bases = set('ATGC')
        return all(base.upper() in valid_bases for base in sequence)
    
    def validate_sequence(sequence):
        """Validate DNA sequence and raise error if invalid."""
        if not sequence:
            raise ValueError("Sequence cannot be empty")
        if not is_valid_dna(sequence):
            raise ValueError(f"Invalid DNA sequence: {sequence}")
        return True
    ```

22. **Update existing functions to use validation**:
    
    Modify `gc_content`:
    ```python
    def gc_content(sequence):
        """Calculate GC content percentage of DNA sequence.
        
        Returns value between 0 and 100.
        """
        validate_sequence(sequence)
        
        sequence = sequence.upper()
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        total = len(sequence)
        return (g_count + c_count) / total * 100
    ```

23. **Commit and push**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add sequence validation

    - Add is_valid_dna() and validate_sequence()
    - Update gc_content() to validate input
    - Raises ValueError for invalid sequences"
    
    git push -u origin add-sequence-validator
    ```

24. **Create Pull Request**:
    - Go to GitHub
    - Create PR: `add-sequence-validator` → `main`
    - Title: "Add DNA sequence validation"
    - Description: Explain the changes
    - Assign Person A as reviewer

**Person A (Repository Owner)**:

25. **Review the PR**:
    - Go to "Pull requests"
    - Click on the PR from Person B
    - Click "Files changed"
    - Review the code
    - Click on a line number, add comment:
      "Should we also update the other functions to validate input?"
    - Click "Start a review"
    - Add a few more comments
    - Click "Review changes" → "Request changes" → "Submit review"

**Person B (Collaborator)**:

26. **Address review comments**:
    
    Update other functions to use validation:
    ```python
    def reverse_complement(sequence):
        """Return the reverse complement of a DNA sequence."""
        validate_sequence(sequence)
        # ... rest of function
    
    def translate(sequence):
        """Translate DNA sequence to protein."""
        validate_sequence(sequence)
        # ... rest of function
    
    def at_gc_ratio(sequence):
        """Calculate ratio of AT content to GC content."""
        validate_sequence(sequence)
        # ... rest of function
    ```

27. **Commit and push updates**:
    ```bash
    git add sequence_analyzer.py
    git commit -m "Add validation to all functions

    Addresses review comments"
    
    git push
    ```

28. **Reply to review**:
    - Go back to PR on GitHub
    - Reply to review comments: "Updated all functions to validate input"

**Person A (Repository Owner)**:

29. **Re-review and approve**:
    - Check the new commits
    - Click "Review changes" → "Approve" → "Submit review"
    - Click "Merge pull request"
    - Click "Confirm merge"

30. **Pull changes locally**:
    ```bash
    git pull origin main
    ```

### Part D: Fork Workflow 

**Simulating contributing to someone else's project**:

31. **Fork a repository**:
    - Go to a public repository (or use a partner's)
    - Click "Fork" button (top right)
    - Click "Create fork"

32. **Clone YOUR fork**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/forked-repo.git
    cd forked-repo
    ```

33. **Add upstream remote**:
    ```bash
    git remote add upstream https://github.com/ORIGINAL_OWNER/original-repo.git
    git remote -v
    ```
    
    You should see:
    - `origin`: Your fork
    - `upstream`: Original repository

34. **Create feature branch**:
    ```bash
    git switch -c fix-documentation
    ```

35. **Make changes**:
    - Fix a typo in README
    - Add more documentation
    - Improve comments

36. **Commit and push to YOUR fork**:
    ```bash
    git add .
    git commit -m "Improve documentation"
    git push -u origin fix-documentation
    ```

37. **Create Pull Request to original**:
    - Go to YOUR fork on GitHub
    - Click "Contribute" → "Open pull request"
    - Base repository: original owner's repo
    - Base: `main`
    - Head repository: your fork
    - Compare: `fix-documentation`
    - Create pull request

38. **Keep fork updated** (do this regularly):
    ```bash
    git fetch upstream
    git switch main
    git merge upstream/main
    git push origin main
    ```

### Part E: Releases and Documentation

39. **Create a release**:
    - Go to repository main page
    - Click "Releases" (right sidebar)
    - Click "Create a new release"
    - Click "Choose a tag"
    - Type: `v1.0.0`
    - Click "Create new tag"
    - Release title: "Version 1.0.0 - Initial Release"
    - Description:
    ```markdown
    ## Features
    - GC content calculation
    - Reverse complement
    - Translation
    - AT/GC ratio
    - Sequence validation
    
    ## Installation
    ```bash
    git clone https://github.com/username/gene-analysis-tools.git
    ```
    ```
    - Click "Publish release"

40. **View the release**:
    - Click on release
    - Note the zip/tar.gz download links
    - This provides a permanent snapshot

41. **Add topics to repository**:
    - Go to repository main page
    - Click gear icon next to "About"
    - Add topics: `dna`, `bioinformatics`, `python`, `genetics`
    - Add website (if you have one)
    - Save changes

42. **Update README with badges**:
    
    Add to top of README.md:
    ```markdown
    # Gene Analysis Tools
    
    ![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
    ![License](https://img.shields.io/badge/license-MIT-green.svg)
    ![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)
    ```
    
    Commit and push.

### Questions to Answer:

1. What's the difference between a fork and a clone?
2. When should you use a Pull Request vs direct commit?
3. Why link commits to issues (e.g., "Fixes #1")?
4. What are the benefits of code review?
5. How do releases differ from commits/tags?

---

## Exercise 5: Integrated Workflow Project

**Learning Objectives:**
- Apply all tools in a complete workflow
- Create reproducible research project
- Collaborate effectively
- Document thoroughly

### Project: Temperature Data Analysis

You'll create a complete analysis project with proper structure, version control, environments, and documentation.

### Part A: Project Setup

1. **Create project directory**:
   ```bash
   mkdir temperature_analysis
   cd temperature_analysis
   ```

2. **Initialize Git**:
   ```bash
   git init
   ```

3. **Create .gitignore**:
   ```
   # Python
   __pycache__/
   *.pyc
   .ipynb_checkpoints/
   
   # Environments
   venv/
   .venv/
   env/
   
   # Data (will be downloaded)
   data/raw/
   
   # Results
   figures/
   results/
   
   # IDE
   .vscode/
   .idea/
   ```

4. **Create project structure**:
   ```bash
   mkdir -p data/{raw,processed} notebooks src figures results
   touch README.md requirements.txt
   touch src/__init__.py
   touch notebooks/.gitkeep figures/.gitkeep results/.gitkeep
   ```

5. **Create README.md**:
   ```markdown
   # Temperature Analysis Project
   
   Analysis of temperature trends over time.
   
   ## Project Structure
   ```
   temperature_analysis/
   ├── data/
   │   ├── raw/          # Original data (not in git)
   │   └── processed/    # Cleaned data
   ├── notebooks/        # Jupyter notebooks
   ├── src/              # Source code
   ├── figures/          # Generated plots
   └── results/          # Analysis results
   ```
   
   ## Setup
   
   ### Create Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   
   ### Download Data
   ```bash
   python src/download_data.py
   ```
   
   ## Usage
   
   Run the analysis notebooks in order:
   1. `01_data_exploration.ipynb`
   2. `02_statistical_analysis.ipynb`
   3. `03_visualization.ipynb`
   
   ## Author
   Your Name
   ```

6. **Commit initial structure**:
   ```bash
   git add .
   git commit -m "Initial project structure"
   ```

### Part B: Environment Setup 

7. **Create requirements.txt**:
   ```
   numpy>=1.24.0
   pandas>=2.0.0
   matplotlib>=3.7.0
   scipy>=1.10.0
   jupyter>=1.0.0
   seaborn>=0.12.0
   ```

8. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

9. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

10. **Commit requirements**:
    ```bash
    git add requirements.txt
    git commit -m "Add project dependencies"
    ```

### Part C: Data Acquisition

11. **Create data download script**:
    
    Create `src/download_data.py`:
    ```python
    """
    Download temperature data for analysis.
    """
    import numpy as np
    import pandas as pd
    from pathlib import Path
    
    def generate_sample_data():
        """Generate sample temperature data."""
        np.random.seed(42)
        
        # Generate 365 days of data
        dates = pd.date_range('2023-01-01', periods=365, freq='D')
        
        # Seasonal component (sine wave with period of 365 days)
        day_of_year = dates.dayofyear
        seasonal = 15 * np.sin(2 * np.pi * day_of_year / 365 - np.pi/2)
        
        # Trend (slight warming)
        trend = np.linspace(0, 2, 365)
        
        # Random noise
        noise = np.random.normal(0, 3, 365)
        
        # Combine components
        temperature = 15 + seasonal + trend + noise
        
        # Create DataFrame
        df = pd.DataFrame({
            'date': dates,
            'temperature': temperature,
            'location': 'City_A'
        })
        
        return df
    
    def main():
        """Download/generate and save data."""
        print("Generating sample data...")
        df = generate_sample_data()
        
        # Create data directory if needed
        data_dir = Path('data/raw')
        data_dir.mkdir(parents=True, exist_ok=True)
        
        # Save data
        output_file = data_dir / 'temperature_data.csv'
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
        print(f"Generated {len(df)} records")
    
    if __name__ == "__main__":
        main()
    ```

12. **Run the script**:
    ```bash
    python src/download_data.py
    ```

13. **Commit the script** (but not the data!):
    ```bash
    git add src/download_data.py
    git commit -m "Add data download script"
    ```

### Part D: Data Processing Module 

14. **Create processing module**:
    
    Create `src/data_processing.py`:
    ```python
    """
    Data processing utilities.
    """
    import pandas as pd
    import numpy as np
    from pathlib import Path
    
    def load_raw_data(filepath):
        """
        Load raw temperature data.
        
        Parameters
        ----------
        filepath : str or Path
            Path to CSV file.
        
        Returns
        -------
        DataFrame
            Loaded data with parsed dates.
        """
        df = pd.read_csv(filepath, parse_dates=['date'])
        return df
    
    def clean_data(df):
        """
        Clean temperature data.
        
        Parameters
        ----------
        df : DataFrame
            Raw data.
        
        Returns
        -------
        DataFrame
            Cleaned data.
        """
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Remove missing values
        df = df.dropna()
        
        # Sort by date
        df = df.sort_values('date')
        
        # Reset index
        df = df.reset_index(drop=True)
        
        return df
    
    def add_features(df):
        """
        Add derived features.
        
        Parameters
        ----------
        df : DataFrame
            Cleaned data.
        
        Returns
        -------
        DataFrame
            Data with additional features.
        """
        # Extract date components
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day_of_year'] = df['date'].dt.dayofyear
        
        # Calculate moving averages
        df['temp_7day_ma'] = df['temperature'].rolling(window=7, center=True).mean()
        df['temp_30day_ma'] = df['temperature'].rolling(window=30, center=True).mean()
        
        return df
    
    def process_data(input_path, output_path):
        """
        Complete data processing pipeline.
        
        Parameters
        ----------
        input_path : str or Path
            Path to raw data.
        output_path : str or Path
            Path to save processed data.
        
        Returns
        -------
        DataFrame
            Processed data.
        """
        print("Loading data...")
        df = load_raw_data(input_path)
        
        print("Cleaning data...")
        df = clean_data(df)
        
        print("Adding features...")
        df = add_features(df)
        
        # Save processed data
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
        
        return df
    
    if __name__ == "__main__":
        process_data(
            'data/raw/temperature_data.csv',
            'data/processed/temperature_processed.csv'
        )
    ```

15. **Test the module**:
    ```bash
    python src/data_processing.py
    ```

16. **Commit**:
    ```bash
    git add src/data_processing.py
    git commit -m "Add data processing module"
    ```

### Part E: Analysis Notebooks

17. **Start Jupyter**:
    ```bash
    jupyter notebook
    ```

18. **Create exploration notebook**:
    
    Create `notebooks/01_data_exploration.ipynb`:
    
    **Cell 1** (Markdown):
    ```markdown
    # Temperature Data Exploration
    
    Initial exploration of temperature data.
    
    **Author**: Your Name  
    **Date**: YYYY-MM-DD
    ```
    
    **Cell 2** (Code - Setup):
    ```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    %matplotlib inline
    sns.set_style('whitegrid')
    
    # Import our modules
    import sys
    sys.path.append('../')
    from src.data_processing import load_raw_data, process_data
    ```
    
    **Cell 3** (Code - Load):
    ```python
    # Load raw data
    df_raw = load_raw_data('../data/raw/temperature_data.csv')
    print(f"Loaded {len(df_raw)} records")
    df_raw.head()
    ```
    
    **Cell 4** (Code - Summary):
    ```python
    # Summary statistics
    df_raw['temperature'].describe()
    ```
    
    **Cell 5** (Code - Plot):
    ```python
    # Plot time series
    plt.figure(figsize=(12, 6))
    plt.plot(df_raw['date'], df_raw['temperature'], alpha=0.7)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Raw Temperature Data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    ```
    
    **Cell 6** (Code - Distribution):
    ```python
    # Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df_raw['temperature'], bins=50, edgecolor='black')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Temperature Distribution')
    plt.axvline(df_raw['temperature'].mean(), color='red', 
                linestyle='--', label='Mean')
    plt.legend()
    plt.show()
    ```
    
    **Cell 7** (Markdown):
    ```markdown
    ## Observations
    
    - Data shows clear seasonal pattern
    - Some random fluctuations visible
    - Distribution appears roughly normal
    - Mean temperature around 15-20°C
    ```

19. **Process data and create analysis notebook**:
    
    Create `notebooks/02_statistical_analysis.ipynb`:
    
    **Cell 1** (Markdown):
    ```markdown
    # Statistical Analysis
    
    Detailed statistical analysis of temperature trends.
    ```
    
    **Cell 2** (Code - Setup):
    ```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy import stats
    
    import sys
    sys.path.append('../')
    from src.data_processing import process_data
    
    %matplotlib inline
    ```
    
    **Cell 3** (Code - Load processed):
    ```python
    # Process data
    df = process_data(
        '../data/raw/temperature_data.csv',
        '../data/processed/temperature_processed.csv'
    )
    df.head()
    ```
    
    **Cell 4** (Code - Monthly analysis):
    ```python
    # Monthly statistics
    monthly_stats = df.groupby('month')['temperature'].agg([
        'mean', 'std', 'min', 'max'
    ]).round(2)
    monthly_stats
    ```
    
    **Cell 5** (Code - Trend analysis):
    ```python
    # Linear trend
    x = np.arange(len(df))
    y = df['temperature'].values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    print(f"Trend: {slope:.4f} °C/day")
    print(f"R-squared: {r_value**2:.4f}")
    print(f"P-value: {p_value:.4e}")
    ```
    
    **Cell 6** (Code - Plot with trend):
    ```python
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['temperature'], alpha=0.5, label='Data')
    plt.plot(df['date'], df['temp_30day_ma'], 
             label='30-day MA', linewidth=2)
    
    # Add trend line
    trend_line = slope * x + intercept
    plt.plot(df['date'], trend_line, 'r--', 
             label=f'Trend ({slope*365:.2f}°C/year)')
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature with Trend')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../figures/temperature_trend.png', dpi=300)
    plt.show()
    ```

20. **Save notebooks and commit**:
    ```bash
    git add notebooks/
    git commit -m "Add exploration and analysis notebooks"
    ```

### Part F: Create GitHub Repository

21. **Create repository on GitHub**:
    - Name: `temperature-analysis`
    - Description: "Statistical analysis of temperature trends"
    - Public
    - Don't initialize

22. **Connect and push**:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/temperature-analysis.git
    git branch -M main
    git push -u origin main
    ```

23. **Add LICENSE**:
    - On GitHub, click "Add file" → "Create new file"
    - Name: `LICENSE`
    - Click "Choose a license template"
    - Select "MIT License"
    - Fill in year and name
    - Commit

24. **Pull license locally**:
    ```bash
    git pull origin main
    ```

### Part G: Collaborative Feature 

25. **Create issue**:
    - On GitHub: Issues → New issue
    - Title: "Add seasonal decomposition analysis"
    - Body: "Decompose temperature into trend, seasonal, and residual components"
    - Submit

26. **Create feature branch**:
    ```bash
    git switch -c seasonal-decomposition
    ```

27. **Add analysis function**:
    
    Create `src/analysis.py`:
    ```python
    """
    Statistical analysis functions.
    """
    import numpy as np
    import pandas as pd
    from scipy import signal
    
    def seasonal_decomposition(series, period=365):
        """
        Decompose time series into components.
        
        Parameters
        ----------
        series : array-like
            Time series data.
        period : int
            Period for seasonal component.
        
        Returns
        -------
        dict
            Dictionary with 'trend', 'seasonal', 'residual' components.
        """
        # Simple moving average for trend
        trend = pd.Series(series).rolling(
            window=period, center=True
        ).mean().values
        
        # Detrended data
        detrended = series - trend
        
        # Average seasonal pattern
        seasonal = np.tile(
            np.nanmean(
                detrended.reshape(-1, period), axis=0
            ),
            len(series) // period + 1
        )[:len(series)]
        
        # Residual
        residual = series - trend - seasonal
        
        return {
            'trend': trend,
            'seasonal': seasonal,
            'residual': residual
        }
    ```

28. **Create notebook to test**:
    
    Create `notebooks/03_seasonal_decomposition.ipynb`:
    
    ```python
    # Setup
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import sys
    sys.path.append('../')
    from src.analysis import seasonal_decomposition
    
    # Load data
    df = pd.read_csv('../data/processed/temperature_processed.csv',
                     parse_dates=['date'])
    
    # Decompose
    components = seasonal_decomposition(
        df['temperature'].values, period=365
    )
    
    # Plot
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))
    
    axes[0].plot(df['date'], df['temperature'])
    axes[0].set_title('Original')
    axes[0].set_ylabel('Temperature (°C)')
    
    axes[1].plot(df['date'], components['trend'])
    axes[1].set_title('Trend')
    axes[1].set_ylabel('Temperature (°C)')
    
    axes[2].plot(df['date'], components['seasonal'])
    axes[2].set_title('Seasonal')
    axes[2].set_ylabel('Temperature (°C)')
    
    axes[3].plot(df['date'], components['residual'])
    axes[3].set_title('Residual')
    axes[3].set_ylabel('Temperature (°C)')
    axes[3].set_xlabel('Date')
    
    plt.tight_layout()
    plt.savefig('../figures/seasonal_decomposition.png', dpi=300)
    plt.show()
    ```

29. **Commit and push**:
    ```bash
    git add src/analysis.py notebooks/03_seasonal_decomposition.ipynb
    git commit -m "Add seasonal decomposition analysis

    Implements #1: Decompose temperature into trend, seasonal, residual"
    git push -u origin seasonal-decomposition
    ```

30. **Create Pull Request**:
    - On GitHub: Create PR
    - Title: "Add seasonal decomposition"
    - Description: Link to issue, explain changes
    - Create PR

31. **Merge (if working alone, or wait for review)**:
    - Review files changed
    - Merge pull request
    - Delete branch on GitHub

32. **Update local**:
    ```bash
    git switch main
    git pull origin main
    git branch -d seasonal-decomposition
    ```

### Part H: Finalize and Release 

33. **Update README with results**:
    
    Add to README.md:
    ```markdown
    ## Results
    
    ### Key Findings
    - Clear seasonal pattern with 365-day period
    - Slight warming trend of ~2°C/year
    - Random variations of ±3°C
    
    ### Figures
    
    ![Temperature Trend](figures/temperature_trend.png)
    
    ![Seasonal Decomposition](figures/seasonal_decomposition.png)
    
    ## Reproducibility
    
    All analyses are fully reproducible:
    1. Clone repository
    2. Set up environment
    3. Run data download script
    4. Execute notebooks in order
    ```

34. **Create final summary notebook**:
    
    `notebooks/00_summary.ipynb`:
    ```markdown
    # Temperature Analysis: Summary
    
    ## Project Overview
    Analysis of temperature trends over one year.
    
    ## Methodology
    1. Data generation/collection
    2. Data cleaning and feature engineering
    3. Statistical analysis
    4. Seasonal decomposition
    
    ## Key Results
    - **Trend**: +2°C/year warming
    - **Seasonality**: Clear 365-day cycle
    - **Variability**: ±3°C random fluctuations
    
    ## Notebooks
    - `01_data_exploration.ipynb`: Initial exploration
    - `02_statistical_analysis.ipynb`: Trend analysis
    - `03_seasonal_decomposition.ipynb`: Component analysis
    ```

35. **Commit everything**:
    ```bash
    git add .
    git commit -m "Final updates: README and summary"
    git push origin main
    ```

36. **Create release**:
    - GitHub: Releases → Create new release
    - Tag: `v1.0.0`
    - Title: "Version 1.0.0 - Complete Analysis"
    - Description:
    ```markdown
    ## Complete temperature analysis package
    
    ### Features
    - Data acquisition and processing
    - Statistical trend analysis
    - Seasonal decomposition
    - Comprehensive visualization
    - Fully reproducible workflow
    
    ### How to Use
    See README.md for complete instructions
    ```
    - Publish release

37. **Add DOI (optional)**:
    - Go to Zenodo.org
    - Connect to GitHub
    - Enable repository
    - Release automatically archived

### Part I: Documentation Review 

38. **Create checklist**:
    
    Create `CHECKLIST.md`:
    ```markdown
    # Reproducibility Checklist
    
    - [x] Code in version control (Git/GitHub)
    - [x] Dependencies documented (requirements.txt)
    - [x] Data acquisition documented (download script)
    - [x] Analysis steps documented (notebooks)
    - [x] Random seeds set (in download script)
    - [x] README explains workflow
    - [x] Results can be reproduced
    - [x] Figures generated from code
    - [x] Environment can be recreated
    - [x] Licensed (MIT)
    - [x] Released (v1.0.0)
    ```

39. **Test full reproducibility**:
    
    In a new directory:
    ```bash
    git clone https://github.com/YOUR_USERNAME/temperature-analysis.git
    cd temperature-analysis
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python src/download_data.py
    jupyter notebook
    # Run all notebooks
    ```

### Questions to Reflect On:

1. How does version control improve research reproducibility?
2. What are the benefits of modular code (separate modules vs all in notebooks)?
3. How does documentation help your future self and collaborators?
4. What would you do differently in your next project?
5. How can you apply these practices to your research?

---

## Additional Challenges

### Challenge 1: Add Testing
Create `tests/test_data_processing.py` with unit tests for all functions.

### Challenge 2: Add CI/CD
Create `.github/workflows/tests.yml` to run tests automatically on push.

### Challenge 3: Add Interactive Dashboard
Use Plotly or Streamlit to create interactive visualizations.

### Challenge 4: Improve Documentation
Use Sphinx to generate HTML documentation from docstrings.

### Challenge 5: Add Data Validation
Use libraries like `pandera` or `great_expectations` to validate data quality.

---

## Evaluation Criteria

For each exercise, you should be able to:

1. **Execute successfully**: All commands work without errors
2. **Understand**: Explain what each step does
3. **Troubleshoot**: Debug common issues
4. **Adapt**: Apply concepts to different scenarios
5. **Teach**: Explain concepts to others

---

## Getting Help

If stuck:
1. **Read error messages carefully**: They often tell you what's wrong
2. **Check documentation**: Official docs are authoritative
3. **Search online**: Stack Overflow, GitHub issues
4. **Ask specific questions**: "This command gives this error" vs "It doesn't work"
5. **Use `--help`**: Most commands have built-in help
6. **Check Git status often**: `git status` tells you what's happening

---
## Next Steps

After completing these exercises:

1. **Apply to your research**: Implement in your own projects
2. **Practice regularly**: Make it part of your workflow
3. **Share knowledge**: Help others learn
4. **Stay current**: Tools evolve, keep learning
5. **Contribute**: Contribute to open source projects

---
>**Good luck with the exercises! Remember: programming is learned by doing. Don't be afraid to experiment, make mistakes, and ask questions.**

**Document Version**: 1.0  
**Estimated Total Time**: 6-8 hours
