cifry =input("Введіть число: ")

if not cifry.isdigit():
    print("Помилка: введіть ціле число!")
    exit()

while True:
    print("\n--- МЕНЮ ---")
    print("1. Кількість цифр")
    print("2. Сума цифр")
    print("3. Середнє арифметичне")
    print("4. Кількість нулів")
    print("5. Ввести інше число")
    print("0. Вихід")

    vybir = input("Оберіть пункт (0-5): ")

    if vybir == '1':
        kilkist = len(cifry)
        print(f"Кількість цифр: {kilkist}")

    elif vybir == '2':
        suma = sum(int(litera) for litera in cifry)
        print(f"Сума цифр: {suma}")

    elif vybir == '3':
        suma = sum(int(litera) for litera in cifry)
        kilkist = len(cifry)
        serednye = suma / kilkist if kilkist > 0 else 0
        print(f"Середнє арифметичне: {serednye}")

    elif vybir == '4':
        nuliv = cifry.count('0')
        print(f"Кількість нулів: {nuliv}")

    elif vybir == '5':
        cifry = input("Введіть нове число: ")
        if not cifry.isdigit():
            print("Помилка: введіть ціле число!")
            exit()
        print("Число оновлено!")

    elif vybir == '0':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")