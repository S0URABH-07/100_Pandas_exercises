# change Data type
import pandas as pd
S = [11,22,33,44,55]
var = pd.Series(S, dtype=float)
print(var)
print(type(var))