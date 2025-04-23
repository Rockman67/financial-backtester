import sqlite3, pathlib

db_path = pathlib.Path("db/finance.db")
db_path.parent.mkdir(exist_ok=True)

with sqlite3.connect(db_path) as conn, open("src/db/schema.sql", encoding="utf-8") as f:
    conn.executescript(f.read())

print("DB created at", db_path.resolve())
