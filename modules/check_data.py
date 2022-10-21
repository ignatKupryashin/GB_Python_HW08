def check_data(data, question, field):
    for i in range(len(data)):
        if data[i][field] == question:
            return i
    return "-1"
