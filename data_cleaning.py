import pandas as pd

# Read the dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City values with Unknown
df["City"] = df["City"].fillna("Unknown")

# Save cleaned dataset
df.to_excel("cleaned_sales_dataset.xlsx", index=False)

print("\nData cleaning completed successfully!")