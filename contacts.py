# contacts.py
from database import create_table
from storage.sql_storage import add_contact, get_all_contacts, get_contact, delete_contact, update_contact
from storage.json_storage import export_contacts
from validators import validate_name, validate_phone, validate_email


def input_contact_details():
    """Get validated name, number, and email from the user."""
    while True:
        name = input("Enter contact name: ").capitalize().strip()
        if not validate_name(name):
            print("Name must be at least 3 characters long.")
        else:
            break

    while True:
        number = input("Enter number: ").strip()
        if not validate_phone(number):
            print("Make sure the number has 10 digits and starts with 0.")
        else:
            break

    while True:
        email = input("Enter email address: ").strip()
        if not validate_email(email):
            print("Invalid email format. Please try again.")
        else:
            break

    return name, number, email


def add_new_contact():
    """Add a new contact to the database."""
    name, number, email = input_contact_details()
    if get_contact(name):
        print(f"{name} already exists!")
        return

    add_contact(name, number, email)
    print(f"{name} added successfully!")


def display_contacts():
    """Display all contacts."""
    contacts = get_all_contacts()
    if not contacts:
        print("No contacts to display")
        return

    print("-------📖 Contact List -----------")
    for name, number, email in contacts:
        print(f"""🧑 {name}
📞 Phone: {number}
📧 Email: {email}
""")
    # Backup to JSON
    export_contacts(contacts)


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip().capitalize()
    contact = get_contact(name)
    if contact is None:
        print(f"{name} not found")
        return

    name, number, email = contact
    print(f"""
🧑 {name}
📞 Phone: {number}
📧 Email: {email}
""")


def edit_contact():
    """Edit a contact's number or email."""
    name = input("Enter the name to edit: ").strip().capitalize()
    contact = get_contact(name)
    if not contact:
        print(f"{name} not found!")
        return

    new_phone = input("New number (leave blank to keep current): ").strip()
    if new_phone and not validate_phone(new_phone):
        print("Invalid number. Skipping update for number.")
        new_phone = None

    new_email = input("New email (leave blank to keep current): ").strip()
    if new_email and not validate_email(new_email):
        print("Invalid email. Skipping update for email.")
        new_email = None

    if not new_phone and not new_email:
        print("No changes made.")
        return

    update_contact(name, new_phone, new_email)
    print(f"{name}'s contact updated successfully!")


def delete_existing_contact():
    """Delete a contact by name."""
    name = input("Enter the name to delete: ").strip().capitalize()
    if not get_contact(name):
        print(f"{name} not found!")
        return

    delete_contact(name)
    print(f"{name} deleted successfully!")


def main():
    """Main CLI loop."""
    create_table()
    while True:
        print("""
-------📖CONTACT BOOK📖---------

1. Add contact
2. Display contacts
3. Search contact
4. Edit contact
5. Delete contact
6. Exit
""")
        choice = input("Choose an option (1-6): ").strip()
        try:
            if choice == "1":
                add_new_contact()
            elif choice == "2":
                display_contacts()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                edit_contact()
            elif choice == "5":
                delete_existing_contact()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Enter 1-6.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
