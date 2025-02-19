"""
Create functions to compress ascii art
"""

import json

def encodeString(stringVal):
    letters = [character for character in stringVal]
    b=[]
    x=0
    for i in range(len(letters)):
        if (letters[i] == letters[i-1] or i == 0) and (i < len(letters)-1):
            x += 1
            continue
        elif i == len(letters)-1:
            x +=1
            ch = letters[i-1]
            b.append((ch, x))
        else:
            ch = letters[i-1]
            b.append((ch, x))
            x=1
            continue
    return b

def decodeString(encodedList):
    a = []
    string =''
    for key,value in encodedList:
        a.append(key*value)
    for i in range(len(a)):
        string += a[i]
    return string

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        with open(newFilename, 'w') as g:
            g.write(json.dumps(encodeString(f.read())))

def decodeFile(filename):
    with open(filename, 'r') as f:
        return decodeString(json.loads(f.read()))