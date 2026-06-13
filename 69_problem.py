# Fill the Nan value with the Backward value use axis=
import pandas as pd
var = pd.read_csv("students.csv")
print(var.fillna(method="bfill" , axis=1))