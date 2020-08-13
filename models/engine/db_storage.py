#!/usr/bin/python3
""" database engine storage """
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, Query
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, ForeignKey
import os


class DBStorage:
    """ Data base storage """
    __engine = None
    __session = None

    def __init__(self):
        """ init """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_MYSQL_HOST') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        my_dict = {}
        if cls:
            for row in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(cls, row.id)
                my_dict[key] = row
        else:
            for k in ["State", "City", "User"]:
                for row in self.__session.query(eval(k)).all():
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    my_dict[key] = row
        return my_dict

    def new(self, obj):
        """ comment """
        self.__session.add(obj)

    def save(self):
        """ comment """
        self.__session.commit()

    def delete(self, obj=None):
        """ comment """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ comment """
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
