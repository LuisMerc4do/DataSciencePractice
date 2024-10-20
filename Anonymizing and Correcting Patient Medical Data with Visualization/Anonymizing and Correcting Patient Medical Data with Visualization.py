import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a Sample dataset with sensitive information

data = {
    'Patient_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Name': ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob Clark', 'Eve Davis'],
    'Age': [45, 34, 29, 40, 51],
    'Diagnosis': ['Diabetes', 'Hypertension', 'Asthma', 'Diabetes', 'Hypertension'],
    'Medical_Bill': [1500, 2500, 1200, 1800, 2200]
}

df = pd.DataFrame(data)

# 2. Print the original dataset
print("Original Dataset")
print(df)

# 3. Anonymize sensitive data(Replace names with unique IDs)
df["Name"] = df["Patient_ID"]

# 4. Introduce data Correction
# Lets assume we discovered a billing error for the second patient
df.loc[df["Patient_ID"] == "P002", "Medical_Bill"] = 2600

# 5. Visualize the corrected and anonymized dataset
print("\n Anonymized and corrected Dataset:")
print(df)

# 6. Data Visualization: Bar plot for medical bills by diagnosis
plt.figure(figsize=(8,5))
df.groupby("Diagnosis")["Medical_Bill"].mean().plot(kind="bar", color=['#4CAF50', '#FF9800', '#2196F3'])
plt.title("Average Medical Bill by Diagnosis (Anonymized Data)")
plt.xlabel("Diagnosis")
plt.ylabel("Average Medical Bill (USD)")
plt.show()