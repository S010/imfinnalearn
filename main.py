import tkinter as t
import datetime as d
import sqlite3 as s
from sqlite3 import Error
import random
import hashlib
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

def checkForKeyCode(r):
    cur.execute('SELECT keycode FROM users WHERE keycode='+str(r))
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
        if checkForKeyCode(randomKey) == False:
            return randomKey

def generateUserId():
    cur.execute('SELECT * FROM users ORDER BY id DESC LIMIT 1')
    

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
    def createAdmin(self):
        pass
    def createUser(self):
        firstName = input("First name:")
        lastName = input("Last name:")
        keyCode = generateKeyCode()
        userId = generateUserId()
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
