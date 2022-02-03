# any_exception.py fängt alle Arten von Exceptions ab
try:
    zaehler = int(input('Zähler: '))
    nenner = int(input('Nenner: '))
    ergebnis = zaehler / nenner
    print(ergebnis)
except:
    print('Irgendeine Exception ist aufgetreten')
