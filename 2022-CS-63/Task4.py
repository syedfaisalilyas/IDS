import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

student_names = ['Zainab', 'Farah', 'Zeeshan', 'Hiba', 'Fahad', 'Yasir', 'Mehwish', 'Aqsa', 'Rehan', 'Mariam',
                 'Kashif', 'Lubna', 'Ahsan', 'Samina', 'Imran', 'Shehzad', 'Anila', 'Hamza', 'Arsalan', 'Bushra']
subjects_list = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English Language']
data_dict = {
    'Student_ID': np.random.randint(1000, 2000, 200),
    'Student_Name': np.random.choice(student_names, 200),
    'Subject': np.random.choice(subjects_list, 200),
    'Marks_Obtained': np.random.randint(0, 101, 200),
    'Total_Marks': [100] * 200  
}
df_students = pd.DataFrame(data_dict)
marks_array = df_students['Marks_Obtained'].to_numpy()

mean_marks = np.mean(marks_array)
median_marks = np.median(marks_array)
std_deviation_marks = np.std(marks_array)

top_scorers = df_students[df_students['Marks_Obtained'] > 80]
count_top_scorers = top_scorers.shape[0]

avg_marks_by_subject = df_students.groupby('Subject')['Marks_Obtained'].mean()

plt.figure(figsize=(8, 5))
plt.hist(df_students['Marks_Obtained'], bins=20, color='orange', edgecolor='black', alpha=0.75)
plt.title('Marks Distribution of Students')
plt.xlabel('Marks Obtained')
plt.ylabel('Number of Students')
plt.show()

plt.figure(figsize=(8, 5))
avg_marks_by_subject.plot(kind='bar', color='blue', alpha=0.75)
plt.title('Average Marks by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Marks')
plt.show()

print(f"Mean Marks: {mean_marks:.2f}")
print(f"Median Marks: {median_marks:.2f}")
print(f"Standard Deviation of Marks: {std_deviation_marks:.2f}")
print(f"Number of students scoring above 80: {count_top_scorers}")
print("\nAverage marks by subject:")
print(avg_marks_by_subject)
