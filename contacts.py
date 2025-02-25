user_contacts = {}

def add_contact():
    while True:

        name = input("Enter contact name: ").capitalize()
        if len(name) < 3 or name == '':
            print("Name can't be empty or shorter than 2 characters")
    
        else:
            break

    while True:
        number = input("Enter phone number: ")
        if len(number) < 10 or number[0] != "0":
            print("Make sure number has 10 digits and starts with zero(0)")
        else:
            break

    while True:
        email = input("Enter email address: ")
        if "@" not in email or ".com" not in email:
            print("Make sure email has the '@' and ends with '.com'")
        else:
            break

    if name in user_contacts:
        print(f"❌ {name} already exist")
    
    else:
        user_contacts[name] = {"Number": number, "Email": email}
        print(f"Added 🙋🏽{name} with number: 📞 {number} and email: 📧{email}")

    print("----------------------------------------------")

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

def display_contacts():
    print("-------📖Contact List-----------")
    for name, details in user_contacts.items():
        print(f"""📞 {name}:
        📱 Phone: {details["Number"]}
        📧 Email: {details["Email"]}""")
    
    
while True:
        
        print("📱Hello, your contacts will be kept safe!")
        print("-------📖CONTACT BOOK📖---------")

        print("""What would you like to do?
        1. Add  contact
        2. Search  contact
        3. Delete  contact
        4. Display contacts
        5. Exit""")

        print("----------------------------------")

        user_action = input("Choose from above options(1-4): ")
        print("-------------------------------------")


        if user_action == "1":
            add_contact()
        

        elif user_action == "2":
            #Accessing/ searching the contacts name
            search_contact()
        
        elif user_action == "3":
           delete_contact()

        elif user_action == "4":
           if user_contacts:
            display_contacts()
            print("----------------------------------")
           else:
                print("❌No contacts to display")
               
                print("----------------------------------")
        elif user_action == "5":
            print("👋Bye Bye")
            break

        else:
            print("❌Make a valid choice, choose between 1 and 4")
            



#changing detials to be added soon



