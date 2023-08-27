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

def delete_data(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open('data.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if name not in line:
                f.write(line)
        print("Данные успешно удалены из файла")

def change_data(old_name):
    new_name = input("Введите новые данные о пользователе: ")
    with open('data.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if old_name in lines:
                line = line.replace(old_name, new_name)
            f.write(line)
        print("Данные успешно изменены") # не получается вывести новое имя
        

def choose(choice):
    if choice == '1': return write(input("Введите ваши данные. Пример: фамилия имя отчество номер телефона "))
    if choice == "2": return read_all()
    if choice == "3": return get_by_name(input("Введите имя или фамилию пользователя, данные которого необходимо вывести в терминал: "))
    if choice == "4": return delete_data(input("Введите имя или фамилию пользователя, данные которого необходимо удалить: "))
    if choice == "5": return change_data(input("Введите имя или фамилию пользователя, данные которого необходимо изменить: "))
    if choice == "6": exit()
