# 📒 Contact Book (Python + SQLite)

A command-line Contact Book application built with **Python** and **SQLite**, featuring full CRUD functionality, input validation, and automatic JSON backups. This project demonstrates clean architecture, modular design, and real-world database handling.

---

## ✨ Features

* ➕ Add new contacts
* 📖 Display all contacts
* 🔍 Search contacts by name (case-insensitive)
* ✏️ Edit existing contacts
* 🗑️ Delete contacts
* 💾 Persistent storage using SQLite
* 📤 Automatic JSON export for backup
* ✅ Input validation for names, phone numbers, and emails

---

## 🛠️ Tech Stack

* **Python 3**
* **SQLite3** (built-in Python module)
* **JSON** (for backup/export)

No external libraries required.

---

## 📁 Project Structure

```
contact_book/
│
├── contacts.py              # Main CLI application
├── database.py              # Database connection & table creation
├── contacts.db              # SQLite database (auto-created)
│
├── storage/
│   ├── sql_storage.py       # SQL CRUD operations
│   ├── json_storage.py      # JSON export logic
│   └── __init__.py
│
├── validators.py            # Input validation functions
└── README.md
```

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/contact-book.git
   cd contact-book
   ```

2. **Run the application**

   ```bash
   python3 contacts.py
   ```

3. Follow the on-screen menu to manage contacts.

> ℹ️ The SQLite database (`contacts.db`) is created automatically on first run.

---

## 🧪 Example Usage

```
1. Add contact
2. Display contacts
3. Search contact
4. Edit contact
5. Delete contact
6. Exit
```

---

## 🧾 Database Schema

```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    number TEXT NOT NULL,
    email TEXT NOT NULL
);
```

---

## 📤 JSON Backup

Every time contacts are displayed, they are exported to a JSON file for backup purposes.

Example:

```json
{
  "Alice": {
    "number": "0123456789",
    "email": "alice@email.com"
  }
}
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* SQLite database integration
* Clean separation of concerns
* Error handling and validation
* Case-insensitive SQL queries
* Debugging real-world issues (constraints, paths, returns)

---

## 🚀 Future Improvements

* Add unit tests (pytest)
* Build a Flask REST API
* Create a web frontend (HTML/CSS/JavaScript)
* Add authentication

---

## 👤 Author

**Resego Motlhasi**
Aspiring Software Engineer

---

## 📄 License

This project is open-source and free to use for learning and portfolio purposes.
