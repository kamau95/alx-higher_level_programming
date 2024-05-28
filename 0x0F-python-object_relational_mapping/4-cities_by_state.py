#!/usr/bin/python3
"""use of a inner join"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    def list_cities(username, password, dbname):
        db = MySQLdb.connect(
                host='localhost',
                user=username,
                db=dbname,
                passwd=password
                )
        cur = db.cursor()
        query = """
        SELECT
        cities.id,
        cities.name,
        states.name
        from cities
        INNER JOIN
        states ON cities.state_id = states.id
        """
        cur.execute(query)
        my_records = cur.fetchall()
        for record in my_records:
            print(record)
        cur.close()
        db.close()
    list_cities(username, password, dbname)
