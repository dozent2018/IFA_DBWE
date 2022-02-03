ergebnis = 1
zahl = int( input("Ganze Zahl: "))
for faktor in range(1, zahl+1):
    ergebnis = ergebnis * faktor
print("Fakultät", zahl, "=", ergebnis )