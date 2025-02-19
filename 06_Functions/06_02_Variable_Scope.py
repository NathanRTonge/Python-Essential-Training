"""
Contains info on global & local variables and scope
"""

#/ we can use *args & **kwargs to call func variables
def operate(*args, **kwargs):
    print(args)
    print(kwargs)
operate(1,2, opertation='sum')

print('--------------------')

""".locals()"""

#/ We can also use the .locals() func
def preformOperation(num1, num2, operation='sum'):
    print(locals())
preformOperation(1,2, operation='multiply')
#/ we return a dict. of ALL arguments put in, position or keyword
#  it is called locals() because it gives all variables WITHIN
#  a function

print('--------------------')

"""globals()"""

#/ globals() gives us access to all variables within a program
#  even the hidden or built in ones
print(globals())

print('--------------------')

"""Scope: global & local"""

message= 'some global data'
varA = 15
def function1(varA, varB):
    message = 'some local data'
    print(message) #python will check local scope for variables 1st
    print(varA)
    print(locals())
    print('')

def function2(varC, varB):
    print(message)
    print(varA) #if variables not in local scope, python checks global scope
    print(locals())
    print('')

function1(1,2)
function2(3,4)

print('--------------------')

"""Defining functions within functions"""

def func1(varA, varB):
    message = 'local data'
    print('before innerfunc defined', locals()) #returns all local variables
    def innerfunc(varA,varB):
        print(f'innerfunc local scope: {locals()}') #returns locals of current function

    print('after innerfunc defined', locals()) #returns all local variables (includes functions)
    innerfunc(123, 456)


func1(1,2)