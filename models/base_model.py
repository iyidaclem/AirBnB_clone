#!/usr/bin/python3
""" A base model class """

import uuid
from datetime import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ What class should print """

        name = self.__class__.__name__
        _id = self.id
        _dict = str(self.__dict__)
        _str = "[" + name + "] " + "(" + _id + ") " + _dict
        return _str

    def save(self):
        """ public method to update `updated_at`  """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ 
        returns a dictionary containing all keys/values of __dict__ of the instance:
        """

        our_dict = self.__dict__
        our_dict["__class__"] = self.__class__.__name__
        our_dict["created_at"] = self.created_at.isoformat()
        our_dict["updated_at"] = self.updated_at.isoformat()
        return our_dict
