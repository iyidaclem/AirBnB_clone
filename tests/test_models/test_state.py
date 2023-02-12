#!/usr/bin/python3
""" test suite for state model"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Module for testing state model"""

    def setUp(self):
        """set up the new state instance"""
        self.new_state = State()

    def test_new_state_instance(self):
        """Check if the super class of the new state
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_state, BaseModel)

    def test_new_state_attributes(self):
        """ Test if the new_state instance has
            the attributes name
        """
        self.assertEqual(True, hasattr(self.new_state, "name"))


if __name__ == "__main__":
    unittest.main()
