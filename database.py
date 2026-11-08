
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("travel.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            starting_location TEXT NOT NULL,
            destination TEXT NOT NULL,
            days INTEGER NOT NULL,
            budget REAL NOT NULL,
            travelers INTEGER NOT NULL,
            preference TEXT NOT NULL,
            itinerary TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

    print("Travel Planner database initialized successfully!")


if __name__ == "__main__":
    init_db()
