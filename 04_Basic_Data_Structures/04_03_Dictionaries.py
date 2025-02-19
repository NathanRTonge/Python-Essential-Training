"""
Contains useful info on dictionaries
"""

#/ create a dictionary with {} and key:value pairs
animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat'}

#/ keys work as indexes do in lists
print(animals)
print(animals['a'])
#/ can add to a dictionary like a list
animals['d'] = 'dog'
print(animals)
#/ can change index's values like a list
animals['a'] = 'antelope'
print(animals)
print('--------------------')

#/ all keys can be gotten with .keys()
#/ all values can be gotten with .values()
print(animals.keys())
print(animals.values())
print('--------------------')
#/ creates dict_keys([]) object, immutable
#/ can make into lists with list()

#/ can look for keys in dict. with .get
print(animals.get('a'))
print(animals.get('e'))
#/ can add a default value to return if key not found
print(animals.get('e', 'No \'e\' animals found :('))
print('--------------------')

"""Dictionaries of Lists"""
animals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
    'c': ['cougar']}
print(animals)

#/ to add to list in dict.
animals['b'].append('bison')
print (animals)

#/ if we do not know if key/list is in dict.
if 'd' not in animals:
    animals['d'] = []
animals['d'] = 'deer'
print(animals)
print('--------------------')

"""The Default Dictionary"""

#/ default dict must be imported from collections
from collections import defaultdict

animals2 = defaultdict(list)
print(animals2) #we can see it is currently empty

#/ as animals2 is made from defaultdict(list),
#/ all values will be added to a list automatically
animals2['e'].append('elephant')
print(animals2)
animals2['e'].append('emu')
animals2['d'].append('duck')
print(animals2)
print(animals2['e']) #returns list value in key 'e'
print(animals2['f']) #returns an empty list as no values added