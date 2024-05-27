#!/usr/bin/python3
import MySQLdb
import sys


"""function to list states"""


def list_states(username, password, dbname):
    # Establish connection
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dbname
            )

    cur = db.cursor()
    my_query = """SELECT id, name FROM states ORDER BY id ASC;"""

    # Execute query
    cur.execute(my_query)

    """get all records"""
    my_records = cur.fetchall()
    for record in my_records:
        print(record)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_states(username, password, dbname)
