import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
df["RiskScore"] = 0

df.loc[df["OverTime"] == "Yes", "RiskScore"] += 3

df.loc[df["WorkLifeBalance"] <= 2, "RiskScore"] += 2

df.loc[df["YearsSinceLastPromotion"] > 5, "RiskScore"] += 2

df.loc[df["JobSatisfaction"] <= 2, "RiskScore"] += 3

print(df.sort_values("RiskScore", ascending=False)[["EmployeeNumber", "Department", "JobRole", "RiskScore"]].head(20))