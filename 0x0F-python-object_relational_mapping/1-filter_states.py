#!/usr/bin/python3
"""
script lists states starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        if i[1][0] == 'N':
            print(i)
    cursor.close()
    con.close()
