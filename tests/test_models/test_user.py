#!/usr/bin/python3
""" test suite for user module"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Module for testing user model"""

    def setUp(self):
        """set up the new user instance"""
        self.new_user = User()

    def test_new_user_instance(self):
        """Check if the super class of the new user
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_user, BaseModel)

    def test_new_user_attributes(self):
        """ Test if the new_user instance has
            the attributes email, password, first_name and
            last_name
        """
        self.assertEqual(True, hasattr(self.new_user, "email"))
        self.assertEqual(True, hasattr(self.new_user, "password"))
        self.assertEqual(True, hasattr(self.new_user, "first_name"))
        self.assertEqual(True, hasattr(self.new_user, "last_name"))


if __name__ == "__main__":
    unittest.main()
