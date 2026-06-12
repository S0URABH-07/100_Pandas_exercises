# convert csv to Numpy array using Numpy

import numpy as np
import pandas as pd
pandas_array = pd.read_csv("students.csv")
arr = np.asarray(pandas_array)
print(arr)