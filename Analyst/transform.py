import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
job_avg_salary = df.groupby("JobRole")["MonthlyIncome"].transform("mean")

result = df[df["MonthlyIncome"] > job_avg_salary]

print(result[["EmployeeNumber", "JobRole", "MonthlyIncome"]])