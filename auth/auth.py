import bcrypt
from auth.db import conn, c

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        c.execute("INSERT INTO users VALUES (?,?)", (username, hashed))
        conn.commit()
        return True
    except:
        return False

def login(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result and bcrypt.checkpw(password.encode(), result[0]):
        return True
    return False