import sqlite3
from datetime import datetime

DB_NAME = "career.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        career_path TEXT NOT NULL,
        level INTEGER DEFAULT 1,
        total_xp INTEGER DEFAULT 0,
        frontend_xp INTEGER DEFAULT 0,
        backend_xp INTEGER DEFAULT 0,
        database_xp INTEGER DEFAULT 0,
        system_design_xp INTEGER DEFAULT 0,
        streak INTEGER DEFAULT 0,
        last_active_date TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # MISSIONS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS missions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        difficulty INTEGER NOT NULL,
        category TEXT NOT NULL,
        skill_type TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    # BADGES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS badges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        badge_name TEXT NOT NULL,
        unlocked BOOLEAN DEFAULT 0,
        date_unlocked TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    conn.commit()
    conn.close()


def create_demo_user():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", ("demo",))
    user = cursor.fetchone()

    if not user:
        cursor.execute("""
        INSERT INTO users (username, career_path)
        VALUES (?, ?)
        """, ("demo", "Full Stack"))

        conn.commit()

    conn.close()
