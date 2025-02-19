"""
Contains info on how functions act as variables
"""

def cod():
    return 5

print(cod.__code__.co_varnames) # this returns all arguments in a func
print(cod.__code__.co_code) # this returns a byte object with the instructions in the func

print('--------------')

#/ As we know that funcs are just variables w/ data
#  we can use them in iterables and put them in lists
#  and other stuff we usually do w/ variables
text = "Hello, my name is Nathan and I study at Bath."

def lowercase(string):
    return string.lower()
def removepunc(string):
    puncmarks = [',', '.']
    for punctuation in puncmarks:
        string.replace(punctuation, '')
    return string
def noshortwords(string):
    return ' '.join([word for word in string.split() if len (word) > 3])

processfuncs = [lowercase, removepunc, noshortwords]

print(text) #before we applied all the funcs in the list

for func in processfuncs:
    text = func(text)

print(text) #after

print('--------------')

"""Lambda Functions"""
#/ As we do not have to define a variable to do coding:
print(2+3)
a=2+3
print(a)
#/ we may not need to define a function

print('--------------')

#/ we can do this with lambda functions
#  there is a phantom return after the :
#  (lambda x : func(x))(what we want x to be)
print((lambda x: x+3)(5))

print('--------------')

mylist = [5,8,2,1,4]
print(sorted(mylist))

mylist = [{'num':5}, {'num': 3}, {'num': 1}]
print( sorted(mylist, key= lambda x: x['num']) )
#/ this shows a quick mini-func we needed, instead
#  of using many lines for this 1 use, we can use lambda