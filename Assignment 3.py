import os
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data preparation
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, 'students_scores.csv')

# create sample data
names = ['Aisha', 'Daniyar', 'Zarina', 'Arman', 'Gulnur', 'Bekzat', 'Saltanat', 'Nursultan', 'Madina', 'Yerlan',
         'Aizat', 'Timur', 'Moldir', 'Azat', 'Diana', 'Sanzhar', 'Ainur', 'Marat', 'Kamila', 'Dauren']
genders = ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
           'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male']
groups = ['SE-101', 'SE-101', 'SE-102', 'SE-102', 'SE-103', 'SE-103', 'SE-101', 'SE-102', 'SE-103', 'SE-101',
          'SE-102', 'SE-103', 'SE-101', 'SE-102', 'SE-103', 'SE-101', 'SE-102', 'SE-103', 'SE-101', 'SE-102']

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['student_id', 'name', 'gender', 'group', 'math_score', 'python_score', 'english_score'])
    for i, name in enumerate(names):
        writer.writerow([i + 1, name, genders[i], groups[i], 
                         random.randint(45, 100), random.randint(40, 100), random.randint(50, 100)])

#task 1
print("Task 1: OS Module")
if not os.path.exists(filepath):
    print(f"Error: File {filepath} not found!")
    exit()
else:
    print(f"File found: {filepath}")
    print(f"Absolute path: {os.path.abspath(filepath)}\n")


#task 2
print("Task 2: CSV Module")
with open(filepath, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print(f"Fields: {reader.fieldnames}")
    
    rows = list(reader)
    for i, row in enumerate(rows[:5]):
        print(f"Row {i+1}: {row}")
    
    print(f"Total students: {len(rows)}\n")


#task 3
print("Task 3: Pandas Analysis")

# 3a
df = pd.read_csv(filepath)
print("First 5 rows:\n", df.head())
print(f"Shape: {df.shape}")
print("Data types:\n", df.dtypes)

# 3b
print("\nSummary Statistics:\n", df.describe())
for col in ['math_score', 'python_score', 'english_score']:
    print(f"{col} - Mean: {df[col].mean():.2f}, Median: {df[col].median()}, Std: {df[col].std():.2f}")

# 3c
df['average_score'] = df[['math_score', 'python_score', 'english_score']].mean(axis=1).round(2)
print("\nUpdated DataFrame (Partial):\n", df[['name', 'group', 'average_score']].head())

# 3d
print("\nStudents with average >= 75:\n", df[df['average_score'] >= 75])
print("\nStudents in SE-101:\n", df[df['group'] == 'SE-101'])

# 3e
group_means = df.groupby('group')[['math_score', 'python_score', 'english_score']].mean()
gender_means = df.groupby('gender')['average_score'].mean()
print("\nGroup Means:\n", group_means)
print("\nGender Means:\n", gender_means)


#task 4
sns.set_theme(style="whitegrid")

# Plot 1
plt.figure(figsize=(8, 5))
avg_by_group = df.groupby('group')['average_score'].mean()
plt.bar(avg_by_group.index, avg_by_group.values, color=['#3498DB', '#E74C3C', '#2ECC71'])
plt.title('Average Score by Study Group')
plt.xlabel('Study Group')
plt.ylabel('Average Score')
plt.savefig(os.path.join(data_dir, 'bar_group_avg.png'), bbox_inches='tight')
plt.close()

# Plot 2
plt.figure(figsize=(8, 5))
plt.hist(df['python_score'], bins=10, color='#9B59B6', edgecolor='white')
plt.title('Distribution of Python Scores')
plt.xlabel('Python Score')
plt.ylabel('Number of Students')
plt.savefig(os.path.join(data_dir, 'hist_python_scores.png'), dpi=150, bbox_inches='tight')
plt.close()

# Plot 3
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='gender', y='average_score', palette='Set2')
plt.title('Score Distribution by Gender')
plt.savefig(os.path.join(data_dir, 'box_gender_scores.png'), dpi=150, bbox_inches='tight')
plt.close()

# Plot 4
plt.figure(figsize=(8, 6))
corr = df[['math_score', 'python_score', 'english_score', 'average_score']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Student Scores')
plt.savefig(os.path.join(data_dir, 'heatmap_correlation.png'), dpi=150, bbox_inches='tight')
plt.close()

print("\nVisualizations saved in 'data/' folder.")