#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel):
    """Amenities of the place to stay"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = ""
