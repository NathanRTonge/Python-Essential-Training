"""
Contains info on While loops (pass, break & continue)
"""

from datetime import datetime

"""While Loop"""
print(datetime.now().second)  #gives the current second of the minute
print(datetime.now().second +2) #gives what the second will be in 2 secs (will give 61)
print((datetime.now().second +2) % 60) #gives the actual second in 2sec accounting for minutes

print('-----------------------')

#/ wait_until gives the time we are waiting for (2sec ahead)
wait_until = (datetime.now().second +2) % 60

#/ this will print out loots of values and clog the console
print(f'We are at {datetime.now().second} seconds')
while datetime.now().second != wait_until:
    print('Waiting')
print(f'at {datetime.now().second} seconds')

print('-----------------------')

"""Pass"""

#/ A way to stop this is by using 'pass' in the loop
wait_until = (datetime.now().second +2) % 60
print(f'We are at {datetime.now().second} seconds')
while datetime.now().second != wait_until:
    pass
print(f'at {datetime.now().second} seconds')
#/ pass saves on processing power and also can act
#  as a placeholder, as it tells the code to ignore it

print('-----------------------')

"""Break"""

#/ break statement leaves the current loop completely
wait_until = (datetime.now().second +2) % 60
print(f'We are at {datetime.now().second} seconds')
while True:
    if datetime.now().second == wait_until:
        print(f'at {datetime.now().second} seconds')
        break
#/ only breaks out of the first loop above, not nested loops

print('-----------------------')

"""Continue"""

#/ tells the code to return to top of current loop
wait_until = (datetime.now().second +2) % 60
print(f'We are at {datetime.now().second} seconds')
while True:
    if datetime.now().second < wait_until:
        continue
    break
print(f'at {datetime.now().second} seconds')
#/ pass, break & continue can all be used to do the same
#/ thing, so use the one that makes code more understandable
