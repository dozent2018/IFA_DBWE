# multi_exception.py fängt verschiedene Arten von Exceptions ab
liste = []
try:
    zaehler = int(input('Zähler: '))
    nenner = int(input('Nenner: '))
    ergebnis = zaehler / nenner
    liste.append(zaehler)
    liste.append(nenner)
    liste.append(ergebnis)
    position = int(input('Wert an Listen-Index: '))
    print(liste[position])
except ValueError:
    print('Fehler bei der Umwandlung str -> int')
except ZeroDivisionError:
    print('Division durch 0 ist nicht erlaubt')
except IndexError:
    print('Der Index liegt ausserhalb des Bereichs für diese Liste')  