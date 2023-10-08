'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
'''

import json

def load_phonebook():
    try:
        with open('phonebook.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_phonebook(phonebook):
    with open('phonebook.json', 'w') as file:
        json.dump(phonebook, file)

def add_contact():
    name = input("Введите имя: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = number
    save_phonebook(phonebook)
    print("Контакт успешно добавлен!")

def update_contact():
    name = input("Введите имя контакта, который хотите изменить: ")
    if name in phonebook:
        number = input("Введите новый номер телефона: ")
        phonebook[name] = number
        save_phonebook(phonebook)
        print("Контакт успешно обновлен!")
    else:
        print("Контакт не найден!")

def delete_contact():
    name = input("Введите имя контакта, который хотите удалить: ")
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден!")

def search_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        print(f"Имя: {name}, Телефон: {phonebook[name]}")
    else:
        print("Контакт не найден!")

def print_phonebook():
    if phonebook:
        print("Телефонный справочник:")
        for name, number in phonebook.items():
            print(f"Имя: {name}, Телефон: {number}")
    else:
        print("Справочник пуст!")

phonebook = load_phonebook()

while True:
    print(
        "1. Добавить контакт\n"
        "2. Изменить контакт\n"
        "3. Удалить контакт\n"
        "4. Поиск контакта\n"
        "5. Вывести все контакты\n"
        "6. Выйти"
    )

    choice = input("Выберите действие (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print_phonebook()
    elif choice == '6':
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")