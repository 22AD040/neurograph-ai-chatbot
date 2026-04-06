import json
from auth.db import conn, c

def save_chat(username, chat_id, title, messages):
    c.execute("REPLACE INTO chats VALUES (?,?,?,?)",
              (username, chat_id, title, json.dumps(messages)))
    conn.commit()

def load_chats(username):
    c.execute("SELECT chat_id, title FROM chats WHERE username=?", (username,))
    return c.fetchall()

def load_messages(username, chat_id):
    c.execute("SELECT messages FROM chats WHERE username=? AND chat_id=?",
              (username, chat_id))
    result = c.fetchone()
    return json.loads(result[0]) if result else []