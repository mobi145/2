a=int(input("1="))
b=int(input("2="))
c=0
d=0
if a<b:
    for i in range(a,b+1,1):
        c+=i
        d=c/b
        print(f"{c}{b}")
if a>b:
    for i in range(b,a+1,1):
        print(i)
else:
    print("wrong")