#!/usr/bin/python3
from datetime import datetime, date, time
from models import storage
from uuid import uuid4
"""
Class that other objects inherit from
"""
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    classname = "BaseModel"
    """BaseModel class"""
    """def __init__(self, *args, **kwargs):
        Init for BaseModel class
        formatdate = '%Y-%m-%d %H:%M:%S.%f'
        if args and type(args[0]) is dict:
            self.__dict__ = args[0]
            self.__dict__['created_at'] = datetime.strptime(
                (self.__dict__['created_at']), formatdate)
            self.__dict__['updated_at'] = datetime.strptime(
                (self.__dict__['updated_at']), formatdate)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)"""
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        dstrp = datetime.strptime
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.__dict__['created_at'] = dstrp(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.__dict__['updated_at'] = dstrp(kwargs["updated_at"], time)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """
        Return class name, id, and dictionary to be printed
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        )

    def save(self):
        """
        Saves current datetime, calls
        a function, saves it into a dictionary,
        and converts it to a string to save to a file
        """
        self.updated_at = datetime.now()
        storage.save()
