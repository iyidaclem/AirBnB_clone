#!/usr/bin/env python3
"""Base model test module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import re

class TestBaseModel(unittest.TestCase):
    """ Class for testing fuctions in BaseModel class"""

    def setUp(self):
        """Create new instance for each test case"""
        self.new_model = BaseModel()

    def test_base_model_instance(self):
        """ Checks if the model is instance of BaseModel"""
        self.assertIsInstance(self.new_model, BaseModel)

    def test_model_id(self):
        """ Checks if the instance have public attribute id
            of length 36 
        """
        self.assertEqual(36, len(self.new_model.id))
    
    def test_model_created_at(self):
        """Check if model has attribute created_at which is 
            instance of datetime
        """
        self.assertIsInstance(self.new_model.created_at, datetime)

    def test_model_updated_at(self):
        """Check if model has attribute updated_at which is 
            instance of datetime
        """
        self.assertIsInstance(self.new_model.updated_at, datetime)
        
    def test__str__method(self):
        """ Check if self.new_model.__str__ prints correct string"""
        matched = re.match("^\[BaseModel\]\s\(.{36}\)\s\{.+\}", self.new_model.__str__())
        matched = bool(matched)
        self.assertEqual(True, matched)

    def test_save_method(self):
        """Check if save method work correctly"""
        prev_updated_at = self.new_model.updated_at
        self.new_model.save()
        self.assertEqual(True, prev_updated_at < self.new_model.updated_at)

    def test_to_dict_method(self):
        """Check if to dict has all the neccesary keys
        """
        self_dict = self.new_model.__dict__
        arr1 = [i for i in self_dict]
        self.new_model.to_dict()
        self_dict_2 = self.new_model.__dict__
        arr2 = [j for j in self_dict_2]
        arr1.append("__class__")
        arr1.sort()
        arr2.sort()
        self.assertEqual(arr1, arr2)

    def test_iso_format(self):
        """
            Also checks if updated_at and created_at
        """
        self.new_model.to_dict() 
        match = re.match("^[0-9]{4}[-][0-9]{2}[-][0-9]{2}[T][0-9]{2}[:][0-9]{2}[:][0-9]+", str(self.new_model.created_at))
        match = bool(match)
        match2 = re.match("^[0-9]{4}[-][0-9]{2}[-][0-9]{2}[T][0-9]{2}[:][0-9]{2}[:][0-9]+", str(self.new_model.updated_at))
        match2 = bool(match2)
        self.assertEqual(True, match)
        self.assertEqual(True, match2)

if __name__ == "__main__":
    unittest.main()
