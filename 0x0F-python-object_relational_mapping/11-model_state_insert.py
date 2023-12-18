#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # Create a new State object with the name “Louisiana”
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
