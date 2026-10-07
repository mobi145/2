a=int(input("Введіть кількість: "))
t=str(input("Ввиберіть валюту (USD EUR): "))
if (t=="USD"):
    print(f"{a} Доларів в грн це {a*44.86}")
elif (t=="EUR"):
    print(f"{a} Євро в грн це {a * 50.15}")
else:
    print("Помилка")