import sqlite3

def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            username TEXT,
            history TEXT,
            FOREIGN KEY(username) REFERENCES users(username)
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

def get_chat_history(username):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('SELECT history FROM chat_history WHERE username = ?', (username,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else ""

def save_chat_history(username, history):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO chat_history (username, history) VALUES (?, ?)', (username, history))
    conn.commit()
    conn.close()

def clear_chat_history(username):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('DELETE FROM chat_history WHERE username = ?', (username,))
    conn.commit()
    conn.close()
