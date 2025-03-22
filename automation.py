import mysql.connector
import psycopg2

# ✅ MySQL connection details
MYSQL_HOST = "172.21.184.246"
MYSQL_USER = "root"
MYSQL_PASSWORD = "McpadHF656w60YKrxchHFG6y"
MYSQL_DATABASE = "sales"

# ✅ PostgreSQL connection details
POSTGRES_HOST = "172.21.5.101"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "b4vlibNyq4ZkLngPPcG1kvsb"
POSTGRES_DATABASE = "postgres"

# ✅ Function to get last rowid from PostgreSQL
def get_last_rowid():
    try:
        conn = psycopg2.connect(
            database=POSTGRES_DATABASE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port="5432"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT COALESCE(MAX(rowid), 0) FROM sales_data;")
        last_rowid = cursor.fetchone()[0]

        return last_rowid

    except psycopg2.Error as e:
        print("Error fetching last rowid:", e)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()

# ✅ Function to get latest records from MySQL
def get_latest_records(last_rowid):
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        cursor = conn.cursor()

        query = "SELECT rowid, product_id, customer_id, price, quantity, timestamp FROM sales_data WHERE rowid > %s;"
        cursor.execute(query, (last_rowid,))
        new_records = cursor.fetchall()

        return new_records

    except mysql.connector.Error as e:
        print("Error fetching latest records:", e)
        return []

    finally:
        if conn:
            cursor.close()
            conn.close()

# ✅ Function to insert records into PostgreSQL
def insert_records(records):
    try:
        conn = psycopg2.connect(
            database=POSTGRES_DATABASE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port="5432"
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO sales_data (rowid, product_id, customer_id, price, quantity, timestamp) 
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.executemany(insert_query, records)
        conn.commit()

        print(f"{len(records)} records inserted successfully into PostgreSQL!")

    except psycopg2.Error as e:
        print("Error inserting records:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

# ✅ Main execution
if __name__ == "__main__":
    last_rowid = get_last_rowid()
    print("Last rowid in PostgreSQL:", last_rowid)

    new_records = get_latest_records(last_rowid)
    print(f"New rows found in MySQL: {len(new_records)}")

    if new_records:
        insert_records(new_records)
        print(f"New rows inserted into PostgreSQL: {len(new_records)}")
    else:
        print("No new records to insert.")
