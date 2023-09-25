#!/usr/bin/python3
"""
Defines a FileStorage class Module(JSON).
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path (str): The path to the JSON file to save objects.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if cls in self.all_classes:
                cls = self.all_classes[cls]
            cls_dict = {}
            for key, value in FileStorage.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' Deletes obj from __objects if it is inside '''
        if obj is not None:
            del self.__objects[f'{type(obj).__name__}.{obj.id}']
