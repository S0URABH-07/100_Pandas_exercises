import pandas as pd

df = pd.read_csv("HR_Analytics.csv")

result = (
    df.groupby("Department")["Attrition"]
      .value_counts(normalize=True)
      .mul(100)
      .rename("Attrition Rate")
      .reset_index()
)

print(result[result["Attrition"] == "Yes"])