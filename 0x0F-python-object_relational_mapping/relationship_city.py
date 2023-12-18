#!/usr/bin/python3
"""
This file contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


# Define a City class that inherits from Base
class City(Base):
    """Represents a city in the database"""

    # Link to the MySQL table cities
    __tablename__ = 'cities'

    # Define the columns of the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
