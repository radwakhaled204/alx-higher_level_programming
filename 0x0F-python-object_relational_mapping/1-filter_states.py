#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],  # username
        passwd=sys.argv[2],  # password
        db=sys.argv[3],  # database name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SQL query
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC"
            )

    # Fetch all records
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the connection
    db.close()
