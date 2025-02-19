"""
Contains info on If & Else statements
"""

"""Elif"""
#/ we can use elif statements instead of nested if else statements
for n in range(1,101): # this loop prints out all nums from 1-100
    if  n % 15 == 0:
        print('FizzBuzz') #Prints fizzbuzz if /3 & /5
    elif n % 3 == 0:
        print('Fizz') #prints out fizz if /3
    elif n % 5 == 0:
        print('Buzz') #prints out buzz if /5
    else:
        print(n)

print('-------------------------')

"""Single-line Else If"""
print(*('FizzBuzz' if n%15 ==0 else 'Fizz' if n%3==0 \
       else 'Buzz' if n%5==0 else n for n in range(1,101)))

#// NOTE
#/ For generators, you must print(*(generator))
#  or else will return <generator object>