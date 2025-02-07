#welcome message
print("Hello, your contacts will be kept safe!")
user_contacts = {}
print(f"contacts = {user_contacts}")
print()

#Nesting the contact name dictionary to the main dictionary
contact_name = input("Name: ")
user_contacts[contact_name] = {}
print(user_contacts)
print()

#Adding contact name items to the nested dictionary
contact_number = input("Phone numbers: ")
contact_email = input("Email address: ")
user_contacts[contact_name]["phone number"] = contact_number
user_contacts[contact_name]["email"] = contact_email
print(user_contacts)
print()

#Accessing/ searching the contacts name
access_name = input("Search for a name: ")
print(f"""You searched for {contact_name}
Their number is {user_contacts[contact_name]["phone number"]}
Their email address is {user_contacts[contact_name]["email"]}""")
print()

#changing detials to be added soon

#removing contacts
remove_detail = input("What would you like to remove? ")
user_contacts[contact_name].pop(remove_detail)
print(user_contacts)


