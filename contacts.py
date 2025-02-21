#welcome message
print("Hello, your contacts will be kept safe!")
user_contacts = {}
print(f"contacts = {user_contacts}")
print()

def add_contact(contact_name):
    
    if contact_name in user_contacts:
        print("Contact name already exists")
        return 
        
    #Nesting the contact name dictionary to the main dictionary
    #contact_name = input("Name: ")
    user_contacts[contact_name] = {}
    #print(user_contacts)

    
   
    while True:

        #Adding contact name items to the nested dictionary
        contact_number = input("Phone numbers: ")
        if contact_number[0] != "0":
            print("Contact number should start with a zero(0)")
            break
        elif len(contact_number) != 10:
            print("Contact number should be ten(10) digits!")
            break
        else:
            user_contacts[contact_name]["phone number"] = contact_number
            


        contact_email = input("Email address: ").strip()
        if  "@"  in contact_email and "."  in contact_email:
            user_contacts[contact_name]["email"] = contact_email
            break
        else:
            print("Your email should contain '@' and '.")
    
    
        print(user_contacts)
        print(f"""You added:
        name: {contact_name}
        number: {contact_number}
        email: {contact_email}""")

    #validating email
    #contact_email = contact_email.index("@")
    

def search_contact():
    access_name = input("Search for a name: ")
    if access_name in user_contacts:
        print(f"""You searched for {access_name}
        Their number is {user_contacts[access_name]["phone number"]}
        Their email address is {user_contacts[access_name]["email"]}""")
    else:
        print(f"{access_name} doesn't exist")

def remove_contact():
     #removing contacts
    remove_detail = input("What would you like to remove? ")
    if remove_detail in user_contacts:
        user_contacts.pop(remove_detail)
        print(f"You removed {remove_detail}")
    else:
        print(f"{remove_detail} does not exist")

def display_contacts():
    for name, details in user_contacts.items():
        number = details.get("phone number", "N/A")
        email = details.get("email", "N/A")
        print(f"Here are your contacts {name} : {number} : {email}")

while True:
    
        print("""What would you like to do?
        1. Add a new contact
        2. Search for a contact
        3. Remove a contact
        4. Exit
        5. Display contacts""")
        user_action = input("Choose from above options(1-4): ")

        if user_action == "1":
            contact_name = input("Name: ").capitalize()
            if contact_name == "":
                print("Name can't be empty")
            else:
                add_contact(contact_name)

        elif user_action == "2":
            #Accessing/ searching the contacts name
            search_contact()
        
        elif user_action == "3":
           remove_contact()
        elif user_action == "5":
            display_contacts()
        elif user_action == "4":
            print("Bye Bye")
            break

        else:
            print("Make a valid choice, choose between 1 and 4")
            




#changing detials to be added soon



