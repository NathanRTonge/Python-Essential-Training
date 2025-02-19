"""
Contains info on For loops
"""

#/ For loops can be used to iterate
myList = [1,2,3,4]
for item in myList:
    print(item)

print('-----------------------')

"""Pass"""

#/ Pass is very good for a placeholder that doesn't break
#  your code when run (for funcs and loops)
animalLookup = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog', 'duck'],
}

for letter, animals in animalLookup.items():
    pass # does nothing so code passes it by

print('-----------------------')

"""Continue"""


for letter, animals in animalLookup.items():
    if len(animals) > 1: #if false, statement is bypassed, no continue, sentence printed
        continue # if list of animals is longer than one, do next value on for loop
    print(f'Only 1 animal ({animals[0]}) for {letter}')

print('-----------------------')

"""Break"""

for letter, animals in animalLookup.items():
    if len(animals) > 1: # if > 1 animal,
        print(f'found {len(animals)} animals: {animals}')
        break # breaks from for loop, so d animals not listed

print('-----------------------')

"""For/Else Statement"""

#/ Finding primes (between 2-100)
for number in range(2,200):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break #if triggers, next number in for number loop
    else: # only triggers if break doesn't happen
        print(f'{number} is prime!')