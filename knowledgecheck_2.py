import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os


df = pd.read_csv(os.path.join(os.path.dirname(
    __file__), 'assets', 'SalaryData'.csv))

# df = pd.read_csv(
#     "C:\\Users\\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\SalaryData.csv", encoding='unicode_escape')

print(df.head())
print(df.tail())


def year(salary): return df['CalYear']


year(2020)


dept = df['Department'].unique()
salary = df.groupby(year, ['Department'])['Annual_Rate'].sum()


plt.plot(dept, salary, 'o')
plt.figure(figsize=(20, 5))
plt.scatter(dept, salary)
plt.xticks(dept[::1], rotation="vertical")
plt.xlabel('Department')
plt.ylabel('Salary Budget')
plt.show()
