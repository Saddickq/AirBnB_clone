#!/usr/bin/python3
"""Module that handles storage and retreival of dict
from a json file"""
import json
from os.path import isfile


class FileStorage():
    """base class of current module"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that retrieves all instances of the dict
        stored wihin the json file"""
        return self.__objects

    def new(self, obj):
        """method that creates a new instance of a class"""
        """"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Method that serializes and writes python
        object/instance to a JSON file"""

        py_string = {key: value.to_dict() for key, value in
                     self.__objects.items()}
        object_info = json.dumps(py_string)

        """write to JSON file"""
        with open(self.__file_path, 'w') as json_file:
            json_file.write(object_info)

    def reload(self):
        """method that loads object's json string from a JSON file
        (deserialization) and displays to user as a python object(dict)"""
        objects = {}

        if (isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                objects = json.loads(file.read())
            from models.base_model import BaseModel
            from models.user import User
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
