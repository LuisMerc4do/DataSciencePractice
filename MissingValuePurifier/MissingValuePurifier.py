import pandas as pd
import numpy as np

# Ceate data
data = {"A" : [1, 3, np.nan], "B": [np.nan, 5, 7], "C":[3, np.nan, 9]}
df = pd.DataFrame(data)

# show dataframe before dropping rows
print("Dataframe before dropping values:")
print(df)

# Getting rid of missing values
print("Missing Values:")
print(df.isnull().sum())

#drop missing values
df.dropna(inplace=True)

#Show Dataframe after dropping rows
print("\n DataFame after dropping missing values:")
print(df)