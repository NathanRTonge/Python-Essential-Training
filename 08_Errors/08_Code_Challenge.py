"""
Code challenge to make custom exception and raise it
if non integers are passed in
"""

class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for a in args:
            if type(a) != int:
                raise NonIntArgumentException('Non Integers Passed In')
            else:
                continue
        return func(*args)
    return wrapper

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

print(sum(2,3,5))
print(sum('d', 4, 6))