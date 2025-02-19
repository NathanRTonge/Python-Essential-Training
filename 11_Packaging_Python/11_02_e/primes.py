# This is a module that contains 2 functions, isPrime()
#and listPrimes()
def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)+1) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes
    
print(f'primes.py module name is {__name__}')
print('-----------------------')

#This will only run if the module is run directly and not called
if __name__ == '__main__':
    print('This is a module, please import using: \nimport primes')