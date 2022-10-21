#Метод возвращает прочитанный файл в виде списка
def get_data(filename):
    with open(filename, "r") as file:
        data = [(string.replace("\n", "")).split(";") for string in file.readlines()]
    return data