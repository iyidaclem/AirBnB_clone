#!/usr/bin/python3
""" test suite for review model"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Module for testing review model"""

    def setUp(self):
        """set up the new review instance"""
        self.new_review = Review()

    def test_new_review_instance(self):
        """Check if the super class of the new review
        is an instance of a BaseModel
        """
        self.assertIsInstance(self.new_review, BaseModel)

    def test_new_review_attributes(self):
        """ Test if the new_review instance has
            the attributes place_id, user_id and text
        """
        self.assertEqual(True, hasattr(self.new_review, "place_id"))
        self.assertEqual(True, hasattr(self.new_review, "user_id"))
        self.assertEqual(True, hasattr(self.new_review, "text"))


if __name__ == "__main__":
    unittest.main()
