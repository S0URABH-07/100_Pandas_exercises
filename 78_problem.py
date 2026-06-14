# Only interpolate() fills missing values in numeric columns.
# It does not fill missing values in text
import pandas as pd
var = pd.read_csv("Test.csv")
print(var)
print(var.interpolate(limit_direction="both", limit=2 ,method="linear" ,axis=0))