import tkinter as t
import datetime as d
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
#https://stackabuse.com/a-sqlite-tutorial-with-python/
con = s.connect("dbFile.db")
cur = con.cursor()

usertable = """ CREATE TABLE users (
            id integer PRIMARY KEY,
            firstName text NOT NULL,
            lastName text NOT NULL,
            keycode text NOT NULL
        ) """
admintable ="""CREATE TABLE admins (
            id integer PRIMARY KEY,
            firstName text NOT NULL,
            lastName text NOT NULL,
            keycode text NOT NULL,
            password text NOT NULL
        ) """
booktable = """ CREATE TABLE books (
            id integer PRIMARY KEY,
            name text NOT NULL,
            author text NOT NULL,
            takenout bit
        )"""
dvdtable = """CREATE TABLE dvds(
            id integer PRIMARY KEY,
            name text NOT NULL,
            creator text NOT NULL,
            takenout bit
        ) """

cdtable = """CREATE TABLE cds(
            id integer PRIMARY KEY,
            name text NOT NULL,
            producer text NOT NULL,
            takenout bit
        )"""

def checkForKeyCodeUsers(r):
    cur.execute('SELECT keycode FROM users WHERE keycode='+str(r))
    data =cur.fetchall()
    if not data:
        print("key does not match keycodes :)")
        return False
    else:
        print("key already exists :(")
        return True

def checkForKeyCodeAdmins(r):
    cur.execute('SELECT keycode FROM admins WHERE keycode='+str(r))
    data =cur.fetchall()
    if not data:
        print("key does not match keycodes :)")
        return False
    else:
        print("key already exists :(")
        return True

def generateKeyCode():
    while True:
        randomKey = random.randint(0,999999999)
        if checkForKeyCodeUsers(randomKey) == False and checkForKeyCodeAdmins(randomKey) == False:
            return randomKey

def generateUserId():
    cur.execute('SELECT MAX(id) FROM users')
    data = cur.fetchall()
    userId = (data[0][0]) + 1
    return userId
def generateAdminId():
    cur.execute

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

    

class Admin():
    def __init__(self):
        self.name = ""

    def adminUI(self):
        pass

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
    def removeItem(self):
        pass
    def createAdmin():
        firstName = input("First name:")
        lastName = input("Last name:")
        keyCode = generateKeyCode()
        userId = generateUserId()
        password = input("Password:")
        password = hashingPassword(password)
        cur.execute("INSERT INTO admins (id, firstname, lastname, keycode, password) VALUES (?, ?, ?, ? ,?)",(userId,firstName,lastName,str(keyCode),password))
        con.commit()
        print("Admin {} {} {} {} Created".format(userId, firstName, lastName, keyCode))

        
    def createUser():
        firstName = input("First name:")
        lastName = input("Last name:")
        keyCode = generateKeyCode()
        userId = generateUserId()
        cur.execute("INSERT INTO users (id, firstname, lastname, keycode) VALUES (?, ?, ?, ?)",(userId,firstName,lastName,str(keyCode)))
        con.commit()
        print("User {} {} {} {} Created".format(userId,firstName,lastName,str(keyCode)))

    def deleteAdmin():
        while True:
            keyCode = input("||Type b to go back||Key code:").lower().strip(" ")
            if keyCode == "b":
                break
            elif checkForKeyCodeAdmins(keyCode) == True:
                cur.execute("DELETE FROM admins WHERE keycode=?",(str(keyCode),))
                print("Admin deleted")
                break

    def seeAllAcounts(self):
        pass
    
    def seeRecentLogs(self):
        pass
    
    def login(self):
        pass

class User():
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

#Login function to log into the system
def login():
    while True:
        command = input("Select which method of sign in you would like -\n1.)Scan Card\n2.)Enter Key Code\n3.)Sign in as admin\nb.)Back\n>>").lower().strip(" ")
        if command == "1":
            print("||Key Card is currently unavailable||")
        elif command == "2":
            keyCode = input("Enter Key Code:")
            try:
                data = cur.execute('SELECT keycode FROM users WHERE keycode='+keyCode)
            except s.OperationalError:
                print("||Key code doesnt exist||\n")
        elif command == "3":
            pass
        elif command == "b":
            break
        else :
            print("||That is not a command||")




#login()
