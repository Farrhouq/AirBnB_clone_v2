#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity =  Table("place_amenity", Base.metadata,
                           Column("place_id", String(60),
                                  ForeignKey("places.id"),
                                  nullable=False, primary_key=True),
                           Column("amenity_id", String(60),
                                  ForeignKey("amenities.id"),
                                  nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="places", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, backref="place_amenities")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            """a getter attribute for reviews"""
            return [i for i in list(models.storage.all(Review).values())
                    if i.place_id == self.id]

        @property
        def amenities(self):
            """THis is the properties getter"""
            amenities_list = []
            for i in list(models.storage.all(Amenity).values()):
                if i.place_id == self.id:
                    amenities_list.append(i)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """This is the setter for amenities"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)