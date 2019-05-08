import tkinter as t
import datetime as d
import sqlite3 as s
from sqlite3 import Error
import random

##def createConnection(dbFile):
##    try:
##        conn = sqlite3.connect(dbFile)
##        return conn
##    
##    except Error as e:
##        print(e)
##
##    return None
##
##def createTable(conn,createTableSql):
##    try:
##        c = conn.cursor()
##        c.execute(createTableSql)
##
##    except Error as e:
##        print(e)
##
##        
##
##
##
##
##if __name__ == "__main__":
##    createSql()
##    
##    

class database():
    def __init__(self):
        self.name
        self.conn = s.connect(self.name+".db")

conn = s.connect("user.db")
c = conn.cursor()
conn2 = s.connect("resource.db")
q = conn2.cursor()
c.execute("CREATE TABLE user (card TEXT PRIMARY KEY, name TEXT)")


##c.execute("SELECT * FROM users WHERE card=:cardNo",{"cardNo":cardNo})

