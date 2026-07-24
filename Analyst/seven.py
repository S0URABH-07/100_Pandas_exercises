import pandas as pd

df = pd.read_csv("HR_Analytics.csv")

bins = [0, 5000, 10000, 15000, 25000]

labels = [
    "Low",
    "Medium",
    "High",
    "Executive"
]

df["SalaryBand"] = pd.cut(
    df["MonthlyIncome"],
    bins=bins,
    labels=labels
)

print(df["SalaryBand"].value_counts())