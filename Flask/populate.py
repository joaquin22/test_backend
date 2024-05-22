import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
"""
)

# Insertar algunos datos de ejemplo
cursor.execute(
    "INSERT INTO users (name, email, password) VALUES (?, ?, ? )",
    ("admin", "admin@example.com", "admin123"),
)

cursor.execute(
    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
    ("prueba", "prueba@example.com", "prueba123"),
)

conn.commit()
conn.close()
