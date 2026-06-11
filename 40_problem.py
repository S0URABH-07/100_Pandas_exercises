# Read csv file and change heading with input names using Names=

import pandas as pd
read_student_csv = pd.read_csv("students.csv", names=["col1","col2","col3","col4","col5"])
print(read_student_csv)
# Extra column heading name 
# Extra column give data as a NaN