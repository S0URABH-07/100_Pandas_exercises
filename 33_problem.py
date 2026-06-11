# Read csv file and access perticular Row
import pandas as pd
read_student_csv = pd.read_csv("students.csv",nrows=4)
print(read_student_csv)