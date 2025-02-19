"""
Contains info on how to open, read & write to files
"""

"""Reading Files"""

f = open('10_01_file.txt', 'r') #opens txt file in 'r'ead mode
print(f) #prints the object

print('----------------')

print(f.read()) # gives string of file start to finish

print('----------------')

f = open('10_01_file.txt', 'r')
print(f.readline()) #prints the first unread line in the file
print(f.readline()) # prints the 2nd unread line in the file
print(str(f.readlines())) #prints all unread lines in file as list

print('----------------')

f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line) # prints each line of file (including /n)

print('----------------')

f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line.strip()) #removes /n, meaning single spaced lines

print('----------------')

"""Writing Files"""

f = open('10_01_output.txt', 'w') #opens txt file in 'w'rite mode
print(f)

print('----------------')

f.write('Line 1 \n') #writes 'Line 1' then starts new line
f.write('Line 2 \n')
f.write('Line 3 \n')
f.close()
# This overwrites all that was in the file before

"""Appending Files"""

f = open('10_01_output.txt', 'a') #opens txt file in 'a'ppend mode
print(f)

print('----------------')

f.write('Line 4 \n') #writes 'Line 4' after lines written before
f.write('Line 5 \n')
f.write('Line 6 \n')
f.close() #always remember to close files after finishing with them

"""With"""

with open('10_01_output.txt', 'a') as f:
    f.write('Stuff \n')
    f.write('Other stuff \n')
# as soon as we outdent, file will close

print(f)
f.write('trying to write after with block')

