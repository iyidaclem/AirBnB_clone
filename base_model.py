#!/usr/bin/python3
""" A base model class """

import uuid
import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()

    def __str__(self):
        """ What class should print """

        _str = "[<class name>] (<self.id>) <self.__dict__>"
        return _str

    def save(self):
        """ public method to update `updated_at`  """

        BaseModel().updated_at = datetime.datetime()
