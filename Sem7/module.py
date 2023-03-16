import csv

def create(data):
    with open('contacts.csv', 'a') as book:
        book.write(f'{data[0]};{data[1]};\n')
        return 'Контакт создан'

def find(name):
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        book = {}
        for i in lines[0:-1]:
            member = i.split(';')
            book[member[0]] = member[1]
        if name in book.keys():
            return book[name]
        else:
            return 'Такого нет'

def export_txt():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        txt = ''
        for i in lines[0:-1]:
            member = i.split(';')
            txt += f'{member[0]} {member[1]}\n'
        with open('contacts_base.txt', 'w') as book:
            book.truncate()
            book.write(txt)
        return 'Файл с базой создан'

def imp():
    with open('contact_imp.csv', encoding='utf-8') as data:
            file_reader = csv.reader(data, delimiter = ";")
            for i in file_reader:
                with open('contacts.csv', 'a') as book:
                    book.write(f'{i[0]};{i[1]};\n')
    return 'Файл импортирован'