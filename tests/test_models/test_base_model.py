#!/usr/bin/python3
"""tests for base class"""
from unittest import TestCase
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from datetime import datetime
from os.path import isfile


class TestBaseModel(TestCase):
    """Test cases for the BaseModel class and console"""

    def test_instance_creation(self):
        """Tests instance creation and attribute assignment"""
        my_model = BaseModel(name="Saddiq", my_number=30)
        self.assertEqual(my_model.name, "Saddiq")
        self.assertEqual(my_model.my_number, 30)

    def test_string_attributes(self):
        """Test whether id, name and email attributes are a string"""
        my_model = BaseModel(name="Bob", email="ardiyq@gmail.com")
        self.assertIsInstance(my_model.name, str)
        self.assertIsInstance(my_model.email, str)

    def test_non_string_attributes(self):
        """Tests my_name attribute with integer value"""
        my_model = BaseModel(age=40)
        self.assertIsInstance(my_model.age, int)

    def test_id_is_uuid(self):
        """Test if id attribute is string rep"""
        my_model = BaseModel()
        self.assertIsInstance(str(my_model.id), str)
        self.assertEqual(len(my_model.id), 36)

    def test_whether_datetime_of_update_n_created_at(self):
        """Test created_at and updated at whether they are dto's"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_created_at_date(self):
        """Test updated_at attribute with datetime value"""
        my_model = BaseModel()
        created_at = datetime.now()
        self.assertEqual(my_model.created_at.date(), created_at.date())

    def test_save_updated_at(self):
        """Test whehter after saving updated_at its stil a dto"""
        my_model = BaseModel()
        updated_at = datetime.now()

        self.assertEqual(my_model.updated_at.date(), updated_at.date())
        my_model.save()
        updated_at = datetime.now()
        self.assertEqual(my_model.updated_at.date(), updated_at.date())

    def test_to_dict(self):
        """Test the to_dict method for BaseModel with keyword arguments"""
        my_model = BaseModel()
        self.assertEqual(my_model.to_dict()["__class__"], "BaseModel")
        self.assertIsInstance(my_model.id, str)
        self.assertEqual(len(my_model.id), 36)
        self.assertEqual(my_model.created_at.date(), datetime.now().date())
        self.assertEqual(my_model.updated_at.date(), datetime.now().date())

    def test_str_representation(self):
        """ Test the __str__ method """
        mm = BaseModel()
        id = mm.id
        di = mm.__dict__
        self.assertEqual(str(mm), "[{}] ({}) {}".format("BaseModel", id, di))

    def test_do_all_invalid_class(self):
        """Test 'all' command with invalid class argument"""
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.onecmd("all InvalidClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
