#!/usr/bin/python3
"""
script takes four arguments and and prints values
that match one of the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    searched = sys.argv[4]

    def list_values(user, passd, dbname, searched):
        """
        function takes in arguments and uses on of
        them to display contents
        """
        db = MySQLdb.connect(
                host='localhost',
                passwd=password,
                user=username,
                db=dbname
                )
        cur = db.cursor()
        query = """
        SELECT *
        FROM states
        WHERE name LIKE BINARY %s
        ORDER BY id ASC
        """
        cur.execute(query, (searched,))
        my_records = cur.fetchall()
        for record in my_records:
            print(record)
        cur.close()
        db.close()
    list_values(username, password, dbname, searched)
