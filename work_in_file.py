# Программа должна выводить данные

def write(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Успешно")

def read_all():
    # if "data.txt".exists():
    with open("data.txt", "r", encoding="utf-8") as f:
        # f.readlines()
        for line in f:
            print(line[:-1])

def get_by_name(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(line)

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# def change_data():
#     with open("data.txt", "r", encoding="utf-8") as f:

# def delete_data():
# 
        

def choose(choice):
    if choice == '1': return write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона)"))
    if choice == "2": return read_all()
    if choice == "3": return get_by_name(input("Введите имя или фамилию: "))
    # if choice == "4": return change_data()
    # if choice == "5": return delete_data()
    if choice == "6": exit()
