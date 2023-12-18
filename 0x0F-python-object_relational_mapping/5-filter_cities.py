#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
It is safe from MySQL injections.
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
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id \
    = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the SQL query with the user input as a parameter
    cursor.execute(query, (sys.argv[4],))

    # Fetch all records
    rows = cursor.fetchall()

    # Create a list of city names
    cities = []
    for row in rows:
        cities.append(row[0])

    # Print the list of city names separated by commas
    print(", ".join(cities))

    # Close the cursor
    cursor.close()

    # Close the connection
    db.close()
