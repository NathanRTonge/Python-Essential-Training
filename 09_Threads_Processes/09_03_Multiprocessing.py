"""
Contains info on multiprocessing
PLEASE NOTE
Will only work in actual python console or jupyter
Notebooks, not IDE
"""
from multiprocessing import Process

def longSquare(num):
    import time
    time.sleep(1)
    print(num**2)
    print('finished')

results = {}
processes = [Process(target= longSquare, args= (n,results)) for n in range(10)]
[p.start() for p in processes]
[p.join() for p in processes]


