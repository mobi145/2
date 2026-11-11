import calc
a=1
b=1
while True:
    print("\n--- МЕНЮ ---")
    print("1. вибір чисел")
    print("2. додавання")
    print("3. віднімання")
    print("4. множення")
    print("5. ділення")
    print("6. піднесення до квадрата")
    print("7. віднесення від квадрата")
    print("8. факторіал обох чисол")
    print("0. Вихід")

    choose = input("Оберіть пункт (0-7): ")
    if choose == '1':
        a = int(input("a="))
        b = int(input("b="))
    elif choose == '2':
        z = calc.add(a, b)
        print(z)
    elif choose == '3':
        x = calc.min(a, b)
        print(x)
    elif choose == '4':
        c = calc.mult(a, b)
        print(c)
    elif choose == '5':
        v = calc.div(a, b)
        print(v)
    elif choose == '6':
        b = calc.square(a, b)
        print(b)
    elif choose == '7':
        n = calc.notsquare(a, b)
        print(n)
    elif choose == '8':
        m = calc.factorial(a)
        print(m)
        m = calc.factorial(b)
        print(m)

    elif choose == '0':

        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")