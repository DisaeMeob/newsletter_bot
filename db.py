import sqlite3

def create_table():
    conn = sqlite3.connect('connect.db')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS connect (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE
    )
""")
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('connect.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO connect (user_id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('connect.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM connect')
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]
    