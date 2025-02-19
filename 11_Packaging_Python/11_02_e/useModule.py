"""
Shows how to import and use modules
"""
# You can import the entire module, so you will have to call
#each func as a method
import primes
print(primes.isPrime(5))
print('------------')

# You can use 'as' to shorten the module name and make calling
#it easier
import primes as p
print(p.isPrime(6))
print('------------')

 #You can import specific functions to call them normally
from primes import listPrimes, isPrime
print(listPrimes(100))
print(isPrime(7))

#when import primes is called, all code in the module is
#executed, so the print __name__ is carried out