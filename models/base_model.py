#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models

    Attr:
    id (sqlalchemy string): basemodel id
    created_at (sqlalchemy datetime): datetime at creation
    updated_at (sqlalchemy datetime): datetime during update
    """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        '''if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or 'updated_at':
                    v = datetime.strptime(v, time_fmt)
                if k != "__class__":
                    setattr(self, k, v)'''
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if key == 'created_at' and isinstance(value, str):
                self.created_at = datetime.strptime(value,
                                                    '%Y-%m-%d %H:%M:%S.%f')
            if key == 'updated_at' and isinstance(value, str):
                self.updated_at = datetime.strptime(value,
                                                    '%Y-%m-%d %H:%M:%S.%f')

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            new_dict.pop('_sa_instance_state', None)
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if 'password' in new_dict:
            new_dict['password'] = new_dict['password']
            new_dict.pop('_password', None)
        if 'amenities' in new_dict:
            new_dict.pop('amenities', None)
        if 'reviews' in new_dict:
            new_dict.pop('reviews', None)
        new_dict["__class__"] = self.__class__.__name__
        if not save_to_disk:
            new_dict.pop('password', None)
        return new_dict

    def delete(self):
        ''' Delete current instance from storage by calling its delete
        method
        '''
        models.storage.delete(self)
