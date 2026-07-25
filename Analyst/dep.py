import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
dept_total = df.groupby("Department")["MonthlyIncome"].transform("sum")

df["SalaryContribution"] = (df["MonthlyIncome"] / dept_total * 100)

print(df[["Department", "MonthlyIncome", "SalaryContribution"]])