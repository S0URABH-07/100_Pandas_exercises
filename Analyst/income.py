import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
result = (df.sort_values("MonthlyIncome", ascending=False).groupby("Department").head(3))

print(result)