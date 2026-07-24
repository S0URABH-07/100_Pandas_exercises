import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
analysis = pd.crosstab(df["OverTime"],df["Attrition"],normalize="index") * 100

print(analysis)