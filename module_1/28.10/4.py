a=int(input("1="))
b=int(input("2="))
c=int(input("3="))
if a<b:
    if c==1:
        for num in range(a, b + 1):
           if num % 2 != 0:
              print(num)
    elif c==2:
        for num in range(b, a - 1,-1):
           if num % 2 != 0:
              print(num)
    else:
        print("3 wrong")
else:
    print("wrong")