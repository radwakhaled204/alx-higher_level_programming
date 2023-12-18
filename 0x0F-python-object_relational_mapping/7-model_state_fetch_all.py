#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query the State table and order the results by id
    states = session.query(State).order_by(State.id).all()

    # Print each state's id and name
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
