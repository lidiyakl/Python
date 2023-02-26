# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding = "utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])

        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ["фамилию", "имя", "отчество", "телефон"]
    string = ""
    for i in array:
        string += input(f"Введите {i} ") + " "
    id += 1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')


def search():
    num = input("Кого ищем? ")
    result = []
    for i in all_data:
        if num in i:
            result.append(i)
    print(*result, sep="\n")


def export():
    new_base = input("Введите имя файла ")
    global file_base
    if path.exists(new_base):
        file_base = new_base


def delete_record():
    global all_data
    symbol = "\n"
    show_all()
    rec = input("Введите id контакта ")
    all_data = [i for i in all_data if i[0] != rec]
    with open(file_base, 'w', encoding = "utf-8") as f:
        f.write(f"{symbol.join(all_data)}\n")


def change_record():
    global all_data
    symbol = "\n"
    show_all()
    rec = input("Введите id контакта ")
    
    for i in all_data:
        if i[0] == rec:
            i = input("Введите данные ")
    return all_data
    
    with open(file_base, 'w', encoding = "utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')


def main_menu():
    play = True
    while play:
        read_records()
        answer = int(input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Export base\n"
                       "7. Exit\n"))
        # match answer:
        #     case "1":
        #         show_all()
        #     case "2":
        #         add_new_contact()
        #     case "3":
        #         pass
        #     case "4":
        #         play = False
        #     case _:
        #         print("Try again!\n")

        if answer == 1:
            show_all()
        elif answer == 2:
            add_new_contact()
        elif answer == 3:
            search()
        elif answer == 4:
            change_record()
        elif answer == 5:
            delete_record()
        elif answer == 6:
            export()
        elif answer == 7:
            play = False
        else:
            print("Try again!\n")


main_menu()
