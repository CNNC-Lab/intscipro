# Exercise 2 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Fast and accurate responses
fast_responses = df[df['reaction_time'] < 300]
print(f"Fast responses (<300ms): {len(fast_responses)}")

high_accuracy = df[df['accuracy'] > 0.9]
print(f"High accuracy (>0.9): {len(high_accuracy)}")

fast_and_accurate = df[(df['reaction_time'] < 300) & (df['accuracy'] > 0.9)]
print(f"Fast AND accurate: {len(fast_and_accurate)}")
print(f"Percentage of trials: {len(fast_and_accurate)/len(df)*100:.1f}%\n")

# b) Specific subject and condition
subject_15_drug_a = df[(df['subject_id'] == 15) & (df['condition'] == 'drug_a')]
print(f"Subject 15, drug_a condition: {len(subject_15_drug_a)} trials")
print(subject_15_drug_a[['trial', 'reaction_time', 'accuracy']].head())
print()

# c) Morning trials with specific RT range
morning_medium_rt = df[
    (df['session'] == 'morning') & 
    (df['reaction_time'] >= 300) & 
    (df['reaction_time'] <= 400)
]
print(f"Morning trials, RT 300-400ms: {len(morning_medium_rt)}")
print(f"Mean RT: {morning_medium_rt['reaction_time'].mean():.1f}ms")
print(f"Mean accuracy: {morning_medium_rt['accuracy'].mean():.3f}\n")

# d) Problematic trials (OR condition)
problematic = df[(df['accuracy'] < 0.7) | (df['reaction_time'] > 500)]
print(f"Problematic trials (low acc OR high RT): {len(problematic)}")
print(f"Percentage: {len(problematic)/len(df)*100:.1f}%")

# Breakdown
low_acc_only = df[(df['accuracy'] < 0.7) & (df['reaction_time'] <= 500)]
high_rt_only = df[(df['accuracy'] >= 0.7) & (df['reaction_time'] > 500)]
both = df[(df['accuracy'] < 0.7) & (df['reaction_time'] > 500)]

print(f"  - Low accuracy only: {len(low_acc_only)}")
print(f"  - High RT only: {len(high_rt_only)}")
print(f"  - Both issues: {len(both)}")

# e) Summary table
print("\n=== FILTERING SUMMARY ===")
filters = {
    'Total trials': len(df),
    'Fast responses (<300ms)': len(fast_responses),
    'High accuracy (>0.9)': len(high_accuracy),
    'Fast AND accurate': len(fast_and_accurate),
    'Subject 15, drug_a': len(subject_15_drug_a),
    'Morning, RT 300-400ms': len(morning_medium_rt),
    'Problematic trials': len(problematic)
}

summary_df = pd.DataFrame.from_dict(filters, orient='index', columns=['Count'])
summary_df['Percentage'] = (summary_df['Count'] / len(df) * 100).round(1)
print(summary_df)
