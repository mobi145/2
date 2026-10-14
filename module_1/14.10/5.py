a = int(input("a:"))
b = int(input("b:"))
c = input("+ or - or / or *: ")
if c == "+":
    print(f"{a + b}")
elif c == "-":
    print(f"{a - b}")
elif c == "/":
    print(f"{a / b}")
elif c == "*":
    print(f"{a * b}")
else:
    print("wrong symbol")
