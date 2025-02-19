"""
Contains info on how to handle exceptions
(ry/except, finally, decorators etc.)
"""

"""try/except"""

#/ we can use try/except in functions to catch errors
#  and know their type
def causeError():
    try:
        return 1/0
    except Exception as e:
        return e

print(causeError())
print(type(causeError()))

print('-------------')

#/ we can also not take the exception as an argument
#  and just print a message
def causeError():
    try:
        return 1/0
    except Exception:
        print('There was an error!')

causeError()

print('-------------')

"""Finally"""

# finally causes the indented code to run exception or not
def causeError():
    try:
        return 1/0
    except Exception:
        print('There was an error!')
    finally:
        print('This always executes')
causeError()
print('')

# even if there is an error and no except block
def causeError():
    try:
        return 1/1
    finally:
        print('This always executes')
causeError()
print('')

import time

#can be used for cleanup or to time the code
def causeError():
    start= time.time()
    try:
        time.sleep(0.1)
        return 1/0
    except Exception:
        print('There was an error!')
    finally:
        print(f'Function took {time.time() - start} seconds')
causeError()

print('-------------')

"""Catching Exceptions by type"""

# we can also except subclasses of Exception and chain them
def causeError():
    try:
        return 1/'0'
    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a divide by zero error!')
    except Exception:
        print('There was an error!')
causeError()

# order matters, as python will go down the list and only
# except the first found
def causeError():
    try:
        return 1/'0'
    except Exception:
        print('There was an error!')
    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a divide by zero error!')
causeError()
# because of this, always put the more specific errors first
# and the more catch-all last

print('-------------')

"""Custom Decorators"""

def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a divide by zero error!')
        except Exception:
            print('There was an error!')
    return wrapper
# passes the func through the try/except lines and returns
# either the except or the og function return

# the handle is part of the definition, and takes the func as
# an argument
@handleException
def causeError():
    return 1/'0'

causeError()
# even though try/except isnt in the causeError def,
# they are in the handles definition so get passed anyway

print('-------------')

"""Raising exceptions"""

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a divide by zero error!')
        except Exception:
            print('There was an error!')
    return wrapper

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)
# the og handleException only takes funcs with no args
# so we had to add *args to raiseException func

raiseError(0)
raiseError(8)