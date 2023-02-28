#!/usr/bin/python3
"""Class BaseModel that defines all common attrs/methods for other classes"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance"""
        if kwargs:
            dformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, dformat)
            self.updated_at = datetime.strptime(self.updated_at, dformat)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Str representation of an instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attr updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
