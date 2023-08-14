#!/usr/bin/python3
"""tests for the City class"""

from unittest import TestCase
from datetime import datetime
from models.city import City


class TestCity(TestCase):
    """Test class with methods testing the City class"""

    def test_init(self):
        """ Test city object creation """
        created_at = datetime.now()
        my_models = City()
        self.assertEqual(my_models.created_at.date(), created_at.date())

    def test_str(self):
        """ Test the __str__ method """
        created_at = datetime.now()
        updated_at = datetime.now()
        my_models = City()
        actual = str(my_models)
        self.assertIs(type(actual), str)
        self.assertEqual(my_models.created_at.date(), created_at.date())
        self.assertEqual(my_models.updated_at.date(), updated_at.date())

    def test_save(self):
        """ Test the save method """
        my_models = City()
        updated_at = datetime.now()

        self.assertEqual(my_models.updated_at.date(), updated_at.date())
        my_models.save()
        updated_at = datetime.now()

        self.assertEqual(my_models.updated_at.date(), updated_at.date())

    def test_to_dict(self):
        """ Test the to_dict method """
        expected = ("id", "created_at", "updated_at", "__class__")
        my_models = City()
        actual = my_models.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))
