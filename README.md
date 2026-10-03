# E-Commerce Sales Analytics Dashboard

## Project Overview

This project analyzes e-commerce sales data using Python, MySQL, and Power BI to identify sales trends, profit performance, product performance, category performance, and regional performance.

The dashboard also includes a Business Alert System to highlight important business conditions such as profit margin status.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- MySQL
- Power BI
- DAX
- Git & GitHub
## Key Business Insights

- Total Sales: ₹70,600
- Total Profit: ₹10,050
- Total Orders: 5
- Total Quantity Sold: 10
- Overall Profit Margin: 14.24%
- Electronics generated the highest sales.
- South region generated the highest sales.
- Laptop was the highest-selling product by sales.
## Project Structure

```text
ecommerce-sales-analytics/
│
├── data/
│   └── cleaned_orders.csv
│
├── images/
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── sales_by_region.png
│   └── sales_by_product.png
│
├── powerbi/
│   └── ecommerce_sales_dashboard.pbix
│
├── python/
│   └── analysis.py
│
├── sql/
│
└── README.md
## Business Alert System

The dashboard includes a rule-based Business Alert System that monitors the overall profit margin.

- If profit margin is below 10% → ⚠️ Low Profit Margin
- Otherwise → ✅ Healthy Profit Margin
### Sales Dependency Monitor

The Python analysis also monitors sales concentration by category.

- If one category contributes more than 80% of total sales → ⚠️ High Sales Dependency
- Otherwise → ✅ Sales Distribution is Balanced

For the current dataset, Electronics contributes 89.38% of total sales, triggering a High Sales Dependency alert.
## How to Run

1. Start MySQL and make sure the `ecommerce_sales` database is available.
2. Open the project in VS Code.
3. Install the required Python libraries:
   `pip install pandas mysql-connector-python matplotlib`
4. Run the Python analysis:
   `python python/analysis.py`
5. Open the Power BI file from the `powerbi` folder to view the dashboard.
## Future Improvements

- Add sales forecasting.
- Add anomaly detection for unusual sales.
- Add more Business Alerts.
- Connect Power BI directly to MySQL for live data.
- Add more interactive dashboard filters.

## Author

**Manchala Venkatesh**

B.Tech – Computer Science & Engineering