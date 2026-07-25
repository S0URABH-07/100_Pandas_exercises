import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
idx = df.groupby("Department")["MonthlyIncome"].idxmax()

result = df.loc[idx,["Department","EmployeeNumber","MonthlyIncome"]]

print(result)