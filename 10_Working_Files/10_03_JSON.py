"""
Contains info on working with JSON files
"""
import json
from json import JSONDecodeError, JSONEncoder

"""Loading (inputting JSON)"""
jsonString = '{"a":"aardvark", "b":"bear", "c":"cat"}'
# This is a JSON string, not a dictionary

print(json.loads(jsonString))
# json.loads converts json -> python data
# JSON strings give python dictionaries

print('-------------')

jsonString = '{"a":"aardvark", "b":"bear", "c":"cat",}'
# if string has a trailing comma, get decode error

try:
    print(json.loads(jsonString))
except JSONDecodeError:
    print('Could not parse JSON!')

print('-------------')

"""Dumping (outputting JSON)"""

pythonDict = {'a':'aardvark', 'b':'bear', 'c':'cat',}
print(json.dumps(pythonDict))
# json.dumps converts python data -> JSON
# python dicts give json strings

print('-------------')

"""Custom JSON Decoders"""

class Animal:
    def __init__(self,name):
        self.name = name

# As JSON doesn't know how to encode this object, we need/can
# create our own encoder
class AnimalEncoder(JSONEncoder):
    def default(self, object):
        if type(object) == Animal:
            return object.name # returns name of animal
        return super().default(object)

pythonDict = {'a':Animal('aardvark'), 'b':Animal('bear'),
              'c':Animal('cat'),}
print(json.dumps(pythonDict, cls=AnimalEncoder))
# cls= is the class of encoder used
