import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# try:
#     result = render_er(Base, 'diagram.png')
#     print("Success! Check the diagram.png file")
# except Exception as e:
#     print("There was a problem genering the diagram")
#     raise e





class Characters(Base):
    __tablename__ = 'characters'
    name = Column(String(250), ForeignKey('vehicle.pilot'), ForeignKey('favorites.favorite_chracters'))
    planet_from = Column(String(250),  ForeignKey('planets.name'))
    id = Column(String(250), primary_key=True)
    age = Column(Integer)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    name = Column(String(250), ForeignKey('favorites.favorite_planet'))
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), ForeignKey('favorites.favorite_vehicles') )
    pilot = Column(String(250))
    type = Column(String(250))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, ForeignKey('favorites.user_id'), primary_key=True)
    username = Column(String(250), nullable=False)
    password= Column(String(250), nullable=False)
  
    
class Favorites(Base):
    __tablename__ = 'favorites'
    date_added = Column(DateTime(False))
    user_id = Column(Integer,primary_key=True)
    favorite_chracters = Column(String(250))
    favorite_planets = Column(Integer)
    favorite_vehicles = Column(Integer)
    

    def to_dict(self):
        return {}



render_er(Base, 'diagram.png')
