import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")

if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")