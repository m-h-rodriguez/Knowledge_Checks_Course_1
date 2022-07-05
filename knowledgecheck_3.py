
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
pd.options.mode.chained_assignment = None

path = 'C:\\Users\miche\\OneDrive\\Desktop\\Code Louisville\\knowledge checks\\data_1_checks\\assets\\'

df = os.path.join(path, 'SalaryData.csv')

salary_df = pd.read_csv(df, encoding='cp1252')


def agg_salary(year):
    filterYear = salary_df["CalYear"].isin([year])
    dataByYear = salary_df[filterYear]
    salay_calc = dataByYear.groupby(
        dataByYear['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

    return print(salay_calc)


agg_salary(2018)


def max_salary(year):
    salary_df['Annual_Rate'] = salary_df['Annual_Rate'].astype(
        np.int64)
    filterYear = salary_df["CalYear"].isin([year])
    filterRateMax = salary_df["Annual_Rate"].max()
    dataByYearAsc = salary_df[filterYear]

    dataByYearAsc.sort_values(["Annual_Rate"],
                              axis=0,
                              ascending=[False],
                              inplace=True)

    dataByYearTop = dataByYearAsc[:1]
    return dataByYearTop


print('The highest paid employee of the selected year is: \n',
      max_salary(2016))
