import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("Sales Data:")
print(df.head())

# Total Sales
print("Total Sales:", df["Sales"].sum())

# Average Sales
print("Average Sales:", df["Sales"].mean())

# Maximum Sales
print("Maximum Sales:", df["Sales"].max())

# Minimum Sales
print("Minimum Sales:", df["Sales"].min())

# Sales Graph
df["Sales"].plot(kind="bar", title="Sales Analysis")

plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
