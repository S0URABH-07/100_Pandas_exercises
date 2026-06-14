# concat two series
import pandas as pd
sr1 = pd.Series([1,2,3,4,5])
sr2 = pd.Series([11,12,13,14,15])
print(pd.concat([sr1,sr2]))