import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
promotion = df[(df["TotalWorkingYears"] > 10) & (df["YearsSinceLastPromotion"] > 5) & (df["PerformanceRating"] == 4)]

print(promotion)