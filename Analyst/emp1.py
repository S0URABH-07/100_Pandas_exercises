import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
risk = df[(df["OverTime"] == "Yes") & (df["JobSatisfaction"] <= 2) & (df["WorkLifeBalance"] <= 2) & (df["Attrition"] == "Yes")]

print(risk)