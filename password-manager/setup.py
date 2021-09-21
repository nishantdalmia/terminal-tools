#!/usr/bin/python

import sqlite3
import hashlib

def main():
    # Connect to password manager database
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("""CREATE TABLE passwords (
                    domain text,
                    password text
                )""")

    # User input to do the initial setup for the password manager
    manager_entry_password = input("Enter a password to secure your password manager: ")

    # Saving the hash of the password for increased security
    h = hashlib.sha256()
    h.update(manager_entry_password)
    password_hash = h.hexidigest()
    cur.execute("INSERT INTO passwords VALUES (?, 'master')", password_hash)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
