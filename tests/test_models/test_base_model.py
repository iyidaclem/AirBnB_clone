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
        self.my_json = self.new_model.to_dict()
        self.new_model_2 = BaseModel(**self.my_json)

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
        matched = re.match("^\[BaseModel\]\s\(.{36}\)\s\{.+\}", self.new_model.__str__())  # noqa: E402
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
        self_dict = self.new_model.__dict__.copy()
        arr1 = [i for i in self_dict]
        self_dict_2 = self.new_model.to_dict()
        arr2 = [j for j in self_dict_2]
        arr1.append("__class__")
        arr1.sort()
        arr2.sort()
        self.assertEqual(arr1, arr2)

    def test_iso_format(self):
        """
            Also checks if updated_at and created_at
        """
        _dict = self.new_model.to_dict()
        match = re.match(
                "^[0-9]{4}[-][0-9]{2}[-][0-9]"
                "{2}[T][0-9]{2}[:][0-9]{2}[:]"
                "[0-9]+",
                str(_dict["created_at"])
                )
        match = bool(match)
        match2 = re.match(
            "^[0-9]{4}[-][0-9]{2}[-][0-9]{2}"
            "[T][0-9]{2}[:][0-9]{2}[:][0-9]+",
            str(_dict["updated_at"])
            )
        match2 = bool(match2)
        self.assertEqual(True, match)
        self.assertEqual(True, match2)

    def test_no__class(self):
        """
            Check that "__class__" is not in the new object attributes
        """
        self.assertNotIn("__class__", self.new_model_2.__dict__)

    def test_has_all_keys(self):
        """
            Check of the new instance has dictionary
            keys and values as attributes
        """
        _my_json_keys = [i for i in self.my_json]
        _json_keys_2 = [j for j in self.new_model_2.__dict__]
        _json_keys_2.append("__class__")
        _my_json_keys.sort()
        _json_keys_2.sort()
        self.assertEqual(_my_json_keys, _json_keys_2)

    def test_created_at_and_updated_at(self):
        """
            Check if created_at and updated_at are
            datetime.datetime object
        """
        self.assertIsInstance(self.new_model_2.created_at, datetime)
        self.assertIsInstance(self.new_model_2.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
