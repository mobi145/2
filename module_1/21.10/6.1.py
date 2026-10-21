s = input("Введіть шестизначне число: ")
if len(s) == 6 and s.isdigit():
    result = s[5] + s[4] + s[2] + s[3] + s[1] + s[0]
    print("Результат:", result)
else:
    print("Помилка! Потрібно ввести рівно 6 цифр.")