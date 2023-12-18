#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. It is safe from MySQL injections
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

    # Use format and %s placeholder to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    # Execute the SQL query with the user input as a parameter
    cursor.execute(query, (sys.argv[4],))

    # Fetch all records
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the connection
    db.close()
