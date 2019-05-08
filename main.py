import tkinter as t
import datetime as d
import sqlite3 as s
from sqlite3 import Error
import random
#https://stackabuse.com/a-sqlite-tutorial-with-python/

con = s.connect("dbFile.db")
cur = con.cursor()

usersTable = """ CREATE TABLE users (
    id integer PRIMARY KEY,
    firstName text NOT NULL,
    lastName text NOT NULL) """
cur.execute(usersTable)
bookTable = """ CREATE TABLE books (
    id integer PRIMARY KEY,
    name

)
