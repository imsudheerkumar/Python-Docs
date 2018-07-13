import cx_Oracle
try:
    con = cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("conn established")
except Exception as e:
    print("EXCEPTION :",e)
cursor = con.cursor()
student_id=input("enter student id : ")
student_name=input("enter student name : ")
student_branch=input("enter student branch : ")
student_grade=input("enter student grade : ")

cursor.execute('INSERT INTO students VALUES (:1,:2,:3,:4)',(student_id,student_name,student_branch,student_grade))
cursor.execute('select *from students')
row=cursor.fetchall()
for i in row:
    print(i)
con.commit()
con.close()
