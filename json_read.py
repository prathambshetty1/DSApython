import json
employee={
    "id": 101,
    "name": "Amit",
    "salary": 50000
}
file=open("employee.json","w")
json.dump(employee,file,indent=4)
file.close()
print("JSON file created successfully.")
file=open("employee.json","r")
data=json.load(file)
print("ID:",data["id"])
print("Name:",data["name"])
print("Salary:",data["salary"])
file.close()