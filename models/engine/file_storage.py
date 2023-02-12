#!/usr/bin/env python3
"""
File storage class
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    File storage
    """

    __file_path = "file.json"  # file path
    __objects = {}  # empty at creation

    def all(self):
        """
        public method to return __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to __objects
        """
        _key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[_key] = obj

    def save(self):
        """
        Serializes __objects to JSON file `file.json`
        """
        _obj = FileStorage.__objects
        _obj2 = {obj: _obj[obj].to_dict() for obj in _obj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(_obj2, f)

    def reload(self):
        """
        Deserializes JSON file to __objects;
        only if the file exists
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
