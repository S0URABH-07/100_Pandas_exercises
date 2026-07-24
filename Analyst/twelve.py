import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
avg_salary = df["MonthlyIncome"].mean()
avg_rating = df["PerformanceRating"].mean()

result = df[
    (df["PerformanceRating"] > avg_rating) &
    (df["MonthlyIncome"] < avg_salary)
]

print(result)