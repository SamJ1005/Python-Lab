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
    print("Password is invalid. Please make sure to include at least:")
    missing_requirements = []
    if len(user_input) < 8:
        missing_requirements.append("a minimum length of 8 characters")
    if not any(char.isupper() for char in user_input):
        missing_requirements.append("at least one uppercase letter")
    if not any(char.isdigit() for char in user_input):
        missing_requirements.append("at least one digit")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', user_input):
        missing_requirements.append("at least one special character")
        
    print(f"The password is invalid. Missing: {', '.join(missing_requirements)}")
