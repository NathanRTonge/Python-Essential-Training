"""
Contains info on general functions
"""

def preformOperation(num1, num2, operation):
    if operation == 'sum' or operation == 'add':
        return num1 + num2
    if operation == 'multiply' or operation == 'times':
        return num1 * num2
print(preformOperation(2, 4, 'add'))

print('------------------------')

"""Named Parameters"""

#/ named parameters can be used to assign value to parameters
#  each time it is called or set a default value if that parameter
#  is not added
def preformOperation(num1, num2, operation='sum'):
    if operation in ['sum', 'add']:
        return num1 + num2
    if operation in ['multiply', 'times']:
        return num1 * num2

print(preformOperation(2, 4))
#operation not added, defaulted to 'sum'
print(preformOperation(2, 4, 'times'))
print(preformOperation(2, 4, operation= 'times'))
#operation added, overrides named parameter

print('------------------------')

#/ keyword, positional argument position matters
#  all positional arguments must come before keyword
def preformOperation(num1, num2, operation='sum', message='Default Message'):
    print(message)
    if operation in ['sum', 'add']:
        return num1 + num2
    if operation in ['multiply', 'times']:
        return num1 * num2

print(preformOperation(2, 4))
print(preformOperation(2, 4, #all positional before keyword
                       message= 'New message', operation='times'))
print(preformOperation(2, 4, 'times', #all positional before keyword
                       message= 'New message'))

print('------------------------')

"""*args & **kwargs"""

#/ *args only covers positional arguments, not keyword
def preformOp(*args):
    print(args)
preformOp('b',6,2j,b'w')

#/ **kwargs covers kw arguments but not positional
#  returns dictionary of keyword:value
def preformOp(**kwargs):
    print(kwargs)
preformOp(name = 'benjamin', height = 1.82)

print('------------------------')

#/ These are very useful if we want a varying number
#  of inputs for a functon e.g:
import math

def preformOp(*args, operation='sum'):
    if operation in ['sum', 'add']:
        return sum(args) #will sum all the args
    if operation in ['multiply', 'times']:
        return math.prod(args) #will times all the args
print(preformOp(1,4,6,7))
print(preformOp(1,6,2, operation='times'))