import view
import module


def button():
    x = view.show_menu()
    while x != 9:
        if x == 4:
            module.create(view.add_new())
            print(module.phone_book)
        elif x == 1:
            print(module.find_someone(view.find_somehow()))
        x = view.show_menu()
    else:
        with open('contacts.csv', 'a') as book:
            book.write(str(module.phone_book))
