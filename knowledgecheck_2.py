import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:\\Users\\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\SalaryData.csv", encoding='unicode_escape')

# print(df.head())
# print(df.tail())


dept = df['Department'].unique()
salary = df.groupby(['Department'])['Annual_Rate'].sum()

print(dept)

plt.plot(dept, salary, 'o')
plt.figure(figsize=(20, 5))
plt.scatter(dept, salary)
plt.xticks(dept[::1], rotation="vertical")
plt.xlabel('Department')
plt.ylabel('Salary Budget')
plt.show()
