import cx_Oracle
try:
    con = cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("conn established")
except Exception as e:
    print("EXCEPTION :",e)
cursor = con.cursor()
#sid=input("enter student id")
#sname=input("enter student name")
#sbranch=int(input("enter student branch"))
#sgrade=int(input("enter student grade"))
named_params = {'stud_id':'14a31a05b8', 'stud_name':'sai charan'}
res=cursor.execute("select *from students where student_id= :stud_id and student_name: stud_name",named_params)
print(res)
#row=cursor.fetch()
#print(row)
#for r in row:
    #print(r)

#cursor.close()
#con.close()
#print("connection closed")

