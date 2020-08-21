import csv
from mimesis import Person
import sqlite3

person = Person('en')
connection = sqlite3.connect('DB_add_data.db')
cursor = connection.cursor()


def add_table():
    cursor.execute("""
        create table people
        ( name text, family text, age text, email text, password text)
        """)


"""Заполняю txt файл"""


def gen_to_txt(args):
    file_txt = open('base_person_data.txt', 'w', encoding='utf-8')
    for _ in range(args):
        a = str(person.name()),
        b = str(person.last_name()),
        c = str(person.age()),
        d = str(person.email()),
        e = str(person.password().replace('"', '1')).replace(',', '2')
        for j in a, b, c, d, e:
            file_txt.write(str(j).strip(')('))
        file_txt.write('\n')
    file_txt.close()
    add_csv(args)


""""""

"""Заполняю csv файл"""


def add_csv(args):
    with open('test.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # writer = csv.writer(file_csv)
        reader = open('base_person_data.txt', encoding='utf-8', newline='')
        for _ in range(args):
            for row in reader.read():
                file_csv.write(row)
    add_csv_to_DB()


"""Заполняю базу данных"""


def add_csv_to_DB():
    with open('test.csv', encoding='utf-8') as file_to_bd:
        writer_csv = csv.reader(file_to_bd)
        cursor.executemany("INSERT INTO people VALUES (?, ?, ?, ?, ?)", writer_csv)
        connection.commit()



""""""


def drop_table():
    a = """ DROP TABLE people """
    cursor.execute(a)
    add_table()
    print('Таблица очищена!')


def view_db():
    sql = "select * from people"
    cursor.execute(sql)
    count = 0
    for i in cursor.fetchall():
        count += 1
        print(count, i)


# add_table()
gen_to_txt(100)
# sleep(1)
# add_csv(10**4)
# sleep(1)
# add_csv_to_DB()
# sleep(1)


# gen_to_txt(100)
view_db()

# drop_table()
