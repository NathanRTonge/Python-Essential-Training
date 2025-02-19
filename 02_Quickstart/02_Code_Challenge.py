def factorial(num):
    if (type(num) == int) and (num >= 0):
        x=1
        for i in range(1,num) :
            x = x + i*x
        return x
    else:
        return None

print(factorial(5))
print(factorial('5'))
print(factorial(6))
print(factorial(0))
print(factorial(-2))
print(factorial(1.2))
print(factorial('spam spam spam spam'))