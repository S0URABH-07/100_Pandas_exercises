# Read csv file and remove heading or add indexing

import pandas as pd
read_student_csv = pd.read_csv("students.csv", header=None)
print(read_student_csv)