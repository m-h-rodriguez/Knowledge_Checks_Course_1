
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
pd.options.mode.chained_assignment = None

path = 'C:\\Users\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\'

df = os.path.join(path, 'SalaryData.csv')

salary_df = pd.read_csv(df, encoding='cp1252')


# salary_df['Employee_Name'].replace('', np.nan, inplace=True)
# salary_df.dropna(subset=['Employee_Name'], inplace=True)

# salary_df.drop(
#     salary_df[salary_df['CalYear'] != 2022].index, inplace=True)


def agg_2022_salary():
    salary_df['Employee_Name'].replace('', np.nan, inplace=True)
    salary_df.dropna(subset=['Employee_Name'], inplace=True)
    salary_df.drop(salary_df[salary_df['CalYear'] != 2021].index, inplace=True)
    salay_calc = salary_df.groupby(
        salary_df['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

    return print(salay_calc)


agg_2022_salary()


def max_2021_salary(salary_df):
    salary_df['Annual_Rate'] = salary_df['Annual_Rate'].astype(np.int64)
    filterYear = salary_df["CalYear"].isin([2021])
    filterRateMax = salary_df["Annual_Rate"].max()
    dataByYearAsc = salary_df[filterYear]

    dataByYearAsc.sort_values(["Annual_Rate"],
                              axis=0,
                              ascending=[False],
                              inplace=True)

    dataByYearTop = dataByYearAsc[:1]
    return dataByYearTop


print('The highest paid employee of 2022 is: \n', max_2021_salary(salary_df))
