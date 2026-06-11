# if you want to fetch some data in csv file Use--> describe() fnxn this fnxn give the data like : (count, mean, std, min, 25%, 50%, 75%, max)
import pandas as pd
fetch_data = pd.read_csv("students.csv")
print(fetch_data.describe())