"""Shared setup for the Day 5 solutions.

The exercises build their working data step by step in the exercise text.
This module reproduces those steps so that every solution script runs on its
own:  ``python exercise_2_1.py``
"""
import random

import matplotlib.pyplot as plt  # noqa: F401
import numpy as np
import pandas as pd
import scipy.stats as stats  # noqa: F401
import seaborn as sns  # noqa: F401

# Exercise 1.1 - synthetic dataset
np.random.seed(42)
n_subjects = 30
n_trials_per_condition = 10
n_rows = n_subjects * n_trials_per_condition * 3

df = pd.DataFrame({
    'subject_id': np.repeat(range(1, n_subjects + 1), n_trials_per_condition * 3),
    'condition': np.tile(['control', 'drug_a', 'drug_b'], n_subjects * n_trials_per_condition),
    'trial': np.tile(range(1, n_trials_per_condition + 1), n_subjects * 3),
    'reaction_time': np.random.normal(350, 80, n_rows),
    'accuracy': np.random.uniform(0.6, 1.0, n_rows),
    'session': np.random.choice(['morning', 'afternoon'], n_rows),
})
df.loc[df['condition'] == 'drug_a', 'reaction_time'] += 30
df.loc[df['condition'] == 'drug_b', 'reaction_time'] -= 20
df.loc[df['session'] == 'afternoon', 'reaction_time'] += 15
df['reaction_time'] = df['reaction_time'].round(1)
df['accuracy'] = df['accuracy'].round(3)

# Exercise 1.2 - introduce missing values
random.seed(42)
df_missing = df.copy()
df_missing.loc[random.sample(range(len(df_missing)), 25), 'reaction_time'] = np.nan
df_missing.loc[random.sample(range(len(df_missing)), 30), 'accuracy'] = np.nan

# Exercise 5.2 - subject demographics
demographics = pd.DataFrame({
    'subject_id': range(1, 31),
    'age': np.random.randint(20, 40, 30),
    'sex': np.random.choice(['M', 'F'], 30),
    'handedness': np.random.choice(['R', 'L'], 30, p=[0.9, 0.1]),
})
