#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel():

    current_date = datetime.now()

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = BaseModel.current_date
            self.updated_at = BaseModel.current_date
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        new_time  = BaseModel.current_date
        self.updated_at = new_time
        
    def to_dict(self):
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


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

