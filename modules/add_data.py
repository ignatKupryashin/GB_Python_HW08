from modules.get_data import get_data
from modules.check_data import check_data


def add_data(filename,  new_data):
    filename = "data/" + filename + ".txt"
    data = get_data(filename)
    if len(new_data) == len(data[0]):
        if check_data(data, new_data[0], 0) == "-1":
            data.append(new_data)
            with open(filename, "w") as file:
                data = "\n".join([";".join(list(map(str, data[i]))) for i in range(len(data))])
                file.write(data)
                print("Новая запись добавлена")
        else:
            print("Данные с таким ключевым полем уже есть в таблице")
    else:
        print("Колличество введённых данных не соответствует записи базы данных")