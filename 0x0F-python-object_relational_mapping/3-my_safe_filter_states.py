#!/usr/bin/python3
"""
draft a code script that process argument and
print all value in the states on codition
`name` matches the argument
from the data_base `hbtn_0e_0_usa`.
The script is safe from
MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    permission to the data_base and extracts the states
    from the data_base.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for a in rows_selected:
        print(a)
