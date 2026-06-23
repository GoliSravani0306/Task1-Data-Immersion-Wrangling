import pandas as pd

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")
df = df.drop_duplicates()

df["Sales_Per_Unit"] = df["Total_Sales"] / df["Quantity"]

df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Data Cleaning Completed Successfully")
