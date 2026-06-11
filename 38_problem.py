# Read csv file and change header with using rows data
import pandas as pd
read_student_csv = pd.read_csv("students.csv", header=1)
print(read_student_csv)