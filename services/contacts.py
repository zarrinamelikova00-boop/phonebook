from utils.storage import load_contacts, save_contacts


def add_contact():
    contacts = load_contacts()

    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")

    contacts[name] = phone
    save_contacts(contacts)

    print("Контакт добавлен!")


def show_contacts():
    contacts = load_contacts()

    if not contacts:
        print("Контактов пока нет")
        return

    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def search_contact():
    contacts = load_contacts()

    name = input("Введите имя для поиска: ")

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Контакт не найден")


def delete_contact():
    contacts = load_contacts()

    name = input("Введите имя для удаления: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Контакт удалён!")
    else:
        print("Контакт не найден")