"""
Contains info on list comprehensions.
List comprehensions generate lists from iterable structures
[iteration] for list comprehension
"""

mylist = [1,2,3,4,5]

"""
[func(blank) for blank in group is a comprehension]
preforms func on all values and returns list that has been
iterised
"""
print([2*item for item in mylist])

print('--------------------------------')

#/ can add if statements to filter with list comprehensions
mylist = list(range(100))

filteredlist = [item for item in mylist if item % 10 ==0]
print(filteredlist) # list of all items divisible by 10 (no rem)
filteredlist = [item for item in mylist if item % 10 <3]
print(filteredlist) # list of all items with rem 0,1 or 2 after /10

print('--------------------------------')

"""Comprehensions using functions & strings"""

mystring = 'My name is Nathan Tonge. I live in Bath'
print(mystring.split('.')) # splits the string at '.' character
print(mystring.split())    # splits the string at ' ' (spaces), giving list of words

print('--------------------------------')

def cleanwords(word):
    # replaces '.'s with '' (removes all '.'s from words
    return word.replace('.', '').lower() #chaining func, removes '.'s and lowercases words

print([cleanwords(word) for word in mystring.split()])
print([cleanwords(word) for word in mystring.split() if len(cleanwords(word)) < 3])

print('--------------------------------')

#/ Nested list comprehension, using multiple comprehensions in one [[Comprehension]comprehension]

print([[cleanwords(word) for word in sentence.split()] for sentence in mystring.split('.')])
#creates word list for each sentence
#creates list of 2 lists (1 for each sentence)

print([[cleanwords(word) for word in sentence.split()]\
      for sentence in mystring.split('.')][0])
#selects 1st element in list of lists