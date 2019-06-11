import database
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
"""
If the db is not an atribute error comes back

Run Database.py :)

"""


class User(object):

    #initi33alizes to create variables for name, keycode and id
    def __init__(self,name,keycode,userType,password):
        self.keycode = keycode
        self.userType = userType
        self.password = password
        self.name = name

    def takeItemOutUI(self):
        #check who has item , display availble items , input UID, add takenItems
        while True:
            print("|    UID    |    Title   |   Author  |")
            owneduids = []
            uids = []
            items = database.db.seeAll("items")
            takenItems = database.db.seeAll("takenItems")
            for i in range(len(takenItems)):
                owneduids.append(takenItems[i-1][2])
            for i in range(len(items)):
                    if items[i-1][0] not in owneduids:
                        print("      {}          {}         {}".format(items[i-1][0],items[i-1][1],items[i-1][2]))
                        uids.append(items[i-1][0])
            if uids == []:
                print("No items available")
                break

            command = input("Uid of Item you would like to take out[b to go back]:").lower().strip(" ")
            if command == "b":
                break
            elif int(command) in uids:
                database.db.takeItems(command, self.keycode)
                print("Item taken")



    def returnItemUI(self):
        while True:
            print("|    UID    |    Title   |   Author  |")
            items = database.db.myItems(self.keycode)
            uids = []
            for i in range(len(items)) :
                for j in items[i-1] :
                    print("      {}          {}         {}".format(j[0],j[1],j[2]))
                    uids.append(j[0])
            if items == []:
                print("You do not have any items!")
                break
            command = input("Uid of Item you are returning[b to go back]:").lower().strip(" ")
            if command == "b":
                break
            elif int(command) in uids:
                database.db.delItemTakenItems(command,self.keycode)
                print("Item put back into library")

    def myItemsUI(self):
        print("|    UID    |    Title   |   Author  |")
        items = database.db.myItems(self.keycode)
        for i in range(len(items)) :
            for j in items[i-1] :
                print("      {}          {}         {}".format(j[0],j[1],j[2]))



#    Search ui , will do this on wednesday
#    def searchItemUI(self):
#        while True:
#            command = input("What would you like to search by?\n1.)UID\n2.)Title\n3.)Author\nb.)Back").lower().strip(" ")
#            if command == "1":
#                while True:
#                    command = input("UID[b for back]:").lower().strip(" ")
#                    if database.db.checkForUID(command) == True:
#                        data = database.db.returnItemBy("uid", int(command))
#                        print(data)
#                    elif database.db.checkForUID(command) == False:
#                        print("UID does not exist")
#                    elif command == "b":
#                        break
#                    else:
#                        print("Command invalid")
#            elif command == "2":
#                while True:
#                    command = input("Title[b for back]:")
#                    if database.db.checkForItems(command, "title") == True:
#                        data = database.db.returnItemBy("title", command)
#                    elif database.db.checkForItems(command, "title") == False:
#                        print("Title doe not exist")
#                    elif command == "b" or command == "B":
#                        break
#                    else:
#                        print("Command invalid")
#            elif command == "3":
#                while True:
#                    command = input("Author[b for back]:")
#                    if database.db.checkForItems(command, "author") == True:
#                        data = database.db.returnItemBy("author", command)
#                    elif database.db.checkForItems(command, "author") == False:
#                        print("Author doesnt exist")
#                    elif command == "b" or command == "B":
#                        break
#                    else:
#                        print("Command invalid")
#            elif command == "b":
#                break
#                """
    #This returns what type of user the user is , this is used for Ui reasons atm
    def returnUserType(self):
        if self.userType == 0:
            return "Student"
        elif self.userType == 1:
            return "Teacher"
        elif self.userType == 2:
            return "Admin"

# These two classes will be done when the user functions are complete
class Student(User):
    def UI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~\n~~ {} | {} ~~".format(self.name,self.returnUserType()))
        while True:
            command = input("1.)Take out item\n2.)Put item back\n3.)My items\nb.)Exit\n>>").lower().strip(" ")
            if command == "1":
                self.takeItemOutUI()
            elif command == "2":
                self.returnItemUI()
            elif command == "3":
                self.myItemsUI()
            elif command == "b":
                break
            else:
                print("||Invalid command||")

class Teacher(User):
    def UI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~\n~~ {} | {} ~~".format(self.name,self.returnUserType()))
        while True:
            command = input("1.)Take out item\n2.)Put item back\n3.)My items\nb.)Exit\n>>").lower().strip(" ")
            if command == "1":
                self.takeItemOutUI()
            elif command == "2":
                self.returnItemUI()
            elif command == "3":
                self.myItemsUI()
            elif command == "b":
                break
            else:
                print("||Invalid command||")

class Admin(User):
    #this will be produced in a tkinter ui or something soon
    def deleteUserUI(self):
        while True:
            command = input("User keycode[Press b to go back]:").lower().strip(" ")
            if database.db.checkForKeyCode(command,"users") == True:
                database.db.delUser(command)
                print("User deleted")
            elif command == "b":
                break
            else:
                print("||Invalid Command||")
    def deleteItemUI(self):
        while True:
            command = input("Item UID[Press b to go back]:").strip(" ")
            if database.db.checkForUID(command) == True:
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
                keycode = database.db.generateKeyCode()
                name = input("Name:")
                database.db.addUser(keycode, name, 0 , "")
                print("||Student created||\n{}:{}".format(name,str(keycode)))
            elif command == "2":
                keycode = database.db.generateKeyCode()
                name = input("Name:")
                database.db.addUser(keycode, name, 1 , "")
                print("||Teacher created||\n{}:{}".format(name,str(keycode)))
            elif command == "3":
                keycode = database.db.generateKeyCode()
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
            command = input("1.)Take Out Item\n2.)Put Items Back\n3.)My Items\n4.)Add users\n5.)Delete users\n6.)Add Items\n7.)Delete Items\nb.)Back\n>>").lower().strip(" ")
            if command == "1":
                self.takeItemOutUI()
            elif command == "2":
                self.returnItemUI()
            elif command == "3":
                self.myItemsUI()
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
