#!/usr/bin/python3
"""
The module to set up the database
"""

from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker
from os import getenv
from model.amenity import Amenity
from model.city import City
from model.place import Place
from model.state import State
from model.review import Review
from model.user import User
from model.base_model import Base


class DBStorage:
    """ Class for DBStorage
    """
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
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all table in the database
        """

        Base,metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
