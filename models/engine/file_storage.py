#!/usr/bin/env python3
"""
File storage class
"""


import json


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
        try:
            with open(FileStorage.__file_path, "w") as my_file:
                serialize = json.dump(FileStorage.__objects, my_file)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Deserializes JSON file to __objects;
        only if the file exists
        """
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                FileStorage.__objects = json.load(my_file)
        except FileNotFoundError:
            pass


