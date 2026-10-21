while True:
    a=int(input("1-12:"))
    if a in (1, 2 ,12):
        print("Winter")
    elif a in (3, 4 ,5):
        print("Spring") #пружина
    elif a in (6, 7 ,8):
        print("Summer")
    elif a in (9, 10 ,11):
        print("Autumn") #падать
    else:
        print("incorect")