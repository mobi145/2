lenght=int(input("lenght="))
symbol=input("symbol=")
direction=input("| or --: ")
if direction=="--":
        print(symbol*lenght)
elif direction=="|":
    for i in range(lenght):
        print(symbol)
else:
    print("incorrect")