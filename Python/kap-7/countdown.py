zahl = int ( input("Geben Sie ein, wo der Countdown beginnen soll: "))
if zahl > 0:
    while zahl > 0:
        print(zahl)
        zahl -= 1
    print("Start!")
else:
    print("Eingabe einer Zahl grösser als 0 ist erforderlich!")