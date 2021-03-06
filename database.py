"""
Database module.

Used for interacting with the library database.
"""

import tkinter as t
import datetime
import sqlite3 as s
from sqlite3 import Error
import hashlib, binascii , os ,random
import user

"""
sqlite3 module.

For use of a SQLite3 Database to store information.
"""


class LibDb(object):

    def __init__(self):
        self.con = s.connect("dbFile.db")
        self.cur = self.con.cursor()
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS "users" (
            "keycode"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "userType"	INTEGER NOT NULL,
            "password"	TEXT NOT NULL,
            PRIMARY KEY("keycode")
        ); """)

        self.cur.execute(""" CREATE TABLE IF NOT EXISTS "items" (
            "uid" INTEGER NOT NULL UNIQUE,
            "title" TEXT NOT NULL,
            "author" TEXT NOT NULL,
            PRIMARY KEY("uid")
        ); """)

        self.cur.execute(""" CREATE TABLE IF NOT EXISTS "takenItems" (
            "takenID" INTEGER NOT NULL UNIQUE,
            "keycode"	INTEGER NOT NULL UNIQUE,
            "uid" INTEGER NOT NULL UNIQUE,
            PRIMARY KEY("takenID"),
            FOREIGN KEY (keycode) REFERENCES users(keycode),
            FOREIGN KEY (uid) REFERENCES items(uid)
        ); """)

        self.con.commit()

    def addUser(self, keycode, name, userType, password):
        try:
            self.cur.execute(""" INSERT INTO users(keycode, name, userType,password)VALUES(?,?,?,?)""",
                            (keycode, name, userType, password))
            self.con.commit()
        except s.IntegrityError:
            print("!!!")
    def delUser(self, keycode):
        self.cur.execute(""" DELETE FROM users WHERE keycode=? """,
                         (keycode,))
        self.con.commit()

    def addItem(self,uid,title,author):
        try:
            self.cur.execute("""INSERT INTO items (uid,title,author) VALUES (?, ?, ?) """,
                            (uid,title,author))
            self.con.commit()
        except s.IntegrityError:
            print("!!!")
    def addItemTakenItems(self,takenID,uid,keycode):
        self.cur.execute("""INSERT INTO takenItems (takenID,uid,keycode) VALUES (?, ?, ?)""",
                        (takenID,uid,keycode))
        self.con.commit()

    def delItemTakenItems(self,uid,keycode):
        self.cur.execute("""DELETE FROM takenItems WHERE uid=? AND keycode=?""",
                        (uid,keycode))
        self.con.commit()

    def delItem(self,uid):
        self.cur.execute(""" DELETE FROM items WHERE uid=? """,
                        (uid))
        self.con.commit()

    def checkIfItemAvailable(self,uid):
        self.cur.execute("""SELECT uid FROM takenItems WHERE uid=? """,(uid))
        data = self.cur.fetchall()
        if not data:
            return False
        else:
            return True

    def seeAll(self,table):
        try:
            self.cur.execute("""SELECT * FROM """+table)
            data = self.cur.fetchall()
            return data
        except Exception as e:
            print("Error: %s"% str(e))

    def returnUserInfo(self,keycode):
        self.cur.execute("""SELECT * FROM users WHERE keycode=?""",(keycode,))
        data = self.cur.fetchall()
        return data

    def checkForKeyCode(self,r):
        self.cur.execute("""SELECT keycode FROM users WHERE keycode=?""",(r,))
        data = self.cur.fetchall()
        if not data:
            return False
        else:
            return True

    def checkForUID(self,uid):
        self.cur.execute('SELECT uid FROM items WHERE uid='+str(uid))
        data = self.cur.fetchall()
        if not data:
            return False
        else:
            return True

    #???? print()? *Jacob - I dont know how to do this or what the file format is gonna look like so i just gave up

    #def getKeyCode(di):
    #    with open(di,"r") as data:
    #        reader = csv.reader(data)
    #        for row in reader:
    #            print()

    def generateKeyCode(self):
        while True:
            randomKey = random.randint(0,999999999)
            if self.checkForKeyCode(randomKey) == False:
                return randomKey

    def checkTakenID(self,taken):
        self.cur.execute("""SELECT takenID FROM takenItems WHERE takenID = ?""",(str(taken),))
        data= self.cur.fetchall()
        if not data:
            return False
        else:
            return True

    def generateTakenID(self):
        while True:
            randomKey = random.randint(0,999999999)
            if self.checkTakenID(randomKey) == False:
                return randomKey

    def hashingPassword(self,p):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt,100000)
        passwordHash = binascii.hexlify(passwordHash)
        return(salt+passwordHash).decode("ascii")

    #s = hashedPassword from hashingPasword , p = password to check against/password
    #This function checks if a hashedpassword is the same as a string, returns a boolean value
    def verifyPassword(self,s,p):
        salt = s[:64]
        s = s[64:]
        passwordHash = hashlib.pbkdf2_hmac("sha256",p.encode("utf-8"),salt.encode("ascii"),100000)
        passwordHash = binascii.hexlify(passwordHash).decode("ascii")
        return passwordHash == s


    def takeItems(self,uid,keycode):
        if self.checkIfItemAvailable(uid) == True:
            print("Item is not available")
        else:
            self.addItemTakenItems(self.generateTakenID(), uid, keycode)

    #def putItems(self,uid,keycode):
    #    self.cur.execute("""SELECT uid FROM takenItems WHERE uid=? AND keycode=?""",(uid,keycode,))
    #    data = self.cur.fetchall()
    #    if not data:
    #        self.delItemTakenItems(uid, keycode)
    #    else:
    #        print("You do not own this item")

    def myItems(self,keycode):
        items = []
        self.cur.execute("""SELECT * FROM takenItems WHERE keycode=?""",(keycode,))
        data = self.cur.fetchall()
        for i in data:
            self.cur.execute("""SELECT * FROM items WHERE uid=?""",(i[2],))
            j = self.cur.fetchall()
            items.append(j)
        return items

    def returnItemBy(self,by,index):
        self.cur.execute("""SELECT * FROM items WHERE ?=?""",(by,index,))
        data = self.cur.fetchall()
        return data

    def checkForItems(self,by,index):
        self.cur.execute("""SELECT ? FROM items WHERE ?=?""",(by,index,by))
        data = cur.fetchall()
        if not data:
            return False
        else:
            return True

db = LibDb()
#db.addUser(db.generateKeyCode(), "Jacob Morgan", 2, db.hashingPassword("1234"))
#98219281 yikes
#print(db.myItems(98219281))
