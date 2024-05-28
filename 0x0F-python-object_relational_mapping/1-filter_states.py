#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    def list_names(user, passd, dbname):
        db = MySQLdb.connect(
                port=3306,
                user=username,
                passwd=password,
                host='localhost',
                db=dbname
                )
        cur = db.cursor()

        cur.execute(
                """
                SELECT id, name
                FROM states
                WHERE name LIKE 'N%'
                ORDER BY id ASC;
                """
                )
        """get all records"""
        my_records = cur.fetchall()
        for record in my_records:
            print(record)

        cur.close()
        db.close()
    list_names(username, password, dbname)
