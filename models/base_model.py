#!/usr/bin/python3
"""This is  base Module that handle creation of new instatnces among others"""


from uuid import uuid4
from datetime import datetime
import json

class BaseModel():

    current_date = datetime.now()

    def __init__(self, *args, **kwargs):
        """function that initialises a new instance"""
        if kwargs:
            """if using kwargs skip __class__ and revert  updated_at
            and created__at to a datetime object"""
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f"))

                elif key != "__class__":
                    setattr(self, key, value)
                    """if using kwargs set attribute to (key)'s value to 
                    class instance(self or Basemodel) """

        else:
            """if not if not using kwargs(!kwargs go by the normal
            instatiation/creation of a new instance)"""
            self.id = str(uuid4())
            self.created_at = BaseModel.current_date
            self.updated_at = BaseModel.current_date

    def save(self):
        """saving the current date(stored in a pubic instance variable) 
        after every update"""
        new_time  = BaseModel.current_date
        self.updated_at = new_time
        
    def to_dict(self):
        """dictionary representation of any new object instance"""
        dict = {}
        dict["__class__"] = self.__class__.__name__
        dict["updated_at"] = self.updated_at.isoformat()
        dict["created_at"] = self.created_at.isoformat()

        for key, value in  self.__dict__.items():
            
            if key in ["created_at", "updated_at"]:
                dict[key] = str(value)
            else:
                dict[key] = value

        return dict


    def __str__(self):
        """string representation of any new instance created"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)



my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
