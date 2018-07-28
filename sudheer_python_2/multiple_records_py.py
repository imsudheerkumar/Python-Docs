import cx_Oracle
try:
    con=cx_Oracle.connect('sudheer1122/sudheer@localhost/xe')
    print("conn established")
except Exception as e:
    print("EXCEPTION :",e)
