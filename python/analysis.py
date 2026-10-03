import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourNewStrongPassword@2026",
    database="ecommerce_sales"
)

query = "SELECT * FROM orders"

df = pd.read_sql(query, connection)
df["order_date"] = pd.to_datetime(df["order_date"])
print(df.isnull().sum())

print(df)
print(df.dtypes)

connection.close()
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Total Sales:", df["sales"].sum())
print("Total Profit:", df["profit"].sum())
print("Total Quantity Sold:", df["quantity"].sum())
category_sales = df.groupby("category")["sales"].sum()

print("\nSales by Category:")
print(category_sales)
category_profit = df.groupby("category")["profit"].sum()

print("\nProfit by Category:")
print(category_profit)
region_sales = df.groupby("region")["sales"].sum()

print("\nSales by Region:")
print(region_sales)
product_sales = df.groupby("product_name")["sales"].sum().sort_values(ascending=False)

print("\nSales by Product:")
print(product_sales)
monthly_sales = df.groupby(df["order_date"].dt.month)["sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
profit_margin = (df["profit"].sum() / df["sales"].sum()) * 100

print("\nOverall Profit Margin:", round(profit_margin, 2), "%")
import matplotlib.pyplot as plt

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/sales_by_category.png")
plt.show()
profit_category = df.groupby("category")["profit"].sum()

profit_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("images/profit_by_category.png")
plt.show()
region_sales = df.groupby("region")["sales"].sum()

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/sales_by_region.png")
plt.show()
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/sales_by_product.png")
plt.show()
print("\n========== BUSINESS SUMMARY ==========")
print(f"Total Sales: ₹{df['sales'].sum():,.2f}")
print(f"Total Profit: ₹{df['profit'].sum():,.2f}")
print(f"Total Quantity Sold: {df['quantity'].sum()}")
print(f"Total Orders: {df['order_id'].nunique()}")
print(f"Profit Margin: {profit_margin:.2f}%")
df.to_csv("data/cleaned_orders.csv", index=False)
print("\n========== BUSINESS HEALTH MONITOR ==========")

if profit_margin < 10:
    print("🔴 HIGH ALERT: Profit margin is below 10%")
elif profit_margin < 15:
    print("🟡 WARNING: Profit margin needs attention")
else:
    print("🟢 BUSINESS HEALTH: Stable")

health_status = (
    "HIGH ALERT"
    if profit_margin < 10
    else "WARNING"
    if profit_margin < 15
    else "STABLE"
)

print("Health Status:", health_status)
category_percentage = (category_sales / df["sales"].sum()) * 100

top_category = category_percentage.idxmax()
top_category_share = category_percentage.max()

print("\n========== SALES DEPENDENCY MONITOR ==========")

if top_category_share > 80:
    print(f"⚠️ HIGH SALES DEPENDENCY: {top_category} contributes {top_category_share:.2f}% of total sales")
else:
    print(f"✅ SALES DISTRIBUTION: No category exceeds 80% of total sales")