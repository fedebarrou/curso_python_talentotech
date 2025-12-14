import sqlite3

DB_NAME = "inventario.db"

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_NAME)

def init_db() -> None:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
        """)
        conn.commit()
