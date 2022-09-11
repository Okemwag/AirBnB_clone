#!/usr/bin/python3
"""
Class Place, inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class attributes which can be used in subsequent methods
    """
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
    amenities = []

    def __init__(self, *args, **kwargs):
        """Class init"""
        super().__init__(*args, **kwargs)
