"""
Making a function to return list of primes
up to given number
"""

def allPrimesUpTo(num):
    primesFound = [2]
    for i in range (2,num):
        for prime in primesFound:
            if i % prime == 0:
                break
            if prime > i**0.5:
                primesFound.append(i)
                break
    return primesFound

list1 = allPrimesUpTo(100)
list2 = allPrimesUpTo(1000)
print(list1)
print(list2)