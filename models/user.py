#!/usr/bin/python3
"""
A module for the user
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    A class for the user inherited from the parent class BaseModel
    """

    email = ""  # Email of user
    password = ""  # Password of user
    first_name = ""  # First name of user
    last_name = ""  # Last name of user
