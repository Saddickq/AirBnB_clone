#!/usr/bin/python3
"""Defines unit tests for the File Storage class."""
from unittest import TestCase
from uuid import uuid4
from datetime import datetime, date
import pep8
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os.path import isfile


class TestFileStorage(TestCase):
    """Test class with methods testing the File Storage class"""
    def test_new(self):
        """ Test the new method """
        dict = {"id": "b29b5df5-72e7-43af-8b10-0db51b6d912f",
                "created_at": "2023-08-09 23:56:06.907067",
                "updated_at": "2023-08-09 23:56:06.907067",
                "__class__": "BaseModel"}

        key = "{}.{}".format(dict["__class__"], dict["id"])
        base_obj = BaseModel(**dict)
        my_models = FileStorage()
        if (not isfile("file.json")):
            objects = my_models.all()
            self.assertNotIn(key, list(objects.keys()))
        my_models.new(base_obj)
        objects = my_models.all()
        self.assertIn(key, list(objects.keys()))

    def test_object_info_json_format(self):
        """Verify if the serialized data is in valid JSON format"""
        my_models = FileStorage()
        my_models = BaseModel()
        object_info = json.dumps(my_models.to_dict())

        try:
            json.loads(object_info)
        except json.JSONDecodeError:
            self.fail("object_info is not in valid JSON format")

    def test_save(self):
        """ Test the save method """
        my_models = FileStorage()
        my_models.save()
        self.assertTrue(isfile("file.json"))

    def test_reload(self):
        """ Test the reload method """
        my_models = FileStorage()
        my_models.reload()
        objects = my_models.all()
        if (isfile("file.json")):
            objects = my_models.all()
            self.assertTrue(len(objects) > 0)
        else:
            with self.assertRaises(FileNotFoundError):
                with open("file.json", "r") as file:
                    pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")
