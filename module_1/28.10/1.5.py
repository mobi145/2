while True:
    a = int(input("1max/2min/3quit= "))
    if a==1:
        a = int(input("1="))
        b = int(input("2="))
        c=max(a,b)
        print(c)
    elif a==2:
        a = int(input("1="))
        b = int(input("2="))
        c=min(a,b)
        print(c)
    elif a==3:
        print("exiting")
        break
    else:
        print("wrong")