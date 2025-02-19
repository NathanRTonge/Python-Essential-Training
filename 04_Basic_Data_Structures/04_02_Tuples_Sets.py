"""
contains info on tuples & sets
"""

"""Sets"""

#/sets are a collection of all unique values in a group
#/the order does not matter (no index)
myset = {'a', 'a', 'b', 'c'}
print(myset)
myset2 = set(['t', 'f', 'r', 'r', 'r'])
print(myset2)
print('------------------------')

#/to remove duplicates from list, list->set->list
#/This will randomise the order
listexample = [5, 'b', '7', 'b', 20]
print(listexample)
fixedlistexample = list(set(listexample))
print(fixedlistexample)
print('------------------------')

#/.add(value) adds value to set'''
print(myset)
myset.add('d')
print(myset)
print('------------------------')

#/.pop() can be used only with no index parameter
#/will remove and return random element in set
while myset:
    print(myset.pop())
print('------------------------')

#/Bool logic on set values
myset = {'h', 'g', 'r', 't'}
print('h' in myset)
print('z' in myset)
print('------------------------')

#/.discard(value) will remove specific value in set
print(myset)
myset.discard('g')
print(myset)

print('------------------------')
print('------------------------')

"""Tuples"""

#/ tuples are like lists (indexed) but immutable
#/ tuples save space as they do not preemptively block off space
#/ like lists do in preparation of appendages
mytuple = ('a', 'b', 'c')
print(mytuple)
print('------------------------')

#/Unpacking values
def whateverfunc():
    return 1,2,3 #funcs that return many values return a tuple
print(type(whateverfunc()))

#/ if a func returns multiple values, multiple variables
#/ can be assigned to it like this
a,b,c = whateverfunc()
print(a)
print(b)
print(c)