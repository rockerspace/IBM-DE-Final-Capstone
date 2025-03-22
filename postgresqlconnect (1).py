# This program requires the python module ibm-db to be installed.
# Install it using the below command
# python3 -m pip install psycopg2




import psycopg2
import pandas as pd

# PostgreSQL connection details
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="b4vlibNyq4ZkLngPPcG1kvsb",
    host="172.21.5.101",
    port=5432
)

cursor = conn.cursor()

# Create sales_data table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    rowid SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    price DECIMAL DEFAULT 0.0 NOT NULL,
    quantity INT NOT NULL,
    "timestamp" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")



conn.commit()
cursor.close()
conn.close()

print("✅ CSV Data Loaded Successfully!")




