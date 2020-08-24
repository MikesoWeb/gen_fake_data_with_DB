import csv
from time import sleep
from mimesis import Person
import sqlite3


person = Person('ru')
connection = sqlite3.connect('DB_add_data.db')
cursor = connection.cursor()


def add_table(table):
    cursor.execute(f"""
        create table IF NOT EXISTS {table}
        ( name text, family text, age text, email text, password text)
        """)
    print(f'Таблица {table} создана успешно')


"""Заполняю txt файл"""


def gen_to_txt(args, table):
    file_txt = open('base_person_data.txt', 'w', encoding='utf-8')
    for _ in range(args):
        a = str(person.name()),
        b = str(person.last_name()),
        c = str(person.age()),
        d = str(person.email()),
        e = str(person.password().replace('"', '1')).replace(',', '2')
        for j in a, b, c, d, e:
            file_txt.write(str(j).strip(')(').strip(')('))
        file_txt.write('\n')
    file_txt.close()
    add_csv(args, table)


""""""

"""Заполняю csv файл"""


def add_csv(args, table):
    with open('test.csv', 'w', newline='', encoding='utf-8') as file_csv:
        reader = open('base_person_data.txt', encoding='utf-8', newline='')
        for _ in range(args):
            for row in reader.read():
                file_csv.write(row)
    add_csv_to_DB(table)


"""Заполняю базу данных"""


def add_csv_to_DB(table):
    with open('test.csv', encoding='utf-8') as file_to_bd:
        writer_csv = csv.reader(file_to_bd)
        cursor.executemany(f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?)", writer_csv)
        connection.commit()
        print(f'Таблица {table} успешно заполнена')
        question = input('Хотите вывести иформацию из таблицы? Y/N?')
        question_answer_Y = ['Y', 'y']
        question_answer_N = ['N', 'n']
        if (question in question_answer_N):
            print('Программа завершена')

        elif (question in question_answer_Y):
            view_db(table)
        else:
            print('Вы ничего не ввели, программа завершена')


""""""


def drop_table(table):

    cursor.execute(f""" DROP TABLE IF EXISTS {table} """)
    print(f'Таблица {table} очищена!')


def view_db(table):
    sql = f"select * from {table}"
    cursor.execute(sql)
    count = 0
    for i in cursor.fetchall():
        count += 1
        print(count, i)


add_table('test')

sleep(1)

gen_to_txt(15, 'test')

sleep(1)


