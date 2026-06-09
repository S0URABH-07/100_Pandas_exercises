# Arithmatic operation condition ( <= )

import pandas as pd
S = pd.DataFrame({"A":[10,20,30,40] , "B":[9,18,27,36]})
S["<=30"] = S["A"] <= 30
print(S)