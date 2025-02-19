"""
Contains info on inheritance for classes
"""

#/ classes can inherit features from a 'parent' class,
#  in this case Dog
class Dog:
    _legs = 4
    def __init__(self,name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says "Bark!"')

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: "Yap!"')
    #this overrides the func in parent class

    def wagtail(self):
        print('Their tail is wagging vigorously!')
    # can also define new funcs unique to child

#/ Childclass(Parentclass) to cause inheritance, meaning
#  Childclass now has all the methods and variables
#  of Parentclass

dog1 = Chihuahua('Bono')
dog1.speak()
print(dog1.getLegs())
dog1.wagtail()

dog2 = Dog('Bill')
dog2.speak()
print(dog2.getLegs())

print('----------------')

"""Extending built-in classes"""

#/ inheritance also works with built-in classes
myList = list() #this is a class

class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)
#/ the super() func calls the method from the Parent class

uniquelist = UniqueList()
uniquelist.append(1)
uniquelist.append(2)
uniquelist.append(3)
uniquelist.append(2)

print(uniquelist)

print('----------------')

class UniqueList(list):
    def __init__(self): # may overwrite important info, so
        super().__init__() # this ensures parent constructor called first
        self.someprop = 'Unique List!'

    def append(self, item):
        if item in self:
            return
        super().append(item)

uniquelist = UniqueList()
uniquelist.append(1)
uniquelist.append(2)
uniquelist.append(3)
uniquelist.append(2)

print(uniquelist)