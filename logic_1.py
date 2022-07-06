import cx_Oracle
import traceback

conn=None
try:
    conn=cx_Oracle.connect("mojo/mojo@127.0.0.1/XE")
    print("Connected succesfully to the database")
    print("db version:",conn.version)
    print("Username:",conn.username)
except cx_Oracle.DatabaseError:
   print("Sorry Connectiuon failed")
   print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected succesfully with the db")