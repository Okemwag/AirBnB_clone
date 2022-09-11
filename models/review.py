#!/usr/bin/python3
"""
Review class, inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class attributes
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Class init Review"""
        super().__init__(*args, **kwargs)
