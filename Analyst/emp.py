import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
threshold = df["MonthlyIncome"].quantile(0.90)

result = df[df["MonthlyIncome"] >= threshold]

print(result)