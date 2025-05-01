import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# === STEP 1: Create Database and Insert Sample Data ===

# Create DB only if it doesn't exist
if not os.path.exists("sales_data.db"):
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()

    # Create sales table
    cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Insert sample data
    sample_data = [
        ("Apple", 10, 0.5),
        ("Banana", 20, 0.3),
        ("Orange", 15, 0.7),
        ("Apple", 5, 0.5),
        ("Banana", 10, 0.3),
        ("Orange", 8, 0.7),
        ("Grapes", 12, 1.0),
        ("Apple", 7, 0.5)
    ]

    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
    conn.commit()
    conn.close()
    print("Database and table created with sample data.")
else:
    print("Database already exists. Skipping creation.")

# === STEP 2: Connect and Query Sales Summary ===

conn = sqlite3.connect("sales_data.db")

query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Run query and load into pandas
df = pd.read_sql_query(query, conn)
conn.close()

# === STEP 3: Print and Plot the Result ===

print("\nSales Summary:")
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', color='skyblue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
