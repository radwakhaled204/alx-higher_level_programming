#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument from
the database hbtn_0e_6_usa. It is safe from SQL injections.
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

    # Query the State object with the name passed as argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the state's id if it exists, otherwise print Not found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
