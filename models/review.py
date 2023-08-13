#!/usr/bin/python3
"""module for object reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """derived class of the base class BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
