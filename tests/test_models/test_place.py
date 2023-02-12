#!/usr/bin/python3
""" test suite for place model"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Module for testing place model"""

    def setUp(self):
        """set up the new place instance"""
        self.new_place = Place()

    def test_new_place_instance(self):
        """Check if the super class of the new place
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_place, BaseModel)

    def test_new_place_attributes(self):
        """ Test if the new_place instance has
            all the attributes
        """
        self.assertEqual(True, hasattr(self.new_place, "city_id"))
        self.assertEqual(True, hasattr(self.new_place, "user_id"))
        self.assertEqual(True, hasattr(self.new_place, "name"))
        self.assertEqual(True, hasattr(self.new_place, "description"))
        self.assertEqual(True, hasattr(self.new_place, "number_rooms"))
        self.assertEqual(True, hasattr(self.new_place, "number_bathrooms"))
        self.assertEqual(True, hasattr(self.new_place, "max_guest"))
        self.assertEqual(True, hasattr(self.new_place, "price_by_night"))
        self.assertEqual(True, hasattr(self.new_place, "latitude"))
        self.assertEqual(True, hasattr(self.new_place, "longitude"))
        self.assertEqual(True, hasattr(self.new_place, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
