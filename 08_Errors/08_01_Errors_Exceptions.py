"""
Contains info on errors & exceptions
"""

"""Try/Except"""

#/ Here, instead of stopping the code, the except func caught
#  the exception and executed the code indented
try:
    print(1/0)
except Exception as theerror:
    print(type(theerror))

#/ here there is no Exception object so the code in try is
#  executed
try:
    print(1/1)
except Exception as theerror:
    print(type(theerror))