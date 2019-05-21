#Import all libraries needed.
import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random ,csv

#https://stackabuse.com/a-sqlite-tutorial-with-python/
#making a connection to the sql db as well as making a cursor for it
con = s.connect("dbFile.db")
cur = con.cursor()


#key code is imported from a CSV

usertable = """ CREATE TABLE users (
            keycode integer PRIMARY KEY,
            firstName text NOT NULL,
            lastName text NOT NULL,
            staff bit,
            admin bit,
            pin text NOT NULL
        ) """
booktable = """ CREATE TABLE books (
            uid integer PRIMARY KEY,
            name text NOT NULL,
            author text NOT NULL,
            takenout bit
        )"""
##dvdtable = """CREATE TABLE dvds(
##            id integer PRIMARY KEY,
##            name text NOT NULL,
##            creator text NOT NULL,
##            takenout bit
##        ) """
##
##cdtable = """CREATE TABLE cds(
##            id integer PRIMARY KEY,
##            name text NOT NULL,
##            producer text NOT NULL,
##            takenout bit
##        )"""

#logs a task done by a specific user in file "logs.txt"
def logTask(logMessage,user):
    with open("logs.txt","r+") as data:
        data.write(str(datetime.datetime),"||",str(user),"||",logMessage)
    print("~~Task Logged~~")

#checks to see if a keycode entered is valid and within the user tables.
def checkForKeyCode(r,table):
    cur.execute('SELECT keycode FROM '+table+' WHERE keycode='+str(r))
    data = cur.fetchall()
    if not data:
        print("key does not match keycodes")
        return False
    else:
        print("key already exists")
        return True

#???? print()? *Jacob - I dont know how to do this or what the file format is gonna look like so i just gave up
def getKeyCode(di):
    with open(di,"r") as data:
        reader = csv.reader(data)
        for row in reader:
            print()

# makes a keycode (0-999999999), checks if it exists, if not returns it.
def generateKeyCode():
    while True:
        print("while true")
        randomKey = random.randint(0,999999999)
        print("creates key")
        if checkForKeyCode(randomKey,"users") == False and checkForKeyCode(randomKey,"admins") == False:
            print("if statement")
            return randomKey

#creates a salted hash of p, why the swap from sha256 for the salt to
#pbkdf2_hmac for the hash???
def hashingPassword(p):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt,100000)
    passwordHash = binascii.hexlify(passwordHash)
    return(salt+passwordHash).decode("ascii")

#what is s and what is p wtf. ? like ik what this is meant to do but does it do
#it?? looks like a fucked up version of the function above.
def verifyPassword(s,p):
    salt = s[:64]
    s = s[64:]
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt.encode("ascii"),100000)
    passwordHash = binascii.hexlify(passwordHash).decode("ascii")
    return passwordHash == s

#user class
class User:
    #initializes to create variables for name, keycode and id
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.keycode = ""
        self.id = ""

    def takeItemOut(self):
        pass
    def takeItemsBack(self):
        pass
    def searchItems(self):
        pass
    def userUI(self):
        pass
    def getDetails(self):
        pass

#student class, inherits User.
class Student(User):
    def __init__(self):
        pass
#teacher class, inherits User.
class Teacher(User):
    def __init__(self):
        pass

#admin class, inherits User.
class Admin(User):
    def __init__(self):
        self.password = ""

    #basic ui for the admin
    def adminUI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~")
        while True:
            command = input("1.)Take Out Item\n2.)Put Item Back\n3.)Search Items\n4.)")

    #right now this asks for a command and if it is 1, it says "||Scans can not
    #be produced at the moment||" ? pretty sick tbh
    def addItem(self):
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

    #creates a user object using a boolean for staff and admin and an integer
    #for pin its pin
    def createUser(staff,admin,pin):
        keyCode = generateKeyCode()
        firstName = input("First Name:")
        lastName = input("Last Name:")
        cur.execute("INSERT INTO users (keycode, firstname, lastname, staff, admin, pin) VALUES (?, ?, ?, ?, ?, ?)",(keyCode,firstName,lastName,staff,admin,pin))
        con.commit()
        print("User {} {} {} Created".format(keyCode,firstName,lastName))

    #these are self explanatory but really weird ngl.
    def createStudent():
        createUser(False,False,"")

    def createTeacher():
        createUser(True,False,"")

    #wait all users dont have passwords??? i feel they all should?
    def createAdmin():
        password = input("Password:")
        password =hashingPassword(password)
        createUser(False,True,password)

    #returns all data in a specific table.
    def seeAllAccounts(table):
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
        return data

    #deletes a user by keycode.
    def removeUser(self,table):
        print(self.seeAllAccounts(table))
        while True:
            keyCode = input("||Type b to go back||\nKey code:")
            if keyCode == "b":
                break
            elif checkForKeyCode(keyCode,table) == True:
                cur.execute("DELETE FROM ? WHERE keycode=?",(table,str(keyCode)))
                print("Admin deleted")
                break
            else:
                print("||Invalid Input||")

    def seeRecentLogs(self):
        pass




#Login function to log into the system, currently just checks to see if
#keycode is valid.
def login():
    while True:
        command = input("Select which method of sign in you would like -\n1.)Scan Card\n2.)Enter Key Code\n3.)Sign in as admin\nb.)Back\n>>").lower().strip(" ")
        if command == "1":
            print("||Key Card is currently unavailable||")
        elif command == "2":
            keyCode = input("Enter Key Code:")
            if checkForKeyCode(keyCode,"users") == True:
                pass
            else:
                print("||Key Code doesnt Exist||")

        elif command == "3":
            keyCode = input("Enter Key Code:")
            if checkForKeyCode(keyCode,"admins") == True:
                pass
        elif command == "b":
            break
        else :
            print("||That is not a command||")
