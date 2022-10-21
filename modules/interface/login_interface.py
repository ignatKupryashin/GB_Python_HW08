from modules.register import register
from modules.check_data import check_data
from modules.get_data import get_data
from modules.interface.login import login


def login_interface():
    file = "data/users.txt"
    while True:
        print("")
        print("1 - Войти")
        print("2 - Зарегистрироваться")
        print("9 - Выход")
        choise = input("Введите команду: ")
        if choise == "1":
            login_name = input("Введите логин: ")
            if check_data(get_data(file), login_name, 0) != "-1":
                login(login_name)
            else:
                print("Такой учётной записи не сущесствует")
        if choise == "2":
            register()
        if choise == "9":
            break
