#!/usr/bin/python

import sys, getopt
import sqlite3

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])

    # Populating DataBase.
    conn = sqlite3.connect('database.sqlite3')
    cur = conn.cursor()

    fp = open('database.sql', 'r')
    cur.executescript(fp.read())
    fp.close()

    conn.commit()

    favorites = False
    count = 0
    for item in faculty_staff:
        for d_type in item["Discount_Types"]:
            cur.execute("INSERT INTO faculty_staff VALUES(?, ?, ?, ?, ?, ?)",
                        [count, item["Provider"], item["Discount"], item["Directions"], d_type, favorites])
            count += 1

    scount = 0
    for item in students:
        for d_type in item["Discount_Types"]:
            cur.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?)",
                        [scount, item["Provider"], item["Discount"], item["Directions"], d_type, favorites])
            scount += 1

    ocount = 0
    for item in others:
        for d_type in item["Discount_Types"]:
            cur.execute("INSERT INTO others VALUES(?, ?, ?, ?, ?, ?)",
                        [ocount, item["Provider"], item["Discount"], item["Directions"], d_type, favorites])
            ocount += 1

    conn.commit()



if __name__ == "__main__":
    extract_data_and_populate_sql_database()
