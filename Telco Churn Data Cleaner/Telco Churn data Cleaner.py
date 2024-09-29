import pandas as pd
df = pd.read_csv(r"C:\Users\skill\source\repos\Introduction to Data Science\Telco Churn Data Cleaner\Telco_Customer_Churn_Dataset_with_Missing_Values.csv")

print(df.head())
print(df.info())
print(df.describe())

print("-------- MISSING VALUES --------")

# Identify and handle missing value
missing_values = df.isnull().sum()
print(missing_values)

# drop missing values and keep it in the same document dont create a new one
df.dropna(inplace=True)

# Save the cleaned data as new document
df.to_csv(r"C:\Users\skill\source\repos\Introduction to Data Science\Telco Churn Data Cleaner\Telco_Customer_Churn_Dataset_Cleaned.csv", index=False)