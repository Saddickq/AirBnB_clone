#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from uuid import uuid4
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class and console"""

    def test_instance_creation(self):
        """Tests instance creation and attribute assignment"""
        person = BaseModel(name="Saddiq", my_number=30)
        self.assertEqual(person.name, "Saddiq")
        self.assertEqual(person.my_number, 30)

    def test_my_number_is_integer(self):
        """Tests my_number attribute with non-integer value"""
        with self.assertRaises(ValueError):
            my_model = BaseModel(name="Bob", my_number="thirty")

    def test_id_is_uuid(self):
        """Test if id attribute is a UUID object"""
        my_model = BaseModel(name="Saddiq", my_number=28)
        self.assertIsInstance(my_model.id, uuid4)

    def test_created_at_date(self):
        """Test created_at attribute with datetime value"""
        my_model = BaseModel(name="Michael", my_number=35)
        self.assertIsInstance(my_model.created_at, datetime.datetime)

    def test_updated_at_date(self):
        """Test updated_at attribute with datetime value"""
        my_model = BaseModel(name="Michael", my_number=35)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)

    def test_uuid_is_string(self):
        """Test if id attribute is a string"""
        my_model = BaseModel(name="Saddiq", age=30)
        self.assertIsInstance(str(my_model.id), str)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        updated_at = datetime.now()

        self.assertEqual(obj.updated_at.date(), updated_at.date())
        obj.save()
        updated_at = datetime.now()

        self.assertEqual(obj.updated_at.date(), updated_at.date())

    def test_to_dict(self):
        """Test the to_dict method"""
        expected = ("id", "created_at", "updated_at", "__class__")
        obj = BaseModel()
        actual = obj.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))


if __name__ == '__main__':
    unittest.main()
