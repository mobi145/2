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

def spusok(list):
    pass