import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
salary = (
    df.groupby("JobRole")["MonthlyIncome"].mean().sort_values(ascending=False)
)

print(salary)