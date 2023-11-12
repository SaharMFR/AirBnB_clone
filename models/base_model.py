#!/usr/bin/python3
"""Defines the base model"""


import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isformat()
        my_dict["updated_at"] = self.updated_at.isfromat()
        return my_dict
