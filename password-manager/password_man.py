#!/usr/bin/python

import sys
import sqlite3
import random
import string
import hashlib

def add_to_db(self, domain: string, key: string):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    encrypted_password = password

    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("""INSERT INTO passwords VALUES (?, ?)""", domain, encrypted_password)
    conn.commit()

    print("Domain Name: {}".format(domain))
    print("Password: {}".format(password))

def check_and_process_db(self, domain: string, key: string) -> bool:
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("""SELECT * FROM passwords WHERE domain = ?)""", domain)
    domain_data = cur.fetchall()
    conn.commit()

    if len(domain_data) == 0:
        self.add_to_db(domain, key)
    else:
        print("Domain Name: {}".format(domain_data[0]))

        decrypted_password = domain_data[1]
        print("Password: {}".format(password))


def main(argv):
    manager_entry_password = argv[0]
    master_domain = "master"

    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("""SELECT * FROM passwords WHERE domain = ?)""", master_domain)
    domain_data = cur.fetchall()
    conn.commit()

    h = hashlib.sha256()
    h.update(manager_entry_password)
    password_hash = h.hexidigest()
    if password_hash == domain_data[1]:
        domain = lower(input("Enter a domain name: "))
        check_in_db(domain, password_hash)
    else:
        print("Incorrect Password !!, Please try again !!")


if __name__ == "__main__":
    main(sys.argv[1:])
