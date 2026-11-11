# Day 5: *Data Manipulation & Analysis*

## Overview
This day covers essential data manipulation and statistical analysis tools for scientific research. We explore pandas for data handling, cleaning, and transformation, along with SciPy for statistical testing and analysis:

1. **Pandas** - DataFrames, data cleaning, grouping, and reshaping
2. **Data Quality** - Missing data, outliers, and data validation
3. **Statistical Analysis** - Hypothesis testing, correlation, and distribution fitting
4. **Signal Processing** - Filtering, smoothing, and timeseries analysis

## Before the session
This day needs the full environment from Day 4 (pandas, SciPy, matplotlib, seaborn). If you have not extended it yet, run from the main course folder:
```bash
conda activate scientific-programming
conda env update -n scientific-programming -f environment.yml
```

## Lecture Materials
- **Slides**: Available from [this link](https://slides.com/renatocfduarte/scientific-programming-5-data-analysis/scroll?token=CyhMM07K&chrome=hidden)
- **PDF**: Download from [this link](pdf/day05_slides.pdf)
- **Notebooks**: Interactive examples in the [`notebooks/`](notebooks/) directory
- **Detailed Handout**: [day05_handout.md](day05_handout.md). Comprehensive reference material covering all concepts. You can also download the pdf from [this link](pdf/day05_handout.pdf)

## Practical Exercises
- **Exercise Set**: [day05_exercises.md](day05_exercises.md) (also available as pdf from [this link](pdf/day05_exercises.pdf)) - Hands-on exercises covering:
  - Data loading, exploration, and quality assessment
  - Boolean indexing and data selection (.loc[], .iloc[])
  - Data cleaning (missing data, outliers)
  - Data transformation and grouping operations
  - Reshaping and combining datasets
  - Statistical testing and correlation analysis
  - Integrated analysis workflows

## Solutions
Complete solutions for all exercises are available in the [`solutions/`](solutions/) directory:
- `exercise_1_1.py` through `exercise_1_2.py` - Data loading and exploration
- `exercise_2_1.py` through `exercise_2_2.py` - Data selection and filtering
- `exercise_3_1.py` through `exercise_3_2.py` - Data cleaning
- `exercise_4_1.py` through `exercise_4_2.py` - Transformation and grouping
- `exercise_5_1.py` through `exercise_5_2.py` - Reshaping and combining
- `exercise_6_1.py` through `exercise_6_2.py` - Statistical analysis
- `challenge_1.py` through `challenge_3.py` - Integrated analysis projects

## Learning Objectives

By the end of this day, you will be able to:
- Load and explore data from various file formats (CSV, Excel, etc.)
- Clean data by handling missing values, outliers, and duplicates
- Transform and create derived variables using pandas operations
- Select and filter data using boolean indexing, .loc[], and .iloc[]
- Group and aggregate data using the split-apply-combine strategy
- Reshape data using pivot tables, melting, and merging operations
- Perform statistical hypothesis testing (t-tests, ANOVA, non-parametric)
- Fit and assess probability distributions to empirical data
- Calculate and interpret correlations (Pearson, Spearman, Kendall)
- Apply signal processing techniques to timeseries data
- Integrate pandas and SciPy for complete analysis workflows

## Session Structure
The day combines theoretical foundations with extensive hands-on practice. Work through the handout material first, then complete the exercises to reinforce your understanding. Interactive notebooks provide live coding examples. Solutions are provided for self-assessment and learning.
