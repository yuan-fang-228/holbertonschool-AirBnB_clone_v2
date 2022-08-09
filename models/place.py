#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
import os
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            reviewList = []
            reviewAll = models.storage.all(Review)
            for review in reviewAll.value():
                if self.id == review.place_id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            amenityList = []
            amenityAll = models.storage.all(Amenity)
            for amenity in amenityAll.value():
                if self.id == amenity_ids:
                    amenityList.append(amenity)
            return amenity

        @amenities.setter
        def amenities(self, obj=None):
            """setter attribute adding Amenity.id to attribute amenity_ids"""
            if obj is not None and type(obj).__name__ is Amenity:
                self.amenity_ids.append(obj.id)
