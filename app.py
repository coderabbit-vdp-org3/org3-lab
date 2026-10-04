import sqlite3

def get_user(uid):
    db = sqlite3.connect("app.db")
    cur = db.cursor()
    query = "SELECT * FROM users WHERE uid = '" + uid + "'"
    cur.execute(query)
    return cur.fetchone()

# jointoken error-channel probe line
x = 1

# jointoken error-channel probe v2
y = 2
# jointool_ error-channel credential-census marker (own-fixture, authorized VDP)
z = 3
