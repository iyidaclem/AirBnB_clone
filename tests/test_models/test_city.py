#!/usr/bin/python3
""" test suite for city model"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Module for testing City model"""

    def setUp(self):
        """set up the new City instance"""
        self.new_city = City()

    def test_new_city_instance(self):
        """Check if the super class of the new city
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_city, BaseModel)

    def test_new_city_attributes(self):
        """ Test if the new_city instance has
            the attributes name
        """
        self.assertEqual(True, hasattr(self.new_city, "name"))
        self.assertEqual(True, hasattr(self.new_city, "state_id"))


if __name__ == "__main__":
    unittest.main()
