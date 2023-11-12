#!/usr/bin/python3
"""Defines the base model"""


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the new object from BaseModel"""
        if len(kwargs) != 0:
            for k in kwargs:
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(
                            kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """Returns string representation of the object"""

        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`"""

        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns dictionary contains all keys and values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
