#!/usr/bin/python3
"""Class creation to define attrs/methods of the console"""
from os import path
import json


class FileStorage:
    """Class FileStorage to define attrs/methods"""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionaty '__objects'"""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the object with the key """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        """Deserializes the JSON file to __objects' dictionary'"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State

        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)
