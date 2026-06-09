# Add two series
import pandas as pd
s1 = pd.Series(12, index=[0,1,2,3,4,5,6,7,8])
s2 = pd.Series(12 , index=[1,2,3,4,5,6])
print(s1+s2)