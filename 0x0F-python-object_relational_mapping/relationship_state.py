#!/usr/bin/python3
"""
This file contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create a base class
Base = declarative_base()


# Define a State class that inherits from Base
class State(Base):
    """Represents a state in the database"""

    # Link to the MySQL table states
    __tablename__ = 'states'

    # Define the columns of the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Define the cities relationship with the City class
    cities = relationship("City", cascade="all, delete", backref="state")
