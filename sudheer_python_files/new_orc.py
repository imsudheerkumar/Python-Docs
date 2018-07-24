import cx_Oracle
try:
    connection=cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("Conn estbalished")

except Exception as e:
    print('Exception :',e)
c1=input("branch")
c2=input("no")
cursor=connection.cursor()
cursor.execute("SELECT * FROM students WHERE c1=:2 AND c2=:1", (1, 2))
print(cursor.rowcount)
row=cursor.fetchall()
for i in row:
    print(i)
print(cursor.rowcount)
    
