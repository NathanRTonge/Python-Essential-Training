"""
Contains info on CSV files
"""
import csv

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f) #iterable like list, reader objects can read csvs
    for row in reader:
        print(row)
# We see that instead of commas, lines are separated with
# \t, so we set that as the delimiter

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader) #this skips the header for CSV file
    for row in reader:
        print(row)
print('----------------') #or;
with open('10_02_us.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter='\t'))
    for row in reader[:20]: #can skip the header for CSV file
        print(row)

print('----------------')

# If you wish to use the header you can use .DictReader
with open('10_02_us.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        print(row)
# This creates a dictionary with the headers as the keys

print('----------------')

"""Filtering Data"""

with open('10_02_us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

primes = []
for num in range(2,99999): # prime numbers that are also postal codes
    for fact in range(2, int(num**0.5) ):
        if num % fact ==0:
            break
    else:
        primes.append(num)

# Finds prime postal codes in california
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'CA']
print(len(data)) #224

"""Writing"""
with open('10_02_ca_prime.csv', 'w') as f:
    writer = csv.writer(f) #writer objects can write to csvs
    for row in data:
        writer.writerow([row['place name'], row['county']])