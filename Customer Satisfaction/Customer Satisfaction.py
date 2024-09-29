import pandas as pd

df = pd.read_excel(r"C:\Users\skill\source\repos\Introduction to Data Science\Customer Satisfaction\Customer_Satisfaction_Survey.xlsx")

print(df.head())

print("---------------- Description -----------------")
print(df.describe())

if "Column_Name" in df.columns:
    value_counts = df["Column_Name"].value_counts()
    print("---------- Value counts for the selected Column ----------------")
    print(value_counts)
else:
    print("No columns found in the data set")