import sqlite3

def create_tables(cursor):
    # Створення таблиць
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )
    ''')

def main():
    # Підключення до бази даних
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    create_tables(cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

# запуск
# python create_db.py
