import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
df["DepartmentSalaryRank"] = (df.groupby("Department")["MonthlyIncome"].rank(method="dense", ascending=False))

print(df[["Department", "EmployeeNumber", "MonthlyIncome", "DepartmentSalaryRank"]])