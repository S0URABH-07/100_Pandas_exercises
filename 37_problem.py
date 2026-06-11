# Read csv file and change index name with column data
import pandas as pd
read_student_csv = pd.read_csv("students.csv", index_col="Name")
print(read_student_csv)