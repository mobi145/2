a=int(input("1="))
b=int(input("2="))
if a<b:
    for num in range(b, a - 1,-1):
        if num % 2 == 0:
            print(num)
else:
    print("wrong")