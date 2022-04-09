#!/usr/bin/python3
"""
The module to set up the database
"""

from sqlalchemy.engine.create import create_engine
from os import getenv


class DBStorage:
    """ Class for DBStorage
    """

""" Modules for DBstorage """
import os
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ Class for the DB """

    __engine = None
    __session = None

    def __init__(self):

        """ intialization of the content """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                3306,
                getenv("HBNB_MYSQL_DB")
            ), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            from model.amenity import Amenity
            from model.city import City
            from model.place import Place
            from model.state import State
            from model.review import Review
            from model.user import User
            from model.base_model import Base

            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on current database session
        """
        dicty = {}
        if cls == None:
            for clas in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(clas).all():
                    dicty[type(obj).__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session.query(cls).all():
                dicty[type(obj).__name__ + '.' + obj.id] = obj

        return dicty

    def new(self, obj):
        """ add the object to  current db session
        """
        self.__session.add(obj)

    def save(self):
        """ commit all changes to current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from currenct db session
        """

        """ attrs of storage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ create all table in the database
        """

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ Remove or close the session """
        self.__session.close()
