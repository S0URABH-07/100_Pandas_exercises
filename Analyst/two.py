import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
top10 = (
    df.sort_values("MonthlyIncome", ascending=False)
      [["EmployeeNumber", "JobRole", "Department", "MonthlyIncome"]]
      .head(10)
)

print(top10)