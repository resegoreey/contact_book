
def validate_name(name: str) -> bool:
    return bool(name and len(name.strip()) >= 3)

def validate_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 10 and phone.startswith("0")

def validate_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]
