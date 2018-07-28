import cx_Oracle
try:
    connection=cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("Connection-Established")
    print("Database version:", connection.version)
    print(cx_Oracle.version)
except Exception as e:
    print("The Exception is :",e)
5

cursor=connection.cursor()
print("row-count :" ,cursor.rowcount)
cursor.execute("insert into users values(106,'shyam','varma','employee')")
#row=cursor.fetchall()
#for i in row:
    #print(i)
print("row-count :" ,cursor.rowcount)

connection.commit()
connection.close()
            
