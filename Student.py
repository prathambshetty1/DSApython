import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
               id INTEGER,
               name TEXT,
               marks INTEGER)
""")

cursor.execute("INSERT INTO student VALUES(101,'Pratham',98)")
cursor.execute("INSERT INTO student VALUES(102,'Naman',95)")
conn.commit()
sid=int(input("Enter the student id:"))
cursor.execute("SELECT * FROM student where id=?",(sid,))
record=cursor.fetchone()
if record:
    print("Student Found:",record)
else:
    print("Student Not Found")
conn.close()