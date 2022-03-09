#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
<<<<<<< HEAD

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = user
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")

=======
from sqlalchemy.orm import relationship
# import models


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place",
                          backref="user",
                          cascade="all, delete, delete-orphan")
>>>>>>> 93aec226044c69f750b41f33ba2e57ebc53b2835
    reviews = relationship("Review", backref="user",
                           cascade="all, delete, delete-orphan")
