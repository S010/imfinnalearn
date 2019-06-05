import datetime
import sqlite3 as s
from sqlite3 import Error
import database
import uti


class User:

    #initializes to create variables for name, keycode and id
    def __init__(self,name,keycode,userType,password):
        self.keycode = keycode
        self.userType = userType
        self.password = password
        self.name = name

# Charlie needs to do these three functions and i will do the rest :)
    def takeItemOut(self):
        pass
    def returnItem(self):
        pass
    def myItems(self):
        pass
    #This returns what type of user the user is , this is used for Ui reasons atm
    def returnUserType(self):
        if self.userType == 1:
            return "Student"
        elif self.userType == 2:
            return "Teacher"
        elif self.userType == 3:
            return "Admin"

# These two classes will be done when the user functions are complete

class Student(User):
    def UI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~\n~~ {} | {} ~~".format(self.name,self.returnUserType()))
        while True:
            command = input("1.)Take out item\n2.)Put item back\n3.)My items\nb.)Exit\n>>").lower().strip(" ")
            if command == "1":
                self.takeItemOut()
            elif command == "2":
                self.returnItem()
            elif command == "3":
                self.myItems()
            elif command == "b":
                break
            else:
                print("||Invalid command||")


class Teacher(User):
    def UI(self):
        print("teacher ui")

class Admin(User):
    #returns all data in a specific table.
    #right now this asks for a command and if it is 1, it says "||Scans can not
    #be produced at the moment||" ? pretty sick tbh , will add nore when more is added
    #this will be produced in a tkinter ui or something soon
    def deleteUserUI(self):
        while True:
            command = input("User keycode[Press b to go back]:").lower().strip(" ")
            if uti.checkForKeyCode(command,"users") == True:
                database.db.delUser(command)
                print("User deleted")
            elif command == "b":
                break
            else:
                print("||Invalid Command||")
    def deleteItemUI(self):
        while True:
            command = input("Item UID[Press b to go back]:").strip(" ")
            if uti.checkForUID(command) == True:
                database.db.delItem(command)
                print("Item deleted")
            elif command == "b" or command == "B":
                break
            else:
                print("||Invalid command||")
    def addItemUI(self):
        while True:
            command = input("What item would you like to add to the database?\n1.)Scan item\n2.)Book\nb)Back\n>>").lower().strip(" ")
            if command == "1":
                print("||Scans can not be produced at the moment||")
            elif command == "2":
                uid = int(input("UID:"))
                title = input("Title:")
                author = input("Author:")
                database.db.addItem(uid, title, author)
                print("{}:{} by {} added".format(str(uid),title,author))

            elif command == "b":
                break
            else:
                print("||That is not a command||")

    def addUserUI(self):
        while True:
            command = input("What type of user would you like to create?\n1.)Student\n2.)Teacher\n3.)Admin\nb.)Back\n>>").lower().strip(" ")
            if command == "1":
                keycode = uti.generateKeyCode()
                name = input("Name:")
                database.db.addUser(keycode, name, 0 , "")
                print("||Student created||\n{}:{}".format(name,str(keycode)))
            elif command == "2":
                keycode = uti.generateKeyCode()
                name = input("Name:")
                database.db.addUser(keycode, name, 1 , "")
                print("||Teacher created||\n{}:{}".format(name,str(keycode)))
            elif command == "3":
                keycode = uti.generateKeyCode()
                name = input("Name:")
                password = input("Password:")
                password =hashingPassword(password)
                database.db.addUser(keycode, name, 2, password)
                print("||Admin created||\n{}:{}".format(name,str(keycode)))
            elif command == "b":
                break
            else:
                print("||That is not a command||")

    #basic ui for the admin
    def UI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~\n~~ {} | {} ~~".format(self.name,self.returnUserType()))
        while True:
            command = input("1.)Take Out Item\n2.)Put Items Back\n3.)My Items\n4.)Add users\n5.)Delete users\n6.)Add Items\n7.)Delete Items\nb.)Back").lower().strip(" ")
            if command == "1":
                self.takeItemsOut()
            elif command == "2":
                self.returnItems()
            elif command == "3":
                self.myItems()
            elif command == "4":
                self.addUserUI()
            elif command == "5":
                self.deleteUserUI()
            elif command == "6":
                self.addItemUI()
            elif command == "7":
                self.deleteItemUI()

            elif command == "b":
                break
            else:
                print("||That is not a command||")
#Admin.addUserUI(Admin)
