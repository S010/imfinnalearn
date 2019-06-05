import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
import database
import user
import uti
#https://stackabuse.com/a-sqlite-tutorial-with-python/
cur = database.db.cur
con = database.db.con


#Login function to log into the system, currently just checks to see if
#keycode is valid.

#Login function to log into the system

def login():
    while True:
        command = input("Select which method of sign in you would like -\n1.)Scan Card\n2.)Enter Key Code\nb.)Back\n>>").lower().strip(" ")
        if command == "1":
            print("||Scanner is currently unavailable||")
        elif command == "2":
            keyCode = input("Enter Key Code:")
            if uti.checkForKeyCode(keyCode,"users") == True:
                mainUser = uti.returnUserInfo(keyCode)
                print(mainUser)
                #mainUser.UI()
                cur.execute("SELECT keycode FROM users WHERE userType=0 AND WHERE keycode=",keycode)
            else:
                print("||Key Code doesnt Exist||")

        elif command == "b":
            break
        else :
            print("||That is not a command||")
