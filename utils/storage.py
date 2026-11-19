import json
from utils.config import CONTACTS_FILE


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)