#welcome message
print("📱Hello, your contacts will be kept safe!")
user_contacts = {}

def add_contact():
    
    name = input("Enter contact name: ").capitalize()
    number = input("Enter phone number: ")
    email = input("Enter email address: ")

    if name in user_contacts:
        print(f"❌ {name} already exist")
    else:
        user_contacts[name] = {"Number": number, "Email": email}
    
print()
def search_contact():
    print("----🔎 Searching for a contact----")
    access_name = input("Search for a name: ").capitalize().strip()

    if access_name in user_contacts:
        print(f"""Name: 🧑🏽{access_name}
        Number: 📞 {user_contacts[access_name]["Number"]}
        Email: 📧 {user_contacts[access_name]["Email"]}""")
    else:
        print(f"❌ {access_name} doesn't exist")
    print("--------------------------------------")
print()
def delete_contact():
     #removing contacts
    print("--------Delete a contact-----------")
    remove_contact_name = input("Enter contact name to delete: ").capitalize()
    if remove_contact_name in user_contacts:
        del user_contacts[remove_contact_name]
        print(f"✅ You deleted {remove_contact_name}")
    else:
        print(f"❌ {remove_contact_name} does not exist")
    print("--------------------------------------")
print()

def display_contacts():
    print("----📖Contact List----")
    for name, details in user_contacts.items():
        print(f"""📞 {name}:
        📱 Phone: {details["Number"]}
        📧 Email: {details["Email"]}""")
    print("-------------------------")

while True:
    
        print("""What would you like to do?
        1. Add  contact
        2. Search  contact
        3. Delete  contact
        4. Display contacts
        5. Exit""")

        user_action = input("Choose from above options(1-4): ")

        if user_action == "1":
            add_contact()

        elif user_action == "2":
            #Accessing/ searching the contacts name
            search_contact()
        
        elif user_action == "3":
           delete_contact()

        elif user_action == "4":
            display_contacts()

        elif user_action == "5":
            print("👋Bye Bye")
            break

        else:
            print("❌Make a valid choice, choose between 1 and 4")
            

print()


#changing detials to be added soon



