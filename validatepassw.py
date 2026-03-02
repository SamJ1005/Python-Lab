import re

def validate_password(password):
    if len(password) < 8:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

user_input = input("Enter a password: ")
if validate_password(user_input):
    print("Password is valid.")
else:
    print("The password is invalid.")
