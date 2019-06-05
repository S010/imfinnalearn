import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
import database
import user
#https://stackabuse.com/a-sqlite-tutorial-with-python/

cur = database.db.cur
con = database.db.con


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
                user = user.Student(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            elif i == 1:
                user = user.Teacher(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            elif i == 2:
                user = user.Admin(data[0][1],data[0][2],data[0][0],data[0][3],data[0][4])
            break
    return user

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

#def getKeyCode(di):
#    with open(di,"r") as data:
#        reader = csv.reader(data)
#        for row in reader:
#            print()

def generateKeyCode():
    while True:
        randomKey = random.randint(0,999999999)
        print("creates key")
        if checkForKeyCode(randomKey,"users") == False:
            print("if statement")
            return randomKey
        if checkForKeyCode(randomKey,"users") == False and checkForKeyCode(randomKey,"admins") == False:
            return randomKey

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
