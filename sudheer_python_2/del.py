import cx_Oracle
try:
    con = cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("conn established")
except Exception as e:
    print("EXCEPTION :",e)
cursor = con.cursor()
for i in range(0,5):
    worker_id=input("enter worker id :")
    worker_name=input("enter worker name :")
    worker_shift=input("enter worker shift :")
    worker_payscale=input("enter payscale :")
    i=i+1
    cursor.execute("insert into worker values(:1,:2,:3,:4)",(worker_id,worker_name,worker_shift,worker_payscale))

    
