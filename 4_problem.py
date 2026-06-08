# Display Last 5 Rows

import pandas as pd

df = pd.read_csv("students.csv")
print(df.tail())