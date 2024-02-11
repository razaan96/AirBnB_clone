#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.i"""



import os
import json
import models
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Set in __objects obj with key obj_class_name.id"""
        obj_classname = obj.__class__.__name__
        key = "{}.{}".format(obj_classname, obj.id)
        FileStorge.__objects[key] = obj

    def all(self):
         """Return the dictionary __objects."""
         return FileStorage.__objects
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        all_obj = FileStorage.__objects
        objdict = {}
        for obj in all_obj.keys():
            objdict[obj] = all_obj[obj].to__dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
