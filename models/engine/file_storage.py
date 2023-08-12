#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Method that serializes and writes the object's attributes to a JSON file"""

        py_string = {key : value.to_dict() for key, value in self.__objects.items()}
        object_info = json.dumps(py_string)

        """write to JSON file"""
        with open(self.__file_path, 'w') as json_file:
            json_file.write(object_info)

    def reload(self):
        """Function that loads object's attributes from a JSON file (deserialization process)"""
        objects = {}

        if (isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                objects = json.loads(file.read())
            from models.base_model import BaseModel
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
