#!/usr/bin/python3
"""module containing new instance User"""
from models.base_model import BaseModel


class User(BaseModel):
    """derived class of the base class BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
