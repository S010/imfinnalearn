import datetime
import sqllite3 as s
from sqllite3 import Error
import database

class User:

    #initializes to create variables for name, keycode and id
    def __init__(self,firstname,lastname,keycode,userType,password):
        self.firstname = firstname
        self.lastname = lastname
        self.keycode = keycode
        self.userType = userType
        self.password = password
        self.name = self.firstname+" "+self.lastname

    def takeItemOut(self):
        pass
    def takeItemsBack(self):
        pass
    def searchItems(self):
        pass
    def getDetails(self):
        pass



class Student(User):
    def UI(self):
        pass
#teacher class, inherits User.
    def __init__(self):
        pass

class Teacher(User):
    def UI(self):
        print("teacher ui")

class Admin(User):

    def __init__(self,password):
        self.password = password

    def adminUI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~")
        while True:
            command = input("1.)Take Out Item\n2.)Put Item Back\n3.)Search Items\n4.)")

    #returns all data in a specific table.
    #right now this asks for a command and if it is 1, it says "||Scans can not
    #be produced at the moment||" ? pretty sick tbh , will add nore when more is added
    #this will be produced in a tkinter ui or something soon
    def addItemUI(self):
        while True:
            command = input("What item would you like to add to the database?\n1.)Scan item\n2.)Book\n3.)Dvd\n4.)Cd\nb)Back\n>>").lower().strip(" ")
            if command == "1":
                print("||Scans can not be produced at the moment||")
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass
            elif command == "b":
                break
            else:
                print("||That is not a command||")

    def addUserUI(self):
        while True:
            command = input("What type of user would you like to create?\n1.)Student\n2.)Teacher\n3.)Admin\nBack\n>>").lower().strip(" ")
            if command == "1":
                database.db.addUser()
            elif command == "2":
                createUser(1,"")
            elif command == "3":
                password = input("Password:")
                password =hashingPassword(password)
                createUser(2,password)
            elif command == "b":
                break
            else:
                print("||That is not a command||")

    #basic ui for the admin
    def UI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~")
        while True:
            command = input("1.)Take Out Item\n2.)Put Item Back\n3.)Search Items\n4.)Add users\nb.)Back").lower().strip(" ")
            if command == "1":
                pass
            elif command == "2":
                #addItemUI()
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass
            elif command == "b":
                break
            else:
                print("||That is not a command||")
