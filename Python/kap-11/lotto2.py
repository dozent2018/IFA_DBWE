""" lotto2.py liest einen String mit Zahlen ein, wandelt ihn 
in eine Liste um und vergleicht jede Zahl in der Liste mit 
Zahlen in einer Liste, die mit randint() erzeugt wurde """

from random import randint

# Intialisierung der Variablen
ziehung = []
gezogen = 0
tipp = []
richtige = []
anzahl_richtige = 0
getippt = 0

# ZIEHUNG der Lottozahlen
while len(ziehung) < 6 :
    gezogen = randint(1, 49)
    if gezogen not in ziehung :
        # Wenn die Zahl noch nicht gezogen wurde, wird Sie der Liste hinzugefügt
        ziehung.append(gezogen)

# EINGABE, alle Zahlen auf einmal
eingabe_string = input('Geben Sie Ihren Tipp ein. (6 Zahlen von 1 bis 49): ')
# Die durch Leerzeichen getrennten Eingaben werden in eine Liste umgewandelt
eingabe_liste = eingabe_string.split()
for element in eingabe_liste :
    # In der Liste eingaben stehen Strings.
    # Sie müssen noch in Zahlen umgewandelt werden
    if element.isdecimal() :
        # nun kann element in eine Zahl umgewandelt werden 
        zahl = int(element)
        # Die Zahl kann an die Liste tipp angehängt werden, wenn 
        # die Zahl >= 1 und <= 49 ist und sie nicht bereits 
        # darin vorkommt und bisher weniger als 6 Zahlen vorhanden sind
        if zahl >= 1 and zahl <= 49 and zahl not in tipp and len(tipp) < 6 :
            tipp.append(zahl)
        else :
            # Ignorieren, wenn element keine Dezimalzahl ist
            continue
"""Anmerkung: Wenn Sie immer 6 Zahlen einlesen wollten, müssten Sie die Eingabe noch in 
eine Schleife verpacken und sie solange wiederholen, bis 6 Zahlen eingegeben wurden """

#  PRUEFUNG auf Richtige im Tipp 
for zahl in tipp :
    if zahl in ziehung :
        richtige.append(zahl)
        anzahl_richtige = anzahl_richtige + 1

# AUSGABE Ergebnis
print( "Ziehung:", sorted(ziehung))
print( "Ihr Tipp:", sorted(tipp))
print( "Richtige:", len(richtige), richtige)

