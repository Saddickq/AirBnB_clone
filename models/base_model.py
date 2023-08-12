#!/usr/bin/python3
"""base Module that handles creation of new instatnces among others"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():

    current_date = datetime.now()

    def __init__(self, *args, **kwargs):
        """function that initialises a new instance
        Params
        args : tuple
            non-keyworded variable number of arguments.
        kwargs : dicitonary
            key-value pair dicitonary
        """

        if kwargs:
            """if using kwargs skip __class__ and revert  updated_at
            and created__at to a datetime object"""
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f"))

                elif key != "__class__":
                    setattr(self, key, value)
                    """if using kwargs set attribute to (key)'s value to
                    class instance(self or Basemodel)"""

        else:
            """if not using kwargs(!kwargs go by the normal
            instatiation/creation of a new instance)"""
            self.id = str(uuid4())
            self.created_at = BaseModel.current_date
            self.updated_at = BaseModel.current_date
            storage.new(self)

    def save(self):
        """saving the current date(stored in a pubic instance variable)
        after every update"""
        new_time = BaseModel.current_date
        self.updated_at = new_time
        storage.save()

    def to_dict(self):
        """dictionary representation of any new object instance"""
        dict = {}
        dict["__class__"] = self.__class__.__name__
        dict["updated_at"] = self.updated_at.isoformat()
        dict["created_at"] = self.created_at.isoformat()

        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dict[key] = str(value)
            else:
                dict[key] = value

        return dict

    def __str__(self):
        """string representation of any new instance created"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
