# Read csv file and change perticular column data type 

import pandas as pd
read_student_csv = pd.read_csv("students.csv",dtype={"Age":float})
print(read_student_csv)