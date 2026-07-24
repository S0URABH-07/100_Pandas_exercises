import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
corr = df.corr(numeric_only=True)

print(corr)

print(corr["MonthlyIncome"].sort_values(ascending=False))