#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    # Create a session object
    session = Session()

    # Create a new State object with the name “California”
    new_state = State(name="California")

    # Create a new City object with the name “San Francisco”
    # and link it to the new State object
    new_city = City(name="San Francisco", state=new_state)

    # Add the new State and City objects to the session
    session.add(new_state)
    session.add(new_city)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
