import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
Q1 = df["MonthlyIncome"].quantile(0.25)
Q3 = df["MonthlyIncome"].quantile(0.75)

IQR = Q3 - Q1

upper = Q3 + 1.5 * IQR
lower = Q1 - 1.5 * IQR

Upperoutliers = df[df["MonthlyIncome"] > upper]
Loweroutliers = df[df["MonthlyIncome"] < lower]

print(Upperoutliers)
print(Loweroutliers)