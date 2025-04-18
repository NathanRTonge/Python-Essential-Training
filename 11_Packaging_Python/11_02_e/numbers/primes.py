from factors import getFactors

def isPrime(n):
    return len(getFactors(n)) == 2

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n):
            foundPrimes.append(n)
    return foundPrimes
    
