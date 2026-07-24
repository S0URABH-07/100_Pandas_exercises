import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
result = (df.groupby("JobRole")["Attrition"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
)

print(result)