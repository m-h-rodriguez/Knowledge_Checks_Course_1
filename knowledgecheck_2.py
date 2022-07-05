import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os


path = 'C:\\Users\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\'

df = os.path.join(path, 'SalaryData.csv')

salary_df = pd.read_csv(df, encoding='cp1252')
print(salary_df.head())
print(salary_df.tail())


def year(salary): return salary_df['CalYear']


year(2020)


dept = salary_df['Department'].unique()
salary = salary_df.groupby(year, ['Department'])['Annual_Rate'].sum()


plt.plot(dept, salary, 'o')
plt.figure(figsize=(20, 5))
plt.scatter(dept, salary)
plt.xticks(dept[::1], rotation="vertical")
plt.xlabel('Department')
plt.ylabel('Salary Budget')
plt.show()
