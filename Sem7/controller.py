import view
import module

def create_contact():
    return module.create(view.add_new())

def find_contact():
    return module.find(view.find_phone())

def export_contact(data):
    exp = [module.export_txt]
    return exp[int(data)-3]()

def import_contact(data):
    return module.imp()

def menu(data):
    if data == '0':
        show_res('До свидания')
    else:
        if data == '1':
            show_res(create_contact())
        elif data == '2':
            show_res(find_contact())
        elif data == '3':
            show_res(export_contact(data))
        elif data == '4':
            show_res(import_contact(data))
        else:
            show_res('Ошибка ввода')
        menu(view.nemu())

def show_res(data):
    view.view_res(data)