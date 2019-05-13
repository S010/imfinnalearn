import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random ,CSV
#https://stackabuse.com/a-sqlite-tutorial-with-python/
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

def logTask(logMessage,user):
    with open("logs.txt","r+") as data:
        data.write(str(datetime.datetime),"||",str(user),"||",logMessage)
    print("~~Task Logged~~")

def checkForKeyCode(r,table):
    cur.execute('SELECT keycode FROM '+table+' WHERE keycode='+str(r))
    data = cur.fetchall()
    if not data:
        print("key does not match keycodes")
        return False
    else:
        print("key already exists")
        return True

def getKeyCode(di):
    with open(di,"r") as data:
        reader = csv.reader(data)
        for row in reader:
            print()

def generateKeyCode():
    while True:
        randomKey = random.randint(0,999999999)
        if checkForKeyCode(randomKey,"users") == False and checkForKeyCode(randomKey,"admins") == False:
            return randomKey

def hashingPassword(p):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt,100000)
    passwordHash = binascii.hexlify(passwordHash)
    return(salt+passwordHash).decode("ascii")

def verifyPassword(s,p):
    salt = s[:64]
    s = s[64:]
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt.encode("ascii"),100000)
    passwordHash = binascii.hexlify(passwordHash).decode("ascii")
    return passwordHash == s


class User:
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
class Student(User):
    def __init__(self):
        pass

class Teacher(User):
    def __init__(self):
        pass

class Admin(User):
    def __init__(self):
        self.password = ""
        
    def adminUI(self):
        print("~~ WELCOME TO DONCASTER UNIVERSITY LIBRARY ~~")
        while True:
            command = input("1.)Take Out Item\n2.)Put Item Back\n3.)Search Items\n4.)")

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
                
    def createUser(staff,admin,pin):
        keyCode = generateKeyCode()
        firstName = input("First Name:")
        lastName = input("Last Name:")
        cur.execute("INSERT INTO users (keycode, firstname, lastname, staff, admin, pin) VALUES (?, ?, ?, ?, ?, ?)",(keyCode,firstName,lastName,staff,admin,pin))
        con.commit()
        print("User {} {} {} Created".format(keyCode,firstName,lastName))

    def createStudent():
        createUser(False,False,"")
        
    def createTeacher():
        createUser(True,False,"")
        
    def createAdmin():
        password = input("Password:")
        password =hashingPassword(password)
        createUser(False,True,password)
        
    def seeAllAccounts(table):
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
        return data

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
    



#Login function to log into the system
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


#login()
