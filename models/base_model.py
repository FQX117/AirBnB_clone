#!/usr/bin/python3
"""
Module contains the Superclass: BaseModel
"""
from datetime import datetime 
import uuid
time = "%Y-%m-%dT%H:%M:%S.%f"

# Console is working as the shell
# Basemodel is what the object is
# file sotrage 

class BaseModel:
    """
    this class defines all common attributes/methods for other classes
    """
    def __init__(self, *arg, **kwargs):
        """
        Init to create/initialize the object
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at




    def __str__(self):
        """
        string for printing 
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        Returns a dictionary containing all key/values of the instance
        """
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                v = datetime.isoformat(v)
            print(new_dict)
            print(k)
            print(v)
            new_dict[k] = v
            
        return new_dict
