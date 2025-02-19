"""
Contains info on dictionary comprehensions.
Dictionary comprehensions generate dict.s from iterable structures
{iteration} for dictionary comprehension
"""

animalList = [('a', 'aardvark'), ('b', 'bear'),
              ('c', 'cat'), ('d', 'dog')] #creates list of (key,value) tuples

animals = {item[0] : item[1] for item in animalList}
#makes dict. animals by 1st in tuple: 2nd in tuple for all tuples in animalList
#can also be created like this:
animals2 = {key: value for key,value in animalList}

print(animals)
print(animals2)

print('----------------------------')

"""Converting back into list"""

#/ the .items() for dict.s returns list of (key,value) tuples
print(animals.items())
animalList2 = list(animals.items()) #this makes a list like the one we started with
print(animalList == animalList2)    #shows that the 2 lists are identical

print('----------------------------')

#/ Comprehensions can be used for lots of other stuff,
# like a list of dictionaries
finalList = [{'letter': key, 'name': value} for key,value in animalList2]
print(finalList)