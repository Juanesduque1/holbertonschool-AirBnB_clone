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
        key = self.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "w") as file:
                file.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to __objects' dictionary'"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
