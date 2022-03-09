#!/usr/bin/python3
""" Review module for the HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
=======
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
>>>>>>> 93aec226044c69f750b41f33ba2e57ebc53b2835

class Review(BaseModel, Base):
    """ Review classto store review information """
<<<<<<< HEAD
    __tablename__ = 'reviews'
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey=('users.id'))
    text = Column(String(1024), nullable=False)
=======
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
>>>>>>> 93aec226044c69f750b41f33ba2e57ebc53b2835
