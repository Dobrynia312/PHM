phone_book = []
fields = ['Фамилия', 'Имя', 'Должность', 'Зарплата', 'Телефон']


def create(data):
    phone_book.append(dict(zip(fields, data.split(','))))
    return 'Контакт создан'


def find_someone(data):
    x = data[0]
    y = data[1]
    global phone_book
    if x == 1:
        for el in phone_book:
            if el.get("Фамилия") == y:
                return el
            else:
                return "Такой работник отсутвует"
    elif x == 2:
        for el in phone_book:
            if el.get("Имя") == y:
                return el
            else:
                return "Такой работник отсутвует"
    elif x == 3:
        for el in phone_book:
            if el.get("Должность") == y:
                return el
            else:
                return "Такой работник отсутвует"
    elif x == 4:
        for el in phone_book:
            if el.get("Телефон") == y:
                return el
            else:
                return "Такой работник отсутвует"
