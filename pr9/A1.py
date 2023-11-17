import math

def c(x, n):
    r = (x ** n) / math.factorial(n)
    return r
x = 39
n = 27
print(c(x, n))
