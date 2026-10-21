
s = input("Введіть шестизначне число: ")
if len(s) == 6 and s.isdigit():
    sum1 = int(s[0]) + int(s[1]) + int(s[2])
    sum2 = int(s[3]) + int(s[4]) + int(s[5])
    if sum1 == sum2:
        print("Число щасливе!")
    else:
        print("Число нещасливе.")
else:
    print("Помилка! Потрібно ввести рівно 6 цифр.")