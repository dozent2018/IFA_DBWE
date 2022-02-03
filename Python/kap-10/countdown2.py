# diese Variante von countdown benutzt range() und eine for-Schleife
# anstelle der while-Schleife
zahl = int ( input("Geben Sie ein, wo der Countdown beginnen soll: "))
if zahl > 0 :
    for i in range(zahl, 0, -1) :
        print(i)
    print("Start!")
else:
    print("Eingabe einer Zahl grösser als 0 ist erforderlich!")