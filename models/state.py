#!/usr/bin/python3
"""
Class State, inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class attribute
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Class State init
        """
        super().__init__(*args, **kwargs)
