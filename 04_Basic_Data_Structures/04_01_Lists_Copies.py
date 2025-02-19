"""
Contains useful list info (+copies)
"""

mylist = [1,2,3,4,5,6,7,8,9,10]

"""
list[start:end:step]
start is inclusive
end is exclusive
"""
print(mylist[3::2]) #start from 4th element, to end in steps of 2
print(mylist[2:4:]) #start from element up to 4th (exclusive)
print(mylist[::])   #all values
print('------------------------------')

print(mylist[::-2])   #counts backwards from end of list
print(mylist[7:3:-1]) #counts back from 7th element to 4th (exclusive)
print('------------------------------')

list2= list(range(51))  #makes a list from 0-50 (range is exclusive)
print(list2[::-5])      #prints from 50 to 0 in multiples of 5
print('------------------------------')

"""
Modifying lists
"""
otherlist = [0,1,2,3]
print(otherlist)
print('------------------------------')
print('------------------------------')

#/.append() adds element to end of list
otherlist.append(20)
print(otherlist)
#/.insert() inserts new value (at index 3 (4th element))
otherlist.insert(3,'new value')
print(otherlist)
print('------------------------------')

#/.remove removes a value from the list
otherlist.remove('new value')
print(otherlist)
#/.pop removes item from end of list and returns it
print(otherlist.pop())
print(otherlist)
print('------------------------------')

while otherlist: #empty list returns false
    print(otherlist.pop()) # pop(index) will remove & return the value at index
print(otherlist)
print('------------------------------')
print('------------------------------')

"""
Equating variables
"""
#/If set b=a, it will always equal the current value of a
#/even if b has not been altered
a = [1,2,3,4,5]
b=a
a.append(6)
print(b)
print(a)
print('------------------------------')

#/By setting b=a.copy(), b equals the value of a at the
#/time of the function
a = [1,2,3,4,5]
b=a.copy()
a.append(6)
print(b)
print(a)
