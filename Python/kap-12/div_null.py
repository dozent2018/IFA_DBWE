# div_null.py fängt eine Division durch 0 ab
zaehler = int(input('Zähler: '))
nenner = int(input('Nenner: '))

try:
    ergebnis = zaehler / nenner
    print(ergebnis)
except ZeroDivisionError:
    print('Division durch 0 ist nicht erlaubt')