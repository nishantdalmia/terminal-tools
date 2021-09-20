#!/usr/bin/python

import sqlite3
import hashlib

def main():
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()

    cur.execute("""CREATE TABLE passwords (
                domain text,
                password text
                )""")

    manager_entry_password = input("Enter a password to secure your password manager: ")
    h = hashlib.sha256()
    h.update(manager_entry_password)
    password_hash = h.hexidigest()
    cur.execute("""INSERT INTO passwords VALUES (?, ?)""", "master", password_hash)
    conn.commit()

if __name__ == "__main__":
    main()
