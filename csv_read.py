import csv
file=open("students.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["ID","Name","Marks"])
writer.writerow([101,"Pratham",85])
writer.writerow([102,"Priya",90])
file.close()
print("CSV file created successfully")
file=open("students.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()

