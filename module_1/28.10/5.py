a=int(input("1="))
b=int(input("2="))
if a<b:
    for i in range(a,b+1,1):
        print(i)
if a>b:
    for i in range(b,a+1,1):
        print(i)
else:
    print("wrong")