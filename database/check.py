import sqlite3

conn = sqlite3.connect("violations.db")

cur = conn.cursor()

cur.execute("SELECT * FROM violations")

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()