#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    def list_names(user, passd, dbname):
        """
         Connects to the MySQL database,
         retrieves records from the 'states' table
         where the name starts with 'N', and prints them.
        """
        db = MySQLdb.connect(
                port=3306,
                user=username,
                passwd=password,
                host='localhost',
                db=dbname
                )
        cur = db.cursor()

        cur.execute("""SELECT * FROM states WHERE name
                        LIKE BINARY 'N%' ORDER BY states.id"""
                    )
        """get all records"""
        my_records = cur.fetchall()
        for record in my_records:
            print(record)

        cur.close()
        db.close()
    list_names(username, password, dbname)
