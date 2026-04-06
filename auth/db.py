import sqlite3
import os
os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)""")

c.execute("""CREATE TABLE IF NOT EXISTS chats (
    username TEXT,
    chat_id TEXT,
    title TEXT,
    messages TEXT
)""")

conn.commit()