import sqlite3

def get_user(uid):
    db = sqlite3.connect("app.db")
    cur = db.cursor()
    query = "SELECT * FROM users WHERE uid = '" + uid + "'"
    cur.execute(query)
    return cur.fetchone()
