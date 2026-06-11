# Read csv file and access perticular column using indexing
import pandas as pd
read_student_csv = pd.read_csv("students.csv", usecols=[3])
print(read_student_csv)