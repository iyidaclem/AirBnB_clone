#!/usr/bin/python3
"""
Module for the review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class """

    place_id = ""  # it will be the Place.id
    user_id = ""  # It will be the User.id
    text = ""  # empty string
