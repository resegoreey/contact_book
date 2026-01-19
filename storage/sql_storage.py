from typing import Optional, Tuple
from database import get_connection

def add_contact(name, number, email):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO contacts (name, number, email) VALUES (?, ?, ?)", (name, number, email))
        conn.commit()

def get_all_contacts():
    with get_connection() as conn:
        return conn.execute(
            "SELECT name, number, email FROM contacts"
        ).fetchall()
        
    
def get_contact(name: str)-> Optional[Tuple[str, str, str]]:
    with get_connection() as conn:
        conn.execute(
            "SELECT name, number, email FROM contacts WHERE LOWER(name) = LOWER(?)", (name.strip(),)
        ).fetchone()
    
def delete_contact(name):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM contacts WHERE LOWER(name) = LOWER(?)", (name.strip(),)
        )
        conn.commit()
    
def update_contact(name, number=None, email=None):
    with get_connection() as conn:
        if number:
            conn.execute(
                "UPDATE contacts SET number = ? WHERE name = ?", (number, name)
            )
        if email:
            conn.execute(
                "UPDATE contacts SET email = ? WHERE name = ?", (email, name)
            )
        conn.commit()


