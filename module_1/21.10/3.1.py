earn=int(input("paycheck: "))
stag=int(input("experience in years: "))
if 0<= stag <=1:
    print("no bonus for you lol")
elif 1<= stag <=3:
    print(f"5% bonus {((earn/100)*5)+earn}$ ({((earn/100)*5)}$ bonus)")
elif 3<= stag <=5:
    print(f"10% bonus {((earn/100)*101)+earn}$ ({((earn/100)*10)}$ bonus)")
elif 5<= stag:
    print(f"15% bonus {((earn/100)*15)+earn}$ ({((earn/100)*15)}$ bonus)")
else:
    print("incorrect")