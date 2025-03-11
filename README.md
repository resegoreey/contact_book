📖 Contact Book

# Overview

This is a simple Contact Book application built in Python. It allows users to store, manage, and search for contacts with details like name, phone number, and email. The data is stored in a JSON file, making it easy to read, update, and manage. It is a CLI-based (Command Line Interface) tool that can be run directly in the terminal.

# Features

- Add a new contact with name, phone number, and email.
- Search for contacts by name.
- Delete contacts from the contact list.
- Display all contacts saved in the contact book.
- Data is saved in a JSON file (contacts.json).
- Validation checks for name, phone number, and email format.

# Requirements

- Python 3.6+
- Required libraries: json, os

# Setup

1. Clone the repository
   If you want to run this project locally, start by cloning the repository:

git clone https://github.com/your-username/contact-book.git
cd contact-book

2. Install Python (if not installed)
   Ensure that Python 3.6+ is installed on your machine. You can check by running:

python --version
If not installed, you can download Python from the official Python website.

# How to Use

1. Running the Application
   Navigate to the directory containing the contact_book.py file. Then, run the script:

python contact_book.py

2. Menu Options
   Once the script is running, you'll see the following options:

📱Hello, your contacts will be kept safe!
-------📖CONTACT BOOK📖---------
What would you like to do?

1. Add contact
2. Display contacts
3. Search contact
4. Delete contact
5. Exit
   You can choose from the following options:

- Add a contact – Add a contact by entering their name, phone number, and email address.
- Display contacts – View a list of all stored contacts.
- Search a contact – Search for a contact by name and view their details.
- Delete a contact – Remove a contact from the list.
- Exit – Close the application. 3. Input Validation

# The application ensures that:

- Names are at least 3 characters long.
- Phone numbers must be 10 digits and start with 0.
- Emails must contain "@" and ".com".

# How Data is Stored

- The contact information is saved in a JSON file called contacts.json. This allows you to store and retrieve contacts in a structured format.

# Example of the stored JSON format:

{
"John Doe": {
"Number": "0123456789",
"Email": "john@example.com"
},
"Jane Smith": {
"Number": "0987654321",
"Email": "jane@example.com"
}
}

# License

This project is open-source and available under the MIT License.

# Improvements

The following enhancements can be made to the project:

- GUI Version – Convert the CLI-based application into a GUI app using Tkinter or PyQt.
- Cloud Storage – Store contacts in the cloud for multi-device access.
- Search Optimization – Implement fuzzy search to match similar names.
- Backup & Restore – Add options to back up and restore contacts.
- Password Protection – Secure the contact book with a password.

# Contributing

Feel free to fork the repository, open issues, or submit pull requests. Contributions are welcome!

# Author

-Resego Motlhasi

- https://github.com/resegoreey
- Contact: contactresego@gmail.com
