"""
Contains useful info for byte (ie. 01010010) object
"""

#byte objects
print(bytes(5))
"""Creates empty byte object 5 bytes long
Each byte is \x00
Byte represented by 2-digit hexadecimal number (16x16) = (2^8)"""

print(bytearray(5))    #creates array of 5 empty bytes
print(bytearray(5)[3]) #4th byte = 00(hex) = 0(dec)
print('')

#the example string is represented
#in the utf-8 numbers by default
example = bytes(b'hello')
print(example[0], example[1],
      example[2],example[3],example[4])
example2 = bytes('hello', 'utf-8')
print(example2[0], example2[1],
      example2[2],example2[3],example2[4])
print('')

#by creating a byte array we can alter and change the bytes
#in the data
smile_byte = bytearray('Banana', 'utf-8')
print(smile_byte)
print(smile_byte[0])
smile_byte[0] = 65
print(smile_byte)
