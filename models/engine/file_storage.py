#!/usr/bin/python3
"""Defines FileStorage class"""

import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instanes.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictoinary `__objects`"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in `__objects` the `obj` with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file"""

        my_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to `__objects`"""

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            dict_obj = json.load(f)
            dict_obj = {k: self.classes()[v["__class__"]](**v)
                        for k, v in dict_obj.items()}
            FileStorage.__objects = dict_obj
