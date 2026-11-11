vusota = int(input("vusota: "))
shyryna = int(input("shyryna: "))
rozmir = int(input("rozmir(х на х): "))

for rad in range(vusota):
    tekst_radu = ""
    for kolonka in range(shyryna):
        if (rad + kolonka) % 2 == 0:
            tekst_radu += "#" * rozmir + " "

        else:
            tekst_radu += " " * rozmir + " "

    for _ in range(rozmir):
        print(tekst_radu)