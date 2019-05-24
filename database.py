import sqlite3 as sql


class libDb(object):
    def __init__(self):
        self.con = sql.connect("dbFile.db")
        self.cur = self.con.cursor()

    def createDb(self):
        self.cur.execute(""" CREATE TABLE "users" (
            "keycode"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "userType"	INTEGER NOT NULL,
            "password"	TEXT NOT NULL,
            PRIMARY KEY("keycode")
        ); """)

        self.cur.execute(""" CREATE TABLE "items" (
            "uid" INTEGER NOT NULL UNIQUE,
            "title" TEXT NOT NULL,
            "author" TEXT NOT NULL,
            PRIMARY KEY("uid")
        ); """)

        self.cur.execute(""" CREATE TABLE "takenItems" (
            "takenID" INTEGER NOT NULL UNIQUE,
            "keycode"	INTEGER NOT NULL UNIQUE,
            "uid" INTEGER NOT NULL UNIQUE,
            PRIMARY KEY("takenID"),
            FOREIGN KEY (keycode) REFERENCES users(keycode),
            FOREIGN KEY (uid) REFERENCES items(uid)
        ); """)

        self.con.commit()


db = libDb()
db.createDb()
