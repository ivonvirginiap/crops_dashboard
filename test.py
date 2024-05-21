import sqlite3

def check_users():
    conn = sqlite3.connect('crops.db')
    cursor = conn.cursor()
    # cursor.execute("PRAGMA table_info(padi)")
    cursor.execute("SELECT * from padi limit 5")
    users = cursor.fetchall()
    for user in users:
        print(user)
    cursor.close()
    conn.close()

check_users()
