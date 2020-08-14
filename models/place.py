#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String, Integer, Float, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if (os.getenv("HBNB_TYPE_STORAGE") == "db"):

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        description = Column(String(1024), nullable=True)
        reviews = relationship(
            'Review', cascade='all, delete', backref='place')
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            backref="places",
            viewonly=False)

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ get reviews """
            review_list = []
            for key, val in models.storage.items().all():
                class_name = val.__class__.__name__
                if class_name == 'Review':
                    if val.place_id == self.id:
                        review_list.append(val)
            return (review_list)

        @property
        def amenities(self):
            """ get amenities """
            amenities_list = []
            for key, val in models.storage.items().all():
                class_name = val.__class__.__name__
                if class_name == 'Amenity':
                    if val.place_id == self.id:
                        amenities_list.append(val)
            return (amenities_list)

        @amenities.setter
        def amenities(self, obj):
            """ setter amenities """
            if obj.__class__.__name__ == "Amenity":
                amenity_ids.append(obj.id)
