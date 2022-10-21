from modules.get_data import get_data
from modules.check_data import check_data


def read_data(filename, value, field=0):
    filename = "data/" + filename + ".txt"
    data = get_data(filename)
    answer = "Данные отсутствуют"
    if value == "all":
        answer = ""
        for i in range(len(data)):
            answer += " - ".join(data[i]) + "\n"
    else:
        coordinate = check_data(data, value, field)
        if coordinate != -1:
            answer = " - ".join(data[int(coordinate)])
    return answer