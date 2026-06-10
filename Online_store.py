import sqlite3
conn=sqlite3.connect("store.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
               product_id INTEGER PRIMARY KEY,
               product_name TEXT,
               stock INTEGER
               )""")
cursor.execute("INSERT INTO products VALUES(102,'Laptop',20)")
try:
    quantity=2
    cursor.execute("""
                   UPDATE products SET stock=stock-? WHERE product_id=102""",(quantity,))
    cursor.execute("""
                   UPDATE products SET stock=stock+1 WHERE product_id=102""")
    conn.commit()
except Exception:
    print("Purchase Failed!")
    conn.rollback()
    print("Rollback completed")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print (row)
conn.close()