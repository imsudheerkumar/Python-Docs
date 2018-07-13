import mysql.connector
import sqlite3 
class DBconn:
    con=''
    def opencon():
        try:
            con=mysql.connector.connect(user='root',
                                        password='root',
                                        host='127.0.0.1',
                                        database='employee')
            print("conn established")
            cur=con.cursor()
            cur.execute("insert into emp values(103,'kishore')")
            print("values added successfully!!!")
            return
        except Exception as e:
            print("EXCEPTION :",e)
            return
        finally:
            if DBconn.con!='':
                DDconn.close()
                print("connection closed")
                return
        
class mainclass:
    def main():
        DBconn.opencon()
        return


if __name__=='__main__':
    mainclass.main()

    
    
