import os
import sqlite3

DB_NAME = 'contacts.db'

def get_connection():
    # print("📁 Using DB at:", os.path.abspath(DB_NAME))
    return sqlite3.connect(DB_NAME)

def create_table():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                number TEXT NOT NULL,
                email TEXT NOT NULL)

""")