a=int(input("Введіть кількість: "))
t=str(input("Ввиберіть валюту (USD EUR PLN): "))
if (t=="USD"):
    print(f"{a} Доларів в грн це {a*44.86}")
elif (t=="EUR"):
    print(f"{a} Євро в грн це {a * 50.15}")
elif (t=="PLN"):
    print(f"{a} Польських злотих в грн це {a * 11.48}")
elif (t == "TRY"):
    print(f"{a} Турецьких лірах в грн це {a * 0.91}")
else:
    print("Помилка")