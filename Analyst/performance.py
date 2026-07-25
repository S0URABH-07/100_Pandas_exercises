import pandas as pd
import numpy as np

df = pd.read_csv("HR_Analytics.csv")
df["PerformanceCategory"] = np.where(df["PerformanceRating"] >= 4,"High Performer","Average Performer")

print(df[["EmployeeNumber", "PerformanceRating", "PerformanceCategory"]])