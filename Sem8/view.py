def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")#+
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")#+
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def add_new():
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    vacancy = input('Должность: ')
    salary = input('Зарплата: ')
    phone = input('Введите номер: ')
    return (f'{last_name},{first_name},{vacancy},{salary},{phone}')


def find_somehow():
    x = int(input('Введите по чему будем искать:\
                    1 - Фамилия\
                    2 - Имя\
                    3 - Должность\
                    4 - Телефон '))
    if x == 1:
        last_name = input('Фамилия: ')
        return (x, last_name)
    elif x == 2:
        first_name = input('Имя: ')
        return (x, first_name)
    elif x == 3:
        vacancy = input('Должность: ')
        return (x, vacancy)
    elif x == 4:
        phone = input('Введите номер: ')
        return (x, phone)
