#!/usr/bin/python3
"""
Class City, inherts from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public attributes which
    can be accessed in subsequent methods
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiates class City to accept arguments
        """
        super().__init__(*args, **kwargs)
