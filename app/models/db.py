import sqlite3
from werkzeug.security import generate_password_hash

DB = "database.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        image TEXT,
        user_id INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS faculty(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        department TEXT,
        assigned_subject TEXT
    )
    """)

    # add assigned_subject column if table exists from older schema
    c.execute("PRAGMA table_info(faculty)")
    cols = [row[1] for row in c.fetchall()]
    if 'assigned_subject' not in cols:
        c.execute("ALTER TABLE faculty ADD COLUMN assigned_subject TEXT")

    c.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        date TEXT,
        time TEXT
    )
    """)

    # seed default admin
    admin = c.execute("SELECT id FROM users WHERE username='admin'").fetchone()
    if not admin:
        hashed = generate_password_hash('admin')
        c.execute("INSERT INTO users(username, password, role) VALUES (?, ?, ?)", ('admin', hashed, 'admin'))

    # seed 8 CSE AIML faculties
    faculty_names = [
        ('CSE Faculty 1', 'Manisha Hatkar'),
        ('CSE Faculty 2', 'Sanjay Patil '),
        ('CSE Faculty 3', 'Vandana Bahera'),
        ('CSE Faculty 4', 'Indrani Bopariker'),
        ('CSE Faculty 5', 'Sarita Khediker'),
        ('CSE Faculty 6', 'Vijila Gnanaraj'),
        ('CSE Faculty 7', 'S. Mahendran')
    ]
    for uname, name in faculty_names:
        user = c.execute("SELECT id FROM users WHERE username=?", (uname,)).fetchone()
        if not user:
            hashed = generate_password_hash('password')
            c.execute("INSERT INTO users(username, password, role) VALUES (?, ?, ?)", (uname, hashed, 'faculty'))
            uid = c.lastrowid
            c.execute("INSERT INTO faculty(user_id, name, department) VALUES (?, ?, ?)", (uid, name, 'CSE AIML'))

    conn.commit()
    conn.close()