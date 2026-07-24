import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
bins = [0,5,10,20,40]

labels = [
    "0-5",
    "6-10",
    "11-20",
    "20+"
]

df["ExperienceGroup"] = pd.cut(
    df["TotalWorkingYears"],
    bins=bins,
    labels=labels
)

result = (
    df.groupby("ExperienceGroup")["MonthlyIncome"]
      .mean()
)

print(result)