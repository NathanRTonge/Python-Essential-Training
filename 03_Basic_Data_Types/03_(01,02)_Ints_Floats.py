"""
03_01
Contains useful funcs for numbers (int<->float)
"""

print(
3.915/2,' |',           #gives long float that rounds to 2
int(3.915/2),' |',      #int() TRUNCATES the float
round(3.915/2),' |',    #round(float), rounds to nearest integer
round(3.915/2, 2),' |', #round(float, num) rounds to num d.p.
round(3.915/2, 3),
)
print('')

"""
03_02
Contains more useful funcs for numbers (dec<->hex<->bin)
"""

#imports the Decimal class that does away with floating point errors
from decimal import Decimal, getcontext

#converting from other bases
print(
int('100'),' |',     #converts str to decimal number
int('100', 10),' |', #int(str, num), str is written in base num
int('100', 2),' |',  #base 2 > binary
int('ff', 16),' |',  #base 16 > hexadecimal
)
print('')

#Decimals
getcontext()           #Prints all the parameters of the decimal class
print(Decimal(2)/Decimal(3))  #see here rounded accurately to 19 dp
getcontext().prec =2          #can change decimal parameters
print(getcontext())
print(Decimal(2)/Decimal(3))
print(Decimal(0.6))           #try not to use floats or fpe gets carried over
print(Decimal('0.6'))         #can be fixed by using string