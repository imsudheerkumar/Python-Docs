import cx_Oracle
try:
    con_connect=cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("conn established")
except Exception as e:
    print("EXCEPTION :",e)
cursor=con_connect.cursor()
cursor.execute('select *from worker')
row=cursor.fetchall()
for i in row:
   print(i)
con.commit()
con.close()
