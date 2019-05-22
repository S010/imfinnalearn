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
            userType integer,
            pin text NOT NULL
        ) """
itemtable = """ CREATE TABLE items (
            uid integer PRIMARY KEY,
            title text NOT NULL,
            author text NOT NULL,
            takenout integer,
            takenoutby text NOT NULL
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


#Checks the users userType and returns the usersdata in the form of a userclass
def returnUserInfo(keyCode):
    for i in range(3):
        cur.execute("SELECT * FROM users WHERE userType=? AND keycode=?",(i,keyCode))
        data = cur.fetchall()
        if not data:
            print("User type is not "+str(i))
        else:
            print("User type is "+str(i))
            if i == 0:
                user = Student(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            elif i == 1:
                user = Teacher(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            elif i == 2:
                user = Admin(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            break
    return user
    

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

def checkForUID(uid):
    cur.execute('SELECT uid FROM items WHERE uid='+str(uid))
    data = cur.fetchall()
    if not data:
        print("UID doesnt exist")
        return False
    else:
        print("UID already exists")
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
        if checkForKeyCode(randomKey,"users") == False:
            print("if statement")
            return randomKey


#creates a salted hash of p, why the swap from sha256 for the salt to
#pbkdf2_hmac for the hash???
def hashingPassword(p):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt,100000)
    passwordHash = binascii.hexlify(passwordHash)
    return(salt+passwordHash).decode("ascii")

#s = hashedPassword from hashingPasword , p = password to check against/password
#This function checks if a hashedpassword is the same as a string, returns a boolean value
def verifyPassword(s,p):
    salt = s[:64]
    s = s[64:]
    passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt.encode("ascii"),100000)
    passwordHash = binascii.hexlify(passwordHash).decode("ascii")
    return passwordHash == s

#user class
class User:
    #initializes to create variables for name, keycode and id
    def __init__(self,firstname,lastname,keycode,userType,password):
        self.firstname = firstname
        self.lastname = lastname
        self.keycode = keycode
        self.userType = userType
        self.userType = password
        self.name = self.firstname+" "+self.lastname
    def takeItemOut(self):
        pass
    def takeItemsBack(self):
        pass
    def searchItems(self):
        pass
    def getDetails(self):
        pass

#student class, inherits User.
class Student(User):
    def UI(self):
        print("student ui")
#teacher class, inherits User.
class Teacher(User):
    def UI(self):
        print("teacher ui")

#admin class, inherits User.
class Admin(User):
    def __init__(self,password):
        self.password = password

    def addItem(self):
        uid = input("Enter UID:")
        title = input("Enter title:")
        author = input("Enter author:")
        takenOut = 0
        takenOutBy = ""
        cur.execute("INSERT INTO items (uid, title, author, takenout, takenoutby) VALUES (?, ?, ?, ?, ?)",(uid,title,author,takenOut,takenOutBy))
        con.commit()
        print("Item {} , {} , by {}".format(uid,title,author))
        
    def removeItem(self):
        while True:
            uid = input("||Type b to go back||\nUID:").lower().strip(" ")
            if keyCode == "b":
                break
            elif checkForUID(uid) == True:
                cur.execute("DELETE FROM items WHERE uid="+uid)
                print("Item deleted")
                break
            else:
                print("||Invalid Input||")
                
    #creates a user object using a boolean for staff and admin and an integer
    #for pin its pin ,WHEN PROGRAMMING FOR USER MAKE PIN "" since the user has no password
    def createUser(userType,pin):
        keyCode = generateKeyCode()
        firstName = input("First Name:")
        lastName = input("Last Name:")
        cur.execute("INSERT INTO users (keycode, firstName, lastName, userType, pin) VALUES (?, ?, ?, ?, ?)",(keyCode,firstName,lastName,userType,pin))
        con.commit()
        print("User {} {} {} Created".format(keyCode,firstName,lastName))

    #returns all data in a specific table.
    def seeAllAccounts(table):
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
        return data

    #deletes a user by keycode.
    def removeUser(self,table):
        print(self.seeAllAccounts(table))
        while True:
            keyCode = input("||Type b to go back||\nKey code:").lower().strip(" ")
            if keyCode == "b":
                break
            elif checkForKeyCode(keyCode,table) == True:
                cur.execute("DELETE FROM users WHERE keycode="+keyCode)
                print("User deleted")
                break
            else:
                print("||Invalid Input||")

    def seeRecentLogs(self):
        pass
        
    #right now this asks for a command and if it is 1, it says "||Scans can not
    #be produced at the moment||" ? pretty sick tbh , will add nore when more is added
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
                createUser(0,"")
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

#Login function to log into the system, currently just checks to see if
#keycode is valid.
def login():
    while True:
        command = input("Select which method of sign in you would like -\n1.)Scan Card\n2.)Enter Key Code\nb.)Back\n>>").lower().strip(" ")
        if command == "1":
            print("||Scanner is currently unavailable||")
        elif command == "2":
            keyCode = input("Enter Key Code:")
            if checkForKeyCode(keyCode,"users") == True:
                user = returnUserInfo(keyCode)
                user.UI()
            else:
                print("||Key Code doesnt Exist||")
        elif command == "b":
            break
        else :
            print("||That is not a command||")
