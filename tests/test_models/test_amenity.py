#!/usr/bin/python3
""" test suite for amenity model"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Module for testing amenity model"""

    def setUp(self):
        """set up the new amenity instance"""
        self.new_amenity = Amenity()

    def test_new_amenity_instance(self):
        """Check if the super class of the new amenity
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_new_amenity_attributes(self):
        """ Test if the new_amenity instance has
            the attributes name
        """
        self.assertEqual(True, hasattr(self.new_amenity, "name"))


if __name__ == "__main__":
    unittest.main()
