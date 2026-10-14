import math
d = float(input("Enter diameter: "))
choice = input("Choice area/perimeter: ")
r = d / 2
if choice == "area":
    area = math.pi * (r**2)
    print(f"S: {area:.2f}")
elif choice == "perimeter":
    perimeter = math.pi * d
    print(f"perimetr: {perimeter:.2f}")
else:
    print("incorect")