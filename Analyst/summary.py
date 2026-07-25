import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
summary = (df.groupby("Department").agg(
          TotalEmployees=("EmployeeNumber", "count"),
          AverageSalary=("MonthlyIncome", "mean"),
          MaxSalary=("MonthlyIncome", "max"),
          MinSalary=("MonthlyIncome", "min"),
          AverageAge=("Age", "mean"),
          AverageExperience=("TotalWorkingYears", "mean")
      )
)

print(summary)