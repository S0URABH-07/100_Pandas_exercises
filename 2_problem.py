# Create a DataFrame
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "John"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)