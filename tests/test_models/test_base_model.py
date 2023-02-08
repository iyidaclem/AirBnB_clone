#!/usr/bin/env python3
"""Base model test module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import re

class TestBaseModel(unittest.TestCase):
    """ Class for testing fuctions in BaseModel class"""

    def test_base_model_instance(self):
        """ Checks if the model is instance of BaseModel"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_model_id(self):
        """ Checks if the instance have public attribute id
            of length 36 
        """
        new_model = BaseModel()
        self.assertEqual(36, len(new_model.id))
    
    def test_model_created_at(self):
        """Check if model has attribute created_at which is 
            instance of datetime
        """
        new_model = BaseModel()
        self.assertIsInstance(new_model.created_at, datetime)

    def test_model_updated_at(self):
        """Check if model has attribute updated_at which is 
            instance of datetime
        """
        new_model = BaseModel()
        self.assertIsInstance(new_model.updated_at, datetime)
        
    def test__str__method(self):
        """ Check if new_model.__str__ prints correct string"""
        new_model = BaseModel()
        matched = re.match("^\[BaseModel\]\s\(.{36}\)\s\{.+\}", new_model.__str__())
        matched = bool(matched)
        self.assertEqual(True, matched)

if __name__ == "__main__":
    unittest.main()
