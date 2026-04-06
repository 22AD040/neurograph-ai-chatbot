import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "..", "data")
DB_PATH = os.path.join(DB_DIR, "users.db")

os.makedirs(DB_DIR, exist_ok=True)


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