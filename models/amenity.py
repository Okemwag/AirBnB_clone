#!/usr/bin/python3
"""
Class Amenity, inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Create a public class attribute
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
