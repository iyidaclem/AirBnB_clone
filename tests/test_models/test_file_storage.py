#!/usr/bin/python3
"""
Test file for file_storage
"""


import unittest
import models
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Class handles all edge cases for testing file_storage
    """

    def setUp(self):
        """ code to apply to all tests """
        new_model = BaseModel()

    def test_all_method(self):
        """ Test that all() returns dictionary _`_objects` """

        all_return = models.storage.all()
        self.assertIsInstance(all_return, dict)

