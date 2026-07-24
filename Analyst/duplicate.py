import pandas as pd

df = pd.read_csv("HR_Analytics.csv")
duplicates = df[df.duplicated()]

print(duplicates)

print("Total Duplicates:", duplicates.shape[0])