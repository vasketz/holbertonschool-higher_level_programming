#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    crsor = db.cursor()
    crsor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    ORDER BY id ASC")
    rows = crsor.fetchall()
    for row in rows:
        print(row)
    crsor.close()
    db.close()
