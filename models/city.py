#!/usr/bin/python3
"""module for object city"""
from models.base_model import BaseModel


class City(BaseModel):
    """derived class of the base class BaseModel"""

    state_id = ""
    name = ""
