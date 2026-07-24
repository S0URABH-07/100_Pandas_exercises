import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
dashboard = (
    df.groupby("Department")
      .agg(
          Employees=("EmployeeNumber", "count"),
          AvgSalary=("MonthlyIncome", "mean"),
          AvgAge=("Age", "mean"),
          AvgExperience=("TotalWorkingYears", "mean"),
          Attrition=("Attrition", lambda x: (x == "Yes").sum())
      )
)

print(dashboard)