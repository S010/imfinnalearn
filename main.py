import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
import database
import user
#https://stackabuse.com/a-sqlite-tutorial-with-python/

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
            if database.db.checkForKeyCode(keyCode,"users") == True:
                mainUser = database.db.returnUserInfo(keyCode)
                print(mainUser)
                #mainUser.UI()
                #cur.execute("SELECT keycode FROM users WHERE userType=0 AND WHERE keycode=",keycode)
            else:
                print("||Key Code doesnt Exist||")

        elif command == "b":
            break
        else :
            print("||That is not a command||")
