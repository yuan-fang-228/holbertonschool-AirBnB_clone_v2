#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)


    if getenv('HBNB_TYPE_STORAGE') == "FileStorage":
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

    else:
        """ storage = db """
        cities = relationship("City", cascade="all, delete",
                            backref="state")
