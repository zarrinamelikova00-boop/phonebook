from services.contacts import (
    add_contact,
    show_contacts,
    search_contact,
    delete_contact
)


def main():
    while True:
        print("\n--- ТЕЛЕФОННАЯ КНИГА ---")
        print("1. Добавить контакт")
        print("2. Показать контакты")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()
