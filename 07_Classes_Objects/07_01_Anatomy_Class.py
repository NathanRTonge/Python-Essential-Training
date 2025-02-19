"""
Contains general info on classes
"""

"""Instance Attributes"""

#/ instance attributes are attributes that each instance
#  of class Dog has, and are set individually to each dog
class Dog:
    def __init__(self,name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says "Bark!"')

mydog = Dog('Bob')
print(mydog.name)
print(mydog.legs)
#/ although legs is common amoung all dogs, we cant see it
#  directly because it is in the __init__ func

print('-------------')

"""Static Attributes"""

class Dog2:
    legs = 4 #now a static attribute and common to all Dog2s
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + ' says "Bark!"')

mydog2 = Dog('Bill')
print(mydog2.name)
print(mydog2.legs)
print(Dog2.legs) # legs value can be called directly from class
#/ these are often used to hold constants or fundamental
#  facts about a class

print('-------------')

#/ static attributes are a variable and so can be changed
#  outside of the class definition

Dog2.legs = 3
mydog3 = Dog2('Ben')

print(mydog3.name)
print(mydog3.legs)
print(Dog2.legs)
#/ To avoid anything like this happening accidentally,
#  these are often given _s and not accessed directly

print('-------------')

class Dog3:
    _legs = 4 #says not to reference directly and try not to change
    def __init__(self,name):
        self.name = name

    def getLegs(self): #example of 'getter func' to get static attribute
        return self._legs

    def speak(self):
        print(self.name + ' says "Bark!"')

finaldog = Dog3('Barb')
print(finaldog.name)
print(finaldog.getLegs())

#/ or as it is a static method:
class Dog3:
    _legs = 4
    def __init__(self,name):
        self.name = name

    def getLegs():
        return Dog3._legs

    def speak(self):
        print(self.name + ' says "Bark!"')

finaldog = Dog3('Barb')
print(finaldog.name)
print(Dog3.getLegs())
#/ however this is not advised as it can be a bit confusing
#  so doing it the normal/getter way is fine

print('-------------')

#/ the same laws of local and global scope apply, so
#  you can change variable of one instance w/out changing
#  class static attributes

finaldog._legs = 3
print(finaldog._legs) #gives variable for instance
print(Dog3._legs) #gives variable for class


