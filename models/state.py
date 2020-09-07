#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
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
            objects = models.storage.all("City")
            my_cities = []
            for key, obj in objects.items():
                if obj.state_id == self.id:
                    my_cities.append(obj)
            return (my_cities)
