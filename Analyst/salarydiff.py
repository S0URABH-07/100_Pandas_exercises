import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
company_avg = df["MonthlyIncome"].mean()
df["SalaryDifference"] = df["MonthlyIncome"] - company_avg

print(df[["EmployeeNumber" , "MonthlyIncome","SalaryDifference"]])