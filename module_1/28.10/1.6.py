while True:
    a = int(input("1+/2-/3*/4quit= "))
    if a==1:
        a = int(input("1="))
        b = int(input("2="))
        c=a+b
        print(c)
    elif a==2:
        a = int(input("1="))
        b = int(input("2="))
        c=a-b
        print(c)
    elif a == 3:
        a = int(input("1="))
        b = int(input("2="))
        c = a * b
        print(c)
    elif a==4:
        break
    else:
        print("wrong")