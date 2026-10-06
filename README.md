# Introduction to Scientific Programming 🧬🐍

<div align="center">

**Advanced Course for PhD Students in Integrative Neuroscience**  
**University of Coimbra • CNC-UC Polo I**

🕐 **Friday Afternoons • 14 Sessions**  
👨‍🏫 **Coordinator:** [Renato Duarte](mailto:renato.duarte@cnc.uc.pt)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-CNNC--Lab%2Fintscipro-black.svg)](https://github.com/CNNC-Lab/intscipro)

---

</div>

## 🎯 Course Overview

This advanced course is designed to equip students with the programming, computational, and software development skills necessary to produce **reproducible, efficient, and modern scientific analyses**. The course bridges the gap between traditional research programming and professional software development, guiding students from fundamental coding principles to advanced applications in data analysis, visualization, simulation, and machine learning.

### 🔑 Key Features
- **🤖 AI-Assisted Learning**: Integration of modern AI coding tools (Claude Code, GitHub Copilot, ChatGPT) with fundamental programming concepts
- **🔬 Domain-Specific Focus**: Tailored for neuroscience and biological research applications
- **📊 Real-World Applications**: Using authentic research datasets and solving actual scientific problems
- **👥 Collaborative Approach**: Shared GitHub repository with peer contributions and code review
- **🛠️ Professional Skills**: Modern development workflows, version control, and software engineering best practices

## 🗓️ Course Schedule

<table>
<tr><th>#</th><th>📚 Session</th><th>🎯 Focus</th></tr>
<tr><td>1</td><td><strong><a href="day01-introduction/README.md">Introduction & Modern Development Ecosystem</a></strong></td><td>AI-assisted coding, Claude Code demo, environment setup</td></tr>
<tr><td>2</td><td><strong><a href="day02-fundamentals/README.md">Programming Fundamentals</a></strong></td><td>Python basics, data structures</td></tr>
<tr><td>3</td><td><strong><a href="day03-workflows/README.md">Development Tools & Workflow</a></strong></td><td>Git, IDEs, collaboration</td></tr>
<tr><td>4</td><td><strong><a href="day04-numerics/README.md">Numerical Computing Foundations</a></strong></td><td>NumPy, matplotlib, SciPy</td></tr>
<tr><td>5</td><td><strong><a href="day05-data/README.md">Data Manipulation & Analysis</a></strong></td><td>Pandas, data cleaning</td></tr>
<tr><td>6</td><td><strong><a href="day06-visualization/README.md">Visualization & Communication</a></strong></td><td>Publication-quality figures</td></tr>
<tr><td>7</td><td><strong><a href="day07-intermediate/README.md">Intermediate Programming Concepts</a></strong></td><td>Error handling, documentation</td></tr>
<tr><td>8</td><td><strong><a href="day08-machinelearning/README.md">Machine Learning</a></strong></td><td>Statistics, scikit-learn</td></tr>
<tr><td>9</td><td><strong><a href="day09-project-description/README.md">Project Description and Organization</a></strong></td><td>Project planning, organization</td></tr>
<tr><td>10</td><td><strong><a href="day10-neural-networks/README.md">Neural Networks & Deep Learning: From Theory to Biomedical Applications</a></strong></td><td>Deep learning, PyTorch, transformers</td></tr>
<tr><td>11</td><td><strong><a href="day11-simulation/README.md">Simulation & Modeling in Neuroscience</a></strong></td><td>Differential equations, numerical methods, dynamical systems</td></tr>
<tr><td>12</td><td><strong>Student Projects</strong></td><td>Custom research solutions</td></tr>
<tr><td>13</td><td><strong>Student Projects</strong></td><td>Custom research solutions</td></tr>
<tr><td>14</td><td><strong>Student Presentations</strong></td><td>Project showcases</td></tr>
</table>

## 📖 Course Structure

### 🏗️ **Part I: Fundamentals** (Days 1-3)
Building the foundation for modern scientific programming

- **Development Environment Setup**: VS Code, extensions, terminal basics
- **AI-Assisted Coding**: GitHub Copilot, ChatGPT, "vibe coding" techniques
- **Programming Fundamentals**: Variables, control structures, functions, OOP
- **Professional Workflows**: Git, GitHub, documentation, collaboration

### 🔬 **Part II: Scientific Computing Core** (Days 4-7)
Core tools for scientific data analysis

- **Numerical Computing**: NumPy arrays, mathematical operations
- **Data Manipulation**: Pandas for data handling and cleaning
- **Visualization**: matplotlib, seaborn, plotly for scientific figures
- **Code Quality**: Error handling, type hints, debugging strategies

### 🚀 **Part III: Advanced Applications** (Days 8-11)
Specialized tools and advanced techniques

- **Machine Learning**: Statistics, supervised/unsupervised learning, scikit-learn
- **Deep Learning**: Neural networks, PyTorch, transformers
- **Simulation & Modeling**: Differential equations, biological modeling
- **Project Organization**: Planning, structuring and documenting a research project

### 👨‍🎓 **Part IV: Capstone Projects** (Days 12-14)
Applying skills to real research problems: two project work sessions and a final presentation session

## 🛠️ Technology Stack

<div align="center">

| Category | Tools |
|----------|-------|
| **🐍 Core Language** | Python 3.11+ |
| **🔧 Development Environment** | VS Code, Anaconda/conda, Git, Jupyter |
| **🤖 AI Assistants** | Claude Code, GitHub Copilot, ChatGPT |
| **📊 Data Science** | NumPy, Pandas, SciPy, statsmodels |
| **🧠 Machine Learning** | scikit-learn, PyTorch, transformers |
| **📈 Visualization** | matplotlib, seaborn, plotly |
| **🧪 Professional Tools** | pytest, flake8, black, pre-commit, GitHub Actions |

</div>

## 🗂️ Repository Structure

```
intscipro/
├── README.md
├── LICENSE
├── environment.yml          # conda environment: Days 1-9 and 11
├── environment-dl.yml       # conda environment: adds the deep learning stack (Day 10)
├── requirements.txt         # pip equivalent of environment.yml
├── requirements-dl.txt      # pip equivalent of environment-dl.yml
├── datasets/                # small datasets shared across days (see datasets/README.md)
├── resources/               # troubleshooting guide and reference material
└── dayNN-<topic>/           # one folder per session
    ├── README.md            # lecture slides link, session plan, learning goals
    ├── dayNN_handout.md     # written reference for the session
    ├── dayNN_exercises.md   # practice exercises
    ├── notebooks/           # guided Jupyter notebooks (committed without outputs)
    ├── examples/            # short runnable demo scripts
    └── solutions/           # worked solutions
```

Not every day has every folder: Days 10 and 11 are practised through their notebooks, Day 3 exercises are command-line and Git tasks without code solutions, and Day 9 is project planning (README only).

Notebooks are committed **without outputs** (enforced by [`nbstripout`](https://github.com/kynan/nbstripout), see `.pre-commit-config.yaml`); run them to regenerate results. Figures and files created by notebooks and scripts are written to an `outputs/` folder, which is git-ignored.

## 🎯 Learning Objectives

Upon completion of this course, students will be able to:

### 🔧 **Technical Skills**
- ✅ Set up and manage professional scientific development environments
- ✅ Utilize AI-assisted coding tools effectively while understanding fundamentals
- ✅ Implement reproducible research workflows with version control
- ✅ Master numerical computing with NumPy, Pandas, and SciPy
- ✅ Create publication-quality visualizations and figures
- ✅ Apply statistical analyses and machine learning techniques
- ✅ Develop mathematical simulations of biological systems

### 🎓 **Professional Skills**
- ✅ Write clean, documented, and maintainable code
- ✅ Debug and troubleshoot complex programming issues
- ✅ Collaborate effectively using modern development workflows
- ✅ Package and distribute scientific software
- ✅ Apply testing and continuous integration practices

### 🧠 **Research Skills**
- ✅ Transform research questions into computational solutions
- ✅ Analyze complex, multi-dimensional scientific datasets
- ✅ Integrate diverse data types (neural, behavioral, omics)
- ✅ Communicate results through interactive visualizations

## 🚀 Getting Started

### 📥 **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CNNC-Lab/intscipro.git
   cd intscipro
   ```

2. **Install Python environment**:
   ```bash
   # Option A: Using conda (recommended)
   conda env create -f environment.yml
   conda activate scientific-programming

   # Option B: Using pip (Python 3.11+)
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt

   # Day 10 only (deep learning): use environment-dl.yml / requirements-dl.txt instead
   ```

3. **Verify installation**:
   ```bash
   python day01-introduction/demo_scripts/check_installation.py
   ```

4. **Follow Day 1 setup tutorial**: [`day01-introduction/setup_tutorial.md`](day01-introduction/setup_tutorial.md)

### 🎯 **Quick Start Examples**

<details>
<summary><strong>🔍 Simple Data Analysis Example</strong></summary>

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample neuroscience data
data = pd.read_csv('datasets/sample_neuron_data.csv')

# Basic analysis
summary = data.groupby('condition')['spike_count'].describe()
print(summary)

# Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='condition', y='spike_count')
plt.title('Neural Activity by Experimental Condition')
plt.show()
```

</details>

<details>
<summary><strong>🤖 AI-Assisted Coding Example</strong></summary>

```python
# Example prompt for ChatGPT/Copilot:
"""
I have electrophysiological data with columns: neuron_id, condition, 
spike_count, isi_mean, burst_frequency. Please create a comprehensive 
analysis including summary statistics, ANOVA testing, and publication-quality 
visualizations comparing conditions.
"""

# AI will generate complete analysis pipeline
# Students learn to review, understand, and modify AI-generated code
```

</details>

## 📚 Course Materials

### 📖 **Core Resources**
- **Textbooks**: No required textbook - all materials provided in repository
- **Online Platforms**: Jupyter notebooks, GitHub Codespaces support
- **AI Tools**: Free tiers of ChatGPT, GitHub Copilot, Claude
- **Datasets**: Real and synthetic neuroscience datasets from published research

### 🔗 **Recommended Reading**
- [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney
- [Effective Computation in Physics](https://physics.codes/) by Scopatz & Huff  
- [Research Software Engineering with Python](https://merely-useful.tech/py-rse/)

## 💬 Support & Communication

### 📧 **Contact Information**
- **Instructor**: [Renato Duarte](mailto:renato.duarte@cnc.uc.pt)
- **Course Forum**: GitHub Discussions (for technical questions)
- **Office Hours**: Fridays after class (by appointment)

### 🆘 **Getting Help**
1. **Check the FAQ**: [`resources/troubleshooting.md`](resources/troubleshooting.md)
2. **Search Issues**: Look through existing GitHub issues
3. **Ask on Discussions**: Use GitHub Discussions for course-related questions
4. **Emergency Contact**: Email instructor for urgent issues

## 🏆 Assessment & Certification

### 📊 **Grading Structure**
- **Participation & Exercises**: Active participation in the course is strongly encouraged
- **Final Project**: Custom solution to a research problem

### 🎖️ **Project Requirements**
Students will develop a custom computational solution addressing their specific research needs:
- **Proposal**: 1-page project description
- **Implementation**: Coding and analysis
- **Presentation**: 15-minute presentation + code demo
- **Documentation**: Well-documented GitHub repository

---

## 📜 License

This course content is licensed under the [MIT License](LICENSE). Students are free to use, modify, and distribute course materials with proper attribution.

---

<div align="center">

*University of Coimbra • Center for Neuroscience and Cell Biology (CNC)*  
*Empowering the next generation of neuroscientists*

</div>