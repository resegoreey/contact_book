#welcome message
print("Hello, your contacts will be kept safe!")
user_contacts = {}
print(f"contacts = {user_contacts}")
print()

#Nesting the contact name dictionary to the main dictionary
contact_name = input("Name: ")

while not contact_name == "":
    user_contacts[contact_name] = {}
    print(user_contacts)

    #Adding contact name items to the nested dictionary
    contact_number = input("Phone numbers: ")
    contact_email = input("Email address: ")
    user_contacts[contact_name]["phone number"] = contact_number
    user_contacts[contact_name]["email"] = contact_email
    print(user_contacts)
    print()

    print("""What would you like to do?
    1. Add another contact
    2. Search for a contact
    3. Remove a contact""")
    user_action = input("Choose from above options(1-3): ")

    if user_action == "1":
            contact_name = input("Name: ")

    elif user_action == "2":

        #Accessing/ searching the contacts name
        access_name = input("Search for a name: ")
        if access_name in user_contacts:
            print(f"""You searched for {contact_name}
            Their number is {user_contacts[contact_name]["phone number"]}
            Their email address is {user_contacts[contact_name]["email"]}""")
            continue
    
    elif user_action == "3":
        #removing contacts
        remove_detail = input("What would you like to remove? ")
        user_contacts[contact_name].pop(remove_detail)
        print(user_contacts)

    else:
        print("Make a valid choice, choose between 1 and 3")

    
else:
    print("name can't be empty")




#changing detials to be added soon



