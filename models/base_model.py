#!/usr/bin/python3
"""Defines the BaseModel."""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the project."""
    def __int__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, timeform))
                else:
                    setattr(self, key, value)
        models.storage.new(self)


    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value
        """
        ins_dict = self.__dict__.copy()
        ins_dict["__class__"] = self.__class__.__name__
        ins_dict["created_at"] = self.created_at.isoformat()
        ins_dict["updated_at"] = self.updated_at.isoformat()
        return ins_dict
    def __str__(self):
        """Return the print/str representation of the BaseModel."""
        class_name = self.__class__.__name__
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))
if __name__ == "__main__":
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
