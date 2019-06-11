import database
import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
import user
#https://stackabuse.com/a-sqlite-tutorial-with-python/

#Login function to log into the system, currently just checks to see if
#keycode is valid.

#Login function to log into the system
def getUser(keycode):
    data = database.db.returnUser(keycode)
    print(data)
    if data[0][2] == 0:
        user = user.Student(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
    elif data[0][2] == 1:
        user = user.Teacher(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
    elif data[0][2] == 2:
        user = user.Admin(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
    return user


def login():
    while True:
        command = input("Select which method of sign in you would like -\n1.)Scan Card\n2.)Enter Key Code\nb.)Back\n>>").lower().strip(" ")
        if command == "1":
            print("||Scanner is currently unavailable||")
        elif command == "2":
            keyCode = input("Enter Key Code:")
            if database.db.checkForKeyCode(keyCode) == False:
                print("||Key code does not exist||")
            else:
                mainUser = database.db.returnUserInfo(keyCode)[0]
                if mainUser[2] == 2:
                    password = input("Password:")
                    if database.db.verifyPassword(mainUser[3],password) == True:
                        newUser =user.Admin(mainUser[1], mainUser[0], mainUser[2], mainUser[3])
                        newUser.UI()
                    else:
                        print("Password Invalid")
                elif mainUser[2] == 0:
                    newUser = user.User(mainUser[1], mainUser[0], mainUser[2], mainUser[3])
                    newUser.UI()
                elif mainUser[2] == 1:
                    newUser = user.Teacher(mainUser[1], mainUser[0], mainUser[2], mainUser[3])
                    newUser.UI()
        elif command == "b":
            break
        else :
            print("||That is not a command||")

login()
