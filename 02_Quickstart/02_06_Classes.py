"""This file contains info & examples
on classes in Python"""

"""normal class"""
class Dog: #creates the class
    def __init__(self,name: str ,legs: int, breed: str):
        """'initialises' the class, must input name, legs & breed when creating"""
        self.name = name
        self.legs = legs
        self.breed = breed
    def __add__(self, other):
        print(f'{self.name} & {other.name} don\'t seem to '
              f'like each other!')
#some methods (funcs for the class)
    def speak(self):
        """Makes the dog bark"""
        print(self.name + ' says: Bark!')
    def legnum(self):
        """Tells us how many legs the dog has"""
        print(f'{self.name} has {self.legs} legs.')
    def breedof(self):
        """Tells us the breed of the dog"""
        print(f'{self.name} is a {self.breed}.')

h = Dog('Bob', 4, 'Poodle')
g = Dog('Jim', 3, 'Labrador')

h.speak()
g.speak()
g.legnum()
h.breedof()
g + h