import sqlite3
from faker import Faker
import random
from datetime import datetime

def populate_data(cursor):
    faker = Faker()

    # Додавання груп
    group_names = ['Group A', 'Group B', 'Group C']
    for name in group_names:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))

    # Додавання викладачів
    teacher_names = [faker.name() for _ in range(5)]
    for name in teacher_names:
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (name,))

    # Додавання предметів
    subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
    teacher_ids = [row[0] for row in cursor.execute('SELECT id FROM teachers').fetchall()]
    for name in subject_names:
        teacher_id = random.choice(teacher_ids)
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))

    # Додавання студентів
    group_ids = [row[0] for row in cursor.execute('SELECT id FROM groups').fetchall()]
    for _ in range(50):
        name = faker.name()
        group_id = random.choice(group_ids)
        cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))

    # Додавання оцінок
    student_ids = [row[0] for row in cursor.execute('SELECT id FROM students').fetchall()]
    subject_ids = [row[0] for row in cursor.execute('SELECT id FROM subjects').fetchall()]
    for student_id in student_ids:
        for _ in range(20):
            subject_id = random.choice(subject_ids)
            grade = random.randint(60, 100)
            date = faker.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date))

def main():
    # Підключення до бази даних
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    populate_data(cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
# python populate_db.py