import sqlite3
import os

os.makedirs("data", exist_ok=True)

DB_PATH = os.path.join("data", "users.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS chats (
    username TEXT,
    chat_id TEXT,
    title TEXT,
    messages TEXT
)
""")

conn.commit()