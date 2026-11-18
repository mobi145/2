from module_1 import calc
from module_1.calc import square


def product(a, b):
    if a>b:
        a,b=b,a
    c=1
    for i in range(a, b+1):
        c*=i
    return c

print(product(1, 5))

def max_of_list(list):
    max=list[0]

    for d in list:
        if d>max:
            max=d
    return max

print(max_of_list([1, 4, 7, 25, 1488]))

def two_dii(list):
    sum = 0
    count = 0

    for num in list:
        sum += num
        count += 1

    average = sum / count
    return sum, average

print(two_dii([4, 5, 3]))

def fact(numbers):
    a = []
    for num in numbers:
        f = calc.factorial(num)
        a.append(f)
    return a

print(fact([4, 5, 3]))

def perf_square(n):
  if n < 0:
    return False
  root = int(square(n, 0.5))
  return root * root == n

def fibonachi(list):
    fibonachi = []
    for num in list:
        if num >= 0 and (
                perf_square(5 * num * num + 4)
                or perf_square(5 * num * num - 4)
        ):
            fibonachi.append(num)
    return fibonachi

print(fibonachi([0, 1, 2, 3, 4, 5, 8, 10, 13, 20, 21,25, 30, 100, 200, 1488, 4181]))