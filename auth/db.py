import sqlite3

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