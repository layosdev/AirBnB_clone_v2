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
            from models import storage
            if os.getenv("HBNB_TYPE_STORAGE") == "file":

                cities = []
                filestorage = storage.all("City")

                for key, value in filestorage.items():
                    if value.to_dict()["state_id"] == self.id:
                        cities.append(value)
                return(cities)
