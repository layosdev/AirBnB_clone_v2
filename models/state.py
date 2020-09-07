#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """ get cities """
            from models import storage
            objects = storage.all("City")
            my_cities = []
            for key, obj in objects.items():
                if obj.state_id == self.id:
                    my_cities.append(obj)
            return (my_cities)
