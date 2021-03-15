import sqlite3

db = sqlite3.connect("login.db")

cur = db.cursor()

Users = [
    ("harry", "potter"),
    ("jon", "snow"),
    ("tom", "cat")
]

cur.execute("DROP TABLE users")

cur.execute("CREATE TABLE users(username TEXT, password TEXT)")

cur.executemany("INSERT INTO users VALUES (?,?)", Users)

print("Total {} change made".format(db.total_changes))

db.commit()
db.close()