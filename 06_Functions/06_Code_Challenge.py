"""
Challenge was to make a func(n) that gave n^2 without using ** or *,
relying on the previously defined triangle func
( I got this one very quickly:) )
"""

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num-1)

#/ Why this works eg.7
#  triangle(7) = 7 + 6 + 5 + 4 + 3 + 2 + 1
#  triangle(6) =     1 + 2 + 3 + 4 + 5 + 6
#               1st7 2nd 3rd 4th 5th 6th 7th 7 sevens or 7^2