#!/usr/bin/python3
"""Defines unit tests for the Review class"""
from unittest import TestCase
from datetime import datetime
from models.review import Review


class TestReview(TestCase):
    """Test class with methods testing the Review class"""

    def test_init(self):
        """ Test review object creation """
        created_at = datetime.now()
        obj = Review()
        self.assertEqual(obj.created_at.date(), created_at.date())

    def test_str(self):
        """ Test the __str__ method """
        created_at = datetime.now()
        updated_at = datetime.now()
        obj = Review()
        actual = str(obj)
        self.assertIs(type(actual), str)
        self.assertEqual(obj.created_at.date(), created_at.date())
        self.assertEqual(obj.updated_at.date(), updated_at.date())

    def test_save(self):
        """ Test the save method """
        my_models = Review()
        updated_at = datetime.now()

        self.assertEqual(my_models.updated_at.date(), updated_at.date())
        my_models.save()
        updated_at = datetime.now()

        self.assertEqual(my_models.updated_at.date(), updated_at.date())

    def test_to_dict(self):
        """ Test the to_dict method """
        expected = ("id", "created_at", "updated_at", "__class__")
        my_models = Review()
        actual = my_models.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))
