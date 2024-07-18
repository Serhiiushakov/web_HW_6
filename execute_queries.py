import sqlite3
from tabulate import tabulate

def execute_query(query_file):
    with open(query_file, 'r') as file:
        query = file.read()

    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    conn.close()

    return headers, results

if __name__ == "__main__":
    query_files = [
        #'query_1.sql',   #Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
        #'query_2.sql',  #Знайти студента із найвищим середнім балом з певного предмета.
        #'query_3.sql',  #Знайти середній бал у групах з певного предмета.
        # 'query_4.sql', #Знайти середній бал на потоці (по всій таблиці оцінок).
        # 'query_5.sql', #Знайти які курси читає певний викладач.
        # 'query_6.sql', #Знайти список студентів у певній групі.
        # 'query_7.sql', #Знайти оцінки студентів у окремій групі з певного предмета.
        #  'query_8.sql', #Знайти середній бал, який ставить певний викладач зі своїх предметів.
        #'query_9.sql', #Знайти список курсів, які відвідує студент.
        #'query_10.sql',  # Список курсів, які певному студенту читає певний викладач.
        #'query_11_dod.sql',  # Середній бал, який певний викладач поставить певному студентові.
         'query_12_dod.sql',  # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    ]

    for query_file in query_files:
        print(f"Results for {query_file}:")
        headers, results = execute_query(query_file)
        print(tabulate(results, headers, tablefmt='grid'))
        print("\n")



        #### python execute_queries.py

