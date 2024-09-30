def sum(a,b):
    return a+b

result = sum(10,45)
print("sum = ",result)


def GREATERNUMBER(a,b):
    if a>b:
        print("a is bigger and b is small")
    elif a==b:
        print("both have same value")
    else:
        print("b is bigger and a is small")

Number = GREATERNUMBER(10 , 45)
number1 = GREATERNUMBER(100 , 45)
number2 = GREATERNUMBER(100 , 100)

# default aeguments

def avg(a=1 , b=4):
    result = (a+b)/2
    # print("result = ",result)
    return result

print("result =",avg())

value =avg(a=9)
print("AVG =", value)

# required Argument

def avg(a , b=4):
    result = (a+b)/2
    # print("result = ",result)
    return result

# print("result =",avg())

value =avg(a=11)
print("AVG =", value)
 
# Keywordd Argument 

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")


# Variable-length arguments:

# Arbitrary Arguments

# *number = use as a tuple here * mean use somthing as a tuple

def avg(*number):
    # print(*number)
    sum = 0
    for i in number:
        # print(*number)
        sum = sum + i
    print("avg is = ",sum/len(number))

avg(5,6,4,4,5,3,6,1,5,67,98,76)

# Keyword Arbitrary Arguments:

# for the dictionary we use ** and make function

def name(**name):
    print("hello",name["fname"],name["mname"],name["lname"])
name(fname = "manoj",mname = "kumar",lname = "sharma")    
    