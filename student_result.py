file=open("result.txt","w")
name=input("Enter the name: ")
marks=int(input("Enter the marks: "))
file.write(f"Name: {name}\n")
file.write(f"Marks: {marks}\n")
if marks>=40:
    file.write("Result:Pass")
else:
    file.write("Result:Fail")
file.close()
print("Result Saved Successfully.")