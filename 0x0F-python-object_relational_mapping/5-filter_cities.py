#!/usr/bin/python3
"""use of a inner join"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stated = sys.argv[4]

    def list_cities(username, password, dbname, stated):
        db = MySQLdb.connect(
                host='localhost',
                user=username,
                db=dbname,
                passwd=password
                )
        cur = db.cursor()
        query = """
        SELECT
        cities.name FROM cities
        INNER JOIN states
        ON cities.state_id=states.id
        WHERE states.name=%s
        ORDER BY cities.id ASC
        """
        cur.execute(query, (stated,))
        rows = cur.fetchall()
        tmp = list(row[0] for row in rows)
        print(*tmp, sep=", ")
        cur.close()
        db.close()
    list_cities(username, password, dbname, stated)
