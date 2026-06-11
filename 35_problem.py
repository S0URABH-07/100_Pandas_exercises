# Read csv file and access perticular column using column name
import pandas as pd
read_student_csv = pd.read_csv("students.csv", usecols=["Name"])
print(read_student_csv)