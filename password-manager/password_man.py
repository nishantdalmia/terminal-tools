#!/usr/bin/python

import sys, getopt
import sqlite3
import random
import string
import hashlib
from cryptography.fernet import Fernet

def add_to_db(domain: string, key: string):
    # https://pynative.com/python-generate-random-string/#h-create-random-password-with-special-characters-letters-and-digits
    # Generate a random 12 character string to serve as a password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))

    #Password encrypted using key passed as parameter (technically password_hash)
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())

    # Connect to password manager database
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("INSERT INTO passwords VALUES (?, ?)", domain, encrypted_password)
    connection.commit()
    connection.close()

    # Print out added domain and password
    print("You have entered a new domain name. The domain has been added to the database with the credentials below.")
    print("Domain Name: {}".format(domain))
    print("Password: {}".format(password))


def fetch_in_db(domain: string, key: string):
    # Connect to password manager database
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("SELECT * FROM passwords WHERE domain = ?)", domain)
    domain_data = cur.fetchall()
    connection.commit()
    connection.close()

    if len(domain_data) == 0:
        self.add_to_db(domain, key)
    else:
        domain_data = domain_data[0]
        # Print out fetched domain and password
        print("Domain Name: {}".format(domain_data[0]))

        #Password decrypted using key passed as parameter (technically password_hash)
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(domain_data[1]).decode()

        print("Password: {}".format(password))


def show_all_db():
    # Connect to password manager database
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("SELECT * FROM passwords")
    domain_data = cur.fetchall()

    print("Domain\tPassword")
    for item in  domain_data:
        print(item[0] + "\t" + item[1])

    connection.commit()
    connection.close()

def main(argv):
    showall = False
    fetch = False
    manager_entry_password = None

    try:
        opt, args = getopt.getopt(argv, "p:sf", ["password, showall, fetch"])

    except:
        print("USAGE: password_man -p/--password #### -s/--showall -f/--fetch")

    for opt, arg in opts:
        if opt in ['-f', '--fetch']
            fetch = True
        if opt in ['-s', '--showall']
            showall = True
        if opt in ['-p', '--password']
            manager_entry_password = arg

    if password is None:
        manager_entry_password = input("Enter password to enter manager: ")

    # Connect to password manager database
    connection = sqlite3.connect('database.sqlite3')
    cur = connection.cursor()
    cur.execute("SELECT * FROM passwords WHERE domain = 'master')")
    domain_data = cur.fetchall()[0]
    conn.commit()
    connection.close()

    # Checking the hash of the password for increased security
    h = hashlib.sha256()
    h.update(manager_entry_password)
    password_hash = h.hexidigest()
    if password_hash == domain_data[1]:
        domain = lower(input("Enter a domain name: "))
        fetch_in_db(domain, password_hash)
    else:
        print("INCORRECT PASSWORD !!")


if __name__ == "__main__":
    main(sys.argv[1:])
