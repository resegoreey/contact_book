from storage import load_contacts, save_contacts
from validators import validate_name, validate_phone, validate_email

def add_contact(contacts):
    while True:

        name = input("Enter contact name: ").capitalize().strip()
        if not validate_name(name):
            print("Name must be at least 3 characters long.")
    
        else:
            break

    while True:
        number = input("Enter phone number: ")

        if not validate_phone(number):
            print("Make sure number has 10 digits and starts with zero(0)")
        else:
            break

    while True:
        email = input("Enter email address: ")
        
        if not validate_email(email):
            print("Invalid email format. Please try again.")
        else:
            break

    if name in contacts:
        print(f"{name} already exist")
    
    contacts[name] = {"Number": number, "Email": email}
    save_contacts(contacts)
    print(f"Added 🙋🏽 {name} with number: 📞 {number} and email: 📧 {email}")
    

    print("----------------------------------------------")

def display_contacts(contacts):
    
    if not contacts:
            print("No contacts to display")
            return
                
    print("-------📖Contact List-----------")
    
    for name, details in contacts.items():
        print(f"""🧑 {name}:
        📞 Phone: {details["Number"]}
        📧 Email: {details["Email"]}""")


def search_contact(contacts):
    print("----🔎 Searching for a contact----")
    name = input("Search name: ").capitalize().strip()
    contact = contacts.get(name)

    if not contact:
        print(f"Contact not found")
    
    print(f"""
        🧑 {name}
        📞 Phone: {contact["Number"]}
        📧 Email: {contact["Email"]}
""")
    print("--------------------------------------")

def delete_contact(contacts):
     #removing contacts
    print("--------Delete a contact-----------")
    name = input("Enter contact name to delete: ").capitalize().strip()

    if not name in contacts:
        print("Contact not found")
    
    del contacts[name]
    save_contacts(contacts)
    print(f"{name} deleted")
    
    print("--------------------------------------")


def edit_contact(contacts):
    print("-------Edit Contact------")
    name = input("Enter the name you want to edit: ").strip().capitalize()
    if name not in contacts:
        print(f"{name} can't be found!")
        return

    new_number = input("New number (enter to skip): ")
    new_email = input("New email (enter to skip): ")

    if new_number and validate_phone(new_number):
        contacts[name]["Number"] = new_number

    if new_email and validate_email(new_email):
        contacts[name]["Email"] = new_email

    save_contacts(contacts)
    print(f"{name}'s contact updated.")
    
def main():
    contacts = load_contacts()
    while True:
        
        print("-------📖CONTACT BOOK📖---------")

        print("""What would you like to do?
        1. Add  contact
        2. Display contacts
        3. Search  contact
        4. Delete  contact
        5. Edit a contact
        6. Exit""")

        print("----------------------------------")

        choice = input("Choose an option(1-6): ")
        print("-------------------------------------")
        try:

             if choice == "1":
                add_contact(contacts)
            

             elif choice == "2":
                display_contacts(contacts)
            
             elif choice == "3":
                #Accessing/ searching the contacts name
                search_contact(contacts)

             elif choice == "4":
                delete_contact(contacts)
            
             elif choice == "5":
                edit_contact(contacts)

             elif choice == "6":
                print("Goodbye")
                break

             else:
                print("Make a valid choice, choose between 1 to 6")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")
                      


if __name__ == '__main__':
    main()