import sqlite3

conn = sqlite3.connect("violations.db")

cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS violations(

id INTEGER PRIMARY KEY,

plate TEXT,

severity INTEGER,

confidence REAL,

timestamp TEXT,

action TEXT,

image_path TEXT

)

""")

conn.commit()

conn.close()

print("Database Ready")