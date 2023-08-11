#!/usr/bin/python3
import json
import os.path


class FileStorage():
    __filepath = "filepath"
    __objects = {}

    def all(self):
        return self.__objects.__dict__

    def new(self, obj):
        """"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Method that serializes and writes the object's attributes to a JSON file"""

        py_string = {key : value.to_dict() for key, value in self.__objects.items()}
        object_info = json.dumps(py_string)

        """write to JSON file"""
        with open(self.__filepath, 'w') as json_file:
            json_file.write(object_info)

    def reload(self):
        """Function that loads object's attributes from a JSON file (deserialization process)"""
        if os.path.exists(self.__filepath):

            with open(self.__filepath, 'r') as json_file:
                object_info = json.load(json_file)

            return object_info
