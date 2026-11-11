import random

print("--- ПЕРЕВІРКА ЗНАННЯ ТАБЛИЦІ МНОЖЕННЯ ---")
print("Оберіть рівень складності:")
print("1. Легкий (5 питань, числа від 2 до 5)")
print("2. Середній (10 питань, числа від 2 до 9)")
print("3. Складний (15 питань, числа від 6 до 12)")

vybir = input("Введіть номер рівня (1-3): ")

if vybir == '1':
    kilkist_pytan = 5
    min_chysl = 2
    max_chysl = 5
elif vybir == '2':
    kilkist_pytan = 10
    min_chysl = 2
    max_chysl = 9
elif vybir == '3':
    kilkist_pytan = 15
    min_chysl = 6
    max_chysl = 12
else:
    print("Невірний вибір, встановлено легкий рівень за замовчуванням.")
    kilkist_pytan = 5
    min_chysl = 2
    max_chysl = 5

baly = 0

for i in range(1, kilkist_pytan + 1):
    a = random.randint(min_chysl, max_chysl)
    b = random.randint(min_chysl, max_chysl)
    pravylno = a * b

    vidpovid = int(input(f"Питання {i}: Скільки буде {a} * {b}? "))

    if vidpovid == pravylno:
        print("Вірно! 🎉")
        baly += 1
    else:
        print(f"Помилка! Правильна відповідь: {pravylno}")

print("\n--- РЕЗУЛЬТАТИ ---")
print(f"Ви відповіли правильно на {baly} з {kilkist_pytan} питань.")

otsinka = round((baly / kilkist_pytan) * 12)
print(f"ваша оцінка(за 12 - бальною системою): {otsinka}")