def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num -1 ) )

n = 7
number=factorial(n)
print(number)

def fibonaki(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibonaki(n-1)+fibonaki(n-2))

m = 7
number = fibonaki(m)
print(number)

