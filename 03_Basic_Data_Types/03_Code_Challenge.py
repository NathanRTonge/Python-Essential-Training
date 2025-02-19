hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if type(hexNum) == str:
        for i in hexNum:
            if i in hexNumbers:
                continue
            else:
                return None
        y = 0
        b= len(hexNum)
        for i in hexNum:
            y += hexNumbers[i]*(16**(b-1))
            b -= 1
        return y
    else:
        return None
    pass

print(hexToDec('A2'))
print(hexToDec('spam spam spam'))
print(hexToDec('A'))
print(hexToDec('0'))
print(hexToDec('1B'))
print(hexToDec('3C0'))
print(hexToDec('A6G'))
print(hexToDec('ZZT0P'))