import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

np.random.seed(42)

employee_names = [ 'Zainab','Ayesha', 'Ahmed', 'Hassan', 'Fatima', 'Ali', 'Sara', 'Usman', 'Amina', 'Bilal',
                  'Hina', 'Farhan', 'Rabia', 'Kamran', 'Asma', 'Tariq', 'Nida', 'Sana', 'Shahid', 'Naveed']

departments_list = ['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Economics', 
                    'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Business Administration']

data = {
    'Employee ID': np.arange(1, 301),
    'Employee Name': np.random.choice(employee_names, 300),
    'Department': np.random.choice(departments_list, 300),
    'Annual Salary': np.random.uniform(30000, 120000, 300),
    'Experience (Years)': np.random.randint(1, 26, 300)
}

df = pd.DataFrame(data)

salary_array = df['Annual Salary'].to_numpy()

avg_salary = np.mean(salary_array)
highest_salary = np.max(salary_array)
lowest_salary = np.min(salary_array)

experienced_high_salary_employees = df[(df['Experience (Years)'] > 5) & (df['Annual Salary'] > avg_salary)]

avg_salary_by_department = df.groupby('Department')['Annual Salary'].mean()

plt.figure(figsize=(8, 5))
avg_salary_by_department.plot(kind='bar', color='teal', alpha=0.7)
plt.title('Average Annual Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary ($)')
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df['Experience (Years)'], df['Annual Salary'], marker='o', linestyle='-', color='blue', alpha=0.6)
plt.title('Annual Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Annual Salary ($)')
plt.show()


print("Summary Statistics of Employee Salaries:")
print(f"Average Salary: ${avg_salary:.2f}")
print(f"Highest Salary: ${highest_salary:.2f}")
print(f"Lowest Salary: ${lowest_salary:.2f}")

print("\nEmployees with more than 5 years of experience and earning above average salary:")
print(experienced_high_salary_employees[['Employee ID', 'Employee Name', 'Department', 'Annual Salary', 'Experience (Years)']].head())

print("\nAverage Salary by Department:")
print(avg_salary_by_department)