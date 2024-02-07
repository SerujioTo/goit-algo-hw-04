import sys
from pathlib import Path


def total_salary(path):
    salary = []  # Створюємо пустий список для зберігання даних у майбутньому

    try:
        with open(path, "r") as file:  # Відкриваємо файл за шляхом path у режимі читання
            data = file.readlines()  # Читаємо усі рядки файлу
        for line in data:  # Перебираємо рядки файлу
            line = line.split(",")  # Розділяємо рядки за комою
            salary.append(int(line[1]))  # Записуємо зарплату у список
        sum_ = sum(salary)  # Обчислюємо суму усіх зарплат у списку
        avg = int(sum_/len(salary))  # Обчислюємо середнє значення зарплат
        return sum_, avg
    except FileNotFoundError:
        print('Ваш файл не знайдено за таким шляхом')
        return None, None


sum_, avg = total_salary(Path("salary.txt"))
print(f"Загальна сума заробітної плати: {sum_}, Середня заробітна плата: {avg}")


def get_cats_info(path):
    cats = [] # Створюємо пустий список для зберігання даних у майбутньому
    try:
        with open(path, "r") as file:
            data = file.readlines()
            for line in data:
                cat = line.split(",")
                cats.append({"id": cat[0], "name": cat[1], "age": cat[2].strip()})
            return cats
    except FileNotFoundError:
        print('Ваш файл не знайдено за таким шляхом')
        return cats


cats_info = get_cats_info(Path("cats_info.txt"))
print(cats_info)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts.append({'name': name, 'phone': phone})
    return "Contact added."


def show_phone(args, contacts):
    name = args[0]
    for contact in contacts:
        if contact["name"] == name:
            return contact["phone"]
    return 'Not found'

def change_phone(args, contacts):
    name, phone = args
    # contacts.replace()
    for index, contact in enumerate(contacts):
        if contact["name"] == name:
            contacts[index] = {"name": name, "phone": phone}
            return "Contact is changed"
    return "Not found"

def all_phones(args, contacts):
    contact_string = ""
    for contact in contacts:
        contact_string += f"{contact['name']}: {contact['phone']}\n"
    return contact_string

def main():
    contacts = [{'name': 'John Doe', 'phone': '+380988858880'},
                {'name': 'Alice Cooper', 'phone': '+48880884215'}]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(all_phones(args, contacts), end="")
        else:
            print("Invalid command.")


if __name__ == "__main__":  # Точка входу
    main()
