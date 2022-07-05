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
salary_df.drop(salary_df[salary_df['CalYear'] != 2022].index, inplace=True)

depts = salary_df['Department'].unique()
salary_df['Annual_Rate'] = salary_df['Annual_Rate'].astype(float)
salary = salary_df.groupby(['Department'])['Annual_Rate'].sum()

print(depts)

plt.bar(depts, salary)
plt.title('Louisville Metro Salary Budget By Department in 2022')
plt.xlabel('Year')
plt.ylabel('Salary Budget')
plt.xticks(depts[::1], rotation="vertical")
plt.gca().set_yticklabels(['${:,.0f}'.format(x)
                           for x in plt.gca().get_yticks()])
plt.show()


# plt.plot(dept, salary, 'o')
# plt.figure(figsize=(20, 5))
# plt.scatter(dept, salary)
# plt.xticks(dept[::1], rotation="vertical")
# plt.xlabel('Department')
# plt.ylabel('Salary Budget')
# plt.show()
