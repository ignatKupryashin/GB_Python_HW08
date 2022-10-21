from modules.add_data import add_data


def register():
    while True:
        login = input("Введите логин: ")
        if login != "all":
            break
        print("Данное имя запрещено")
    name = input("Введите своё ФИО: ")
    add_data("users", [login, name, 1])
