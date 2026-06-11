# Read csv file and skip some rows using rows number
import pandas as pd
read_student_csv = pd.read_csv("students.csv", skiprows=[1,3])
print(read_student_csv)