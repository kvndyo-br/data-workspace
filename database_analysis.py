import sqlite3

DATABASE = "data/data.db"

conn = sqlite3.connect(DATABASE)

rows = conn.execute("""
    SELECT customers.name,
           SUM(orders.amount) AS total_spent
    FROM customers
    JOIN orders
        ON customers.id = orders.customer_id
    GROUP BY customers.id, customers.name
    ORDER BY total_spent DESC
""").fetchall()

conn.close()

for name, total_spent in rows:
    print(f"{name}: {total_spent:,.2f}")