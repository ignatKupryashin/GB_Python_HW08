from modules.get_data import get_data
from modules.check_data import check_data


def change_data(filename, value, changing_value, field=0, changing_field=1):
    filename = "data/" + filename + ".txt"
    data = get_data(filename)
    coordinate = check_data(data, value, field)
    if coordinate != "-1":
        data[coordinate][changing_field] = changing_value
        print(f"Данные перезаписаны")
        with open(filename, "w") as file:
            file.write("\n".join(";".join(item) for item in data))
        return True
    else:
        return False
