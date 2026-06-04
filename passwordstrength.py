class PasswordError(Exception):
    pass
try:
    password=input("Enter Password: ")
    if len(password)<8:
        raise PasswordError("Password must contain at least 8 characters!!")
    if not any (char.isdigit() for char in password):
        raise PasswordError("Password must contain atleast one digit!!")
    if not any(char.isupper() for char in password):
        raise PasswordError("Password must contain atleast one uppercase character!!")
    print("Strong Password Accepted")
except PasswordError as e:
    print("Password Error:",e)
finally:
    print("Password validation completed")
