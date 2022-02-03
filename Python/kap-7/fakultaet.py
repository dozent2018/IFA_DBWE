# fakultaet.py berechnet die Fakultät einer eingegebenen Zahl und gibt sie aus
grenze = int(input('Zahl: '))
zaehler = 1
zahl = 1
while zaehler <= grenze:
    zahl = zahl * zaehler
    zaehler = zaehler + 1
print(grenze, '! = ' , zahl)