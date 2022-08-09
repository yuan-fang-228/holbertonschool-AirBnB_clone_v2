#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        """ storage = db """
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="state")
    else:
        """ storage = Filestorage """
        name = ""

        @property
        def cities(self):
            """ a getter that returns a list of cities
                where city.state_id == states.id
            """
            citylist = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    citylist.append(city)
            return citylist
