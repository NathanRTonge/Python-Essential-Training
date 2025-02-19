"""
Contains info on threads & multithreading
"""

import threading
import time

# Example of a function that could take a long time if called
def longSquare(num):
    time.sleep(0.5)
    return num**2
# Takes especially long if called over iterables
print([longSquare(n) for n in range(5)])

print('------------------')

"""Threading
allows for a process to have many activities running in parallel"""

def longSquare(num,results):
    time.sleep(1)
    results[num] = num**2

results = {} #empty dictionary to put our results in
#creates 2 threads to calculate longSquare(anumber, results)
t1 = threading.Thread(target= longSquare, args= (1,results))
t2 = threading.Thread(target= longSquare, args= (2,results))

# Starts the two threads
t1.start()
t2.start()
# Joins the 2 threads
t1.join()
t2.join()

print(results)

print('------------------')

def longSquare(num,results):
    time.sleep(1)
    results[num] = num**2

results = {}
# creates 100 threads to calculate
threads = [threading.Thread(target= longSquare, args= (n,results)) for n in range(100)]
# starts & joins all the threads
[t.start() for t in threads]
[t.join() for t in threads]

print(results)
