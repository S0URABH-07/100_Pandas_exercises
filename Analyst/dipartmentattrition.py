import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
result = (df.groupby("Department").agg(TotalEmployees=("EmployeeNumber", "count"),EmployeesLeft=("Attrition", lambda x: (x == "Yes").sum())))

result["AttritionRate"] = (result["EmployeesLeft"] /result["TotalEmployees"] * 100)

print(result)