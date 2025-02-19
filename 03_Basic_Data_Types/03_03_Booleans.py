"""
More info about booleans
"""

#Casting (between types) bools
print(bool(0))    #all ints, floats and complex with value 0
print(bool(0.0))  #will return False for bool
print(bool(0j))
print(bool(1))    #all other numbers will return True
print(bool(5j))
print(bool(27.4))
print('')

#String bools
print(bool('True'))    #all strings with characters (even
print(bool('False'))   #spaces) return true
print(bool('wtsrrgg'))
print(bool(' '))
print(bool(''))        #empty strings return False
print('')

#Other (data structures, none) bools
print(bool( [] ))          #all empty structures (list, tuple,
print(bool( () ))          #dictionaries) return False
print(bool([1,2]))        #If they have any data, return True
print(bool({'breed':'poodle'}))
print('')
print(bool(None))