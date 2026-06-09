import re
def validate_employee(emp_id,name,age,email,salary):
    if not emp_id.startswith("EMP") or not emp_id[3:].isdigit():
        print("Invalid Employee ID! Format: EMP101")
        return
    if not name.replace(" ","").isalpha():
        print("Invalid Name! Only alphabets allowed")
        return
    if age<18 or age>60:
        print("Invalid Age!! Must be between 18 and 60!!")
        return
    email_pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern,email):
        print("Invalid email")
        return
    if salary<=0:
        print("Invalid Salary")
        return
    print("Employee Registered Successfully!")
    print("Emp ID:",emp_id)
    print("Name:",name)
    print("Age:",age)
    print("Email:",email)
    print("Salary:",salary)
validate_employee("EMP272","Pratham",21,"prathamshetty@gmail.com",5000000)