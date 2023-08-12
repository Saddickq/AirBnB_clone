import unittest
from models.base_model import BaseModel
from uuid import UUID
import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        person = BaseModel(name="Saddiq", my_number=30)
        self.assertEqual(person.name, "Saddiq")
        self.assertEqual(person.my_number, 30)

    def test_default_values(self):
        person = BaseModel(name="Ardiy", my_number=25)
        self.assertEqual(person.name, "Ardiy")
        self.assertEqual(person.my_number, 25)

    def test_my_number_is_integer(self):
        with self.assertRaises(ValueError):
            my_model = BaseModel(name="Bob", my_number="thirty")

    def test_id_is_uuid(self):
        my_model = BaseModel(name="Saddiq", my_number=28)
        self.assertIsInstance(my_model.id, UUID)

    def test_created_at_date(self):
        my_model = BaseModel(name="Michael", my_number=35)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
    
    def test_updated_at_date(self):
        my_model = BaseModel(name="Michael", my_number=35)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
    
    def test_uuid_is_string(self):
        my_model = BaseModel(name="Saddiq", age=30)
        self.assertIsInstance(str(my_model.id), str)


if __name__ == '__main__':
    unittest.main()
