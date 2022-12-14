#!/usr/bin/python3
""" BaseClass of all the models """
import uuid
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """ Defines the common attributes and methods for other classes """
    def __init__(self, *args, **kwargs):
        """ init constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    date = value[0:10] + " " + value[11:]
                    self.created_at = datetime.strptime(
                        date, '%Y-%m-%d %H:%M:%S.%f')
                elif key == "updated_at":
                    date = value[0:10] + " " + value[11:]
                    self.updated_at = datetime.strptime(
                        date, "%Y-%m-%d %H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """ String representation for an object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
        __dict__ of the instance """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
