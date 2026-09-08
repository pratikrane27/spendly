import sqlite3
from werkzeug.security import generate_password_hash

DB_PATH = "spendly.db"

def get_db():
    """
    Returns a SQLite connection with row_factory and foreign keys enabled.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """
    Creates the users and expenses tables.
    """
    with get_db() as conn:
        # Users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)

        # Expenses table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        conn.commit()

def seed_db():
    """
    Inserts sample data for development.
    """
    with get_db() as conn:
        # Check if already seeded
        cursor = conn.execute("SELECT id FROM users LIMIT 1")
        if cursor.fetchone():
            return

        # Seed demo user
        password_hash = generate_password_hash("password123")
        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", password_hash)
        )
        user_id = cursor.lastrowid

        # Seed 8 sample expenses across all categories
        # Categories: Food, Transport, Bills, Health, Entertainment, Shopping, Other
        sample_expenses = [
            (user_id, 15.50, "Food", "2026-09-01", "Lunch at cafe"),
            (user_id, 12.00, "Food", "2026-09-02", "Coffee and bagel"),
            (user_id, 20.00, "Transport", "2026-09-03", "Uber to office"),
            (user_id, 100.00, "Bills", "2026-09-04", "Electricity bill"),
            (user_id, 50.00, "Health", "2026-09-05", "Pharmacy"),
            (user_id, 30.00, "Entertainment", "2026-09-06", "Movie ticket"),
            (user_id, 60.00, "Shopping", "2026-09-07", "New t-shirt"),
            (user_id, 10.00, "Other", "2026-09-08", "Small gift"),
        ]

        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            sample_expenses
        )
        conn.commit()
