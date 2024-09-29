import pandas as pd
import numpy as np

# Sample dataset to demonstrate data cleaning
data = {
    'Name': ['John Doe', 'Jane Smith', 'John Doe', 'Alice Johnson', np.nan],
    'Date_of_Birth': ['1985-05-20', '1990-07-15', '1985-05-20', '08/12/1988', '1995-10-01'],
    'Credit_Card_Number': ['1234-5678-9012-3456', '9876-5432-1098-7654', np.nan, '4567-8901-2345-6789', '1234-5678-9012-3456']
}

df = pd.DataFrame(data)

# Display the original data
print("-- Original Data --")
print(df)

# Step 1: Identify Missing Values (Before)
print("-- Step 1: Identify missing Values *Before*")
print(df.isnull().sum())

df_no_duplicates = df.drop_duplicates()

# Step 2: Display Data after removing duplicates
print(" -- Step 2: Data After Removing duplicates --")
print(df_no_duplicates)

# Step 3: Standadize data Formats ( Before)
print("-- Data Before Date Formats --")
print(df_no_duplicates)

# Standardizing the date format to YYYY-MM-DD
df_no_duplicates["Date_of_Birth"] = pd.to_datetime(df_no_duplicates["Date_of_Birth"], errors="coerce", format="mixed").dt.strftime("%d/%m/%y")

# Step 3: Display cleaned data with standar Date Format
print("-- Step 3: Data After Standardizing Date Format --")
print(df_no_duplicates)

# Step 4 : Handling NaN Values
df_no_duplicates["Name"] = df_no_duplicates["Name"].fillna(df_no_duplicates['Name'].mode()[0])
df_no_duplicates["Credit_Card_Number"] = df_no_duplicates["Credit_Card_Number"].fillna(df_no_duplicates['Credit_Card_Number'].mode()[0])

# Dropping rows where "Date of Birth" is still NaN
df_no_duplicates = df_no_duplicates.dropna(subset=["Date_of_Birth"])

# Step 4: Display the final cleaned data after handling NaN Values
print("-- Step 4: data After NaN Values --")
print(df_no_duplicates)