import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
pd.options.mode.chained_assignment = None

path = 'C:\\Users\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\'

df = os.path.join(path, 'SalaryData.csv')

salary_df = pd.read_csv(df, encoding='cp1252')

salary_df['Employee_Name'].replace('', np.nan, inplace=True)
salary_df.dropna(subset=['Employee_Name'], inplace=True)


def select_year(year):
    filterYear = salary_df["CalYear"].isin([year])
    dataByYear = salary_df[filterYear]
    salary_calc = dataByYear.groupby(
        dataByYear['Department']).Annual_Rate.sum()
    return print(salary_calc)


dept = salary_df['Department'].unique()
salary = select_year(2022).to_string()


fig = plt.figure(figsize=(20, 5))
plt.bar(dept, salary, color='blue', width=.2)

plt.xlabel('Departments')
plt.ylabel('Department Wage Budget')

plt.title('Total Amount of Wages Paid Per Metro Department')
plt.show()


# plt.plot(dept, salary, 'o')
# plt.figure(figsize=(20, 5))
# plt.scatter(dept, salary)
# plt.xticks(dept[::1], rotation="vertical")
# plt.xlabel('Department')
# plt.ylabel('Salary Budget')
# plt.show()
