#!/usr/bin/python3
"""heading for py file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Amenity
from models.amenity import Place
from models.review import Review


class FileStorage:
    """ new class for storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in the obj with the key"""
        nameof = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nameof, obj.id)] = obj

    def save(self):
        """serializes the object to the json file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w+") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to the object"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
