# Arithmatic operation

import pandas as pd
S = pd.DataFrame({"A":[1,2,3,4] , "B":[9,8,7,6]})
print(S)
S["C"] = S["A"]+S["B"]
print(S)