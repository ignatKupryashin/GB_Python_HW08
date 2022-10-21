from modules.read_data import read_data
from modules.change_data import change_data
from modules.get_data import get_data


def admin_interface():
    while True:
        print("Интерфейс Администратора")
        print("")
        print("1 - Прсмотреть список учётных записей")
        print("2 - Изменить роль")
        print("9 - Выход")
        choice = input("Введите команду: ")
        print("")
        if choice == "1":
            print(read_data("users", "all", ))
        if choice == "2":
            user_list = get_data("data/users.txt")
            print("")
            for i in range(len(user_list)):
                print(str(i) + ": " + " - ".join(user_list[i]))
            choice_user = input("Введите номер логина, которому требуется изменить роль: ")
            print("")
            if choice_user.isdigit():
                choice_user = int(choice_user)
                if choice_user in range(len(user_list)):
                    print("")
                    print("1 - Студент\n2 - Преподаватель\n3 - Администратор")
                    new_role = input("Введите номер присваевоемой роли: ")
                    if new_role in ["1", "2", "3"]:
                        change_data("users", user_list[choice_user][0], new_role, 0, 2)
                    else:
                        print("Указанной роли не существует")
                else:
                    print("Введена некорректный логин")
            else:
                print("Номер логина нужно ввести цифрой");
        if choice == "9":
            break
