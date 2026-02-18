import sqlite3

DB_NAME = "career.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        total_xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,

        frontend_xp INTEGER DEFAULT 0,
        backend_xp INTEGER DEFAULT 0,
        ai_xp INTEGER DEFAULT 0,
        devops_xp INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def create_demo_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", ("demo",))
    user = cursor.fetchone()

    if not user:
        cursor.execute("""
        INSERT INTO users (username)
        VALUES (?)
        """, ("demo",))
        conn.commit()

    conn.close()
