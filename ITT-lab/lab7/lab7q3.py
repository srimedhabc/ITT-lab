import sqlite3
conn = sqlite3.connect('student123.db')
print ("Opened database successfully")
#create a table
conn.execute('''CREATE TABLE STUDENT
(REGNO INT PRIMARY KEY NOT NULL,
NAME
TEXT NOT NULL,
AGE
INT NOT NULL,
BRANCH
CHAR(50),
CGPA
REAL);''')
print ("Table created successfully")
#insert operation
conn.execute("INSERT INTO STUDENT (REGNO,NAME,AGE,BRANCH,CGPA) \
VALUES (6001, 'Venusaur', 21, 'Mechanical', 9.00 )")
conn.execute("INSERT INTO STUDENT (REGNO,NAME,AGE,BRANCH,CGPA) \
VALUES (2002, 'Tentacool', 18, 'Chemical', 8.00 )")
conn.execute("INSERT INTO STUDENT (REGNO,NAME,AGE,BRANCH,CGPA) \
VALUES (6003, 'Polywhirl', 20, 'IT', 7.50 )")
conn.execute("INSERT INTO STUDENT (REGNO,NAME,AGE,BRANCH,CGPA) \
VALUES (4004, 'Nidoran', 19, 'EEE', 8.50 )")
conn.commit()
print ("Records created successfully")
#select option
print("The records inserted are:\n")
cursor = conn.execute("SELECT REGNO,NAME,AGE,BRANCH,CGPA from STUDENT")
for row in cursor:
    print ("REGNO = ", row[0])
    print ("NAME = ", row[1])
    print ("AGE = ", row[2])
    print ("BRANCH = ", row[3])
    print ("CGPA = ", row[4], "\n")
given_regno = int(input("Enter the REGNO of the student: "))
sql_select_query = """SELECT REGNO,NAME,AGE,BRANCH,CGPA from STUDENT where REGNO = ?"""
cursor.execute(sql_select_query, (given_regno,))
print("The details of the student with REGNO = ",given_regno,"\n")
for row in cursor:
    print ("REGNO = ", row[0])
    print ("NAME = ", row[1])
    print ("AGE = ", row[2])
    print ("BRANCH = ", row[3])
    print ("CGPA = ", row[4], "\n")
print ("Operation done successfully")
conn.close()