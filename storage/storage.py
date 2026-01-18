import json
import os


file_name = "contacts.json"

def load_contacts():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(user_contacts: dict):
    with open(file_name, 'w') as file:
        return json.dump(user_contacts, file, indent=4)
