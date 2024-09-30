def afuc():
    import math
    
    a = int(input("value of a is = "))

    result = math.sqrt(a)
    
    return result

def bfuc():
    from math import sqrt,pi
    
    b = int(input("value of  b is = "))

    result1 = sqrt(b)
    
    result2 = pi*b**2

    return result1,result2

def cfuc():
    import math as m
    
    c = int(input("value of c is = "))
    
    result = m.sqrt(c)
    
    return result

def dfuc():
    
    import math as m
    
    print(dir(m))


# print(afuc())

# print(bfuc())

# print(cfuc())

# print(dfuc())


from num import *

print(a+b)

welcome()

print(__name__)