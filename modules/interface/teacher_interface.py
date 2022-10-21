from modules.read_data import read_data
from modules.change_data import change_data
from modules.get_data import get_data


def teacher_interface():
    while True:
        print("Интерфейс Учителя")
        print("")
        print("1 - Прсмотреть домашние задания")
        print("2 - Изменить домашние задания")
        print("9 - Выход")
        choice = input("Введите команду: ")
        print("")
        if choice == "1":
            print(read_data("hometasks", "all", ))
        if choice == "2":
            subject_list = read_data("classes", "all")
            print("")
            print(subject_list)
            choice_subject = input("Введите номер дисциплины: ")
            print("")
            if choice_subject.isdigit():
                choice_subject = int(choice_subject)
                if choice_subject in range(len(get_data("data/classes.txt"))):
                    home_task = input("Введите домашнее задание: ")
                    change_data("hometasks", get_data("data/classes.txt")[choice_subject][1], home_task)
                else:
                    print("Введена некорректная дисциплина")
            else:
                print("Дисциплину нужно ввести цифрой");
        if choice == "9":
            break

