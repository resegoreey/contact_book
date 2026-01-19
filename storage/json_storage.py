import json
import os


file_name = "contacts.json"

def load_contacts():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return {}

#saving the backup od contacts to JSON
def save_contacts(contacts: dict):
    with open(file_name, 'w') as file:
        return json.dump(contacts, file, indent=4)

def export_contacts(sql_contacts):
    contacts_dict = {
        name: {"number": number, "email": email}
        for name, number, email in sql_contacts
    }
    save_contacts(contacts_dict)