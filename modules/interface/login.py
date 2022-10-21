from modules.read_data import read_data
from modules.interface.student_interface import student_interface
from modules.interface.teacher_interface import teacher_interface
from modules.interface.admin_interface import admin_interface


def login(login_name):
    filename = "users"
    data = read_data(filename, login_name, 0)
    if data != "Данные отсутствуют":
        if data[-1] == "1":
            student_interface()
        if data[-1] == "2":
            teacher_interface()
        if data[-1] == "3":
            admin_interface()