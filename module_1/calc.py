def add(a, b):
    return a+b
def min(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
def square(a, b):
    return a**b
def notsquare(a, b):
    return round(a ** (1 / b))
def factorial(d):
    result = 1
    for i in range(2, d + 1):
        result *= i
    return result