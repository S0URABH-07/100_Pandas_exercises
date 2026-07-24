import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
result = (
    df.pivot_table(
        values="MonthlyIncome",
        index="Department",
        columns="Gender",
        aggfunc="mean"
    )
)

print(result)