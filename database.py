"""
Database module.

Used for interacting with the library database.
"""

import sqlite3 as sql
"""
sqlite3 module.

For use of a SQLite3 Database to store information.
"""


class LibDb(object):

    def __init__(self):
        self.con = sql.connect("dbFile.db")
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
        self.cur.execute(""" INSERT INTO users(keycode, name, userType,
            password)
            VALUES(?,?,?,?)
        """, (keycode, name, userType, password))
        self.con.commit()

    def delUser(self, keycode):
        self.cur.execute(""" DELETE FROM users WHERE keycode=? """,
                         (keycode,))
        self.con.commit()


db = LibDb()
