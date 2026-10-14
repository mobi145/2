a = float(input("Enter price of console: "))
b = int(input("Enter quantity: "))
c = float(input("Enter discount percentage: "))
d = input("Choice one/total: ")
e = a * (1 - c / 100)
if d == "one":
    print(f"1 with znugka: {e:.2f}")
elif d == "total":
    f = e * b
    print(f"sum: {f:.2f}")
else:
    print("Неправильний вибір! Введіть one або total.")