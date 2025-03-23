import sqlite3

conn = sqlite3.connect('price_data.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS prices (date TEXT, price INTEGER)')

cursor.execute("INSERT INTO prices VALUES ('2025-03-22', 2550)")
cursor.execute("INSERT INTO prices VALUES ('2025-03-23', 2600)")
cursor.execute("INSERT INTO prices VALUES ('2025-03-24', 2700)")
cursor.execute("INSERT INTO prices VALUES ('2025-03-25', 2650)")

conn.commit()
conn.close()

print("✅ Database and table created successfully with sample data")
