#!/usr/bin/python3
"""
Test file for file_storage
"""


import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Class handles all edge cases for testing file_storage
    """

    def setUp(self):
        """ code to apply to all tests """
        self.new_model = BaseModel()

    def test_all_method(self):
        """ Test that all() returns dictionary _`_objects` """

        all_return = models.storage.all()
        self.assertIsInstance(all_return, dict)

    def test_new_method(self):
        """ test that new methods adds new instance to __objects"""
        all_object = models.storage.all().copy()
        new_model_2 = BaseModel()
        models.storage.new(new_model_2)
        all_object_2 = models.storage.all()
        self.assertEqual(True, len(all_object.keys())
                         + 1 == len(all_object_2.keys()))

    def test_save_method(self):
        """ Test that save method save file to the path"""
        self.new_model.name = "Clement"
        self.new_model.save()
        all_obj = models.storage.all().copy()
        new_model_2 = BaseModel()
        models.storage.new(new_model_2)
        all_obj2 = models.storage.all().copy()
        self.assertNotEqual(len(all_obj.keys()), len(all_obj2.keys()))

        new_model_2.save()
        all_obj3 = models.storage.all().copy()

        self.assertEqual(len(all_obj3.keys()), len(all_obj2.keys()))


if __name__ == "__main__":
    unittest.main()
