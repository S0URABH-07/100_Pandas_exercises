import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
print("Total Employees :", len(df))

print("Employees Left :", (df["Attrition"] == "Yes").sum())

print("Attrition Rate :",
      round((df["Attrition"] == "Yes").mean() * 100, 2), "%")

print("Average Salary :", df["MonthlyIncome"].mean())

print("Highest Salary :", df["MonthlyIncome"].max())

print("Lowest Salary :", df["MonthlyIncome"].min())

print("Average Age :", round(df["Age"].mean(), 2))

print("Average Experience :", round(df["TotalWorkingYears"].mean(), 2))

print("Most Common Job Role :",
      df["JobRole"].mode()[0])

print("Most Common Department :",
      df["Department"].mode()[0])