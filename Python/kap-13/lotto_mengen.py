""" lotto3.py zeigt, wie Mengen und Tupel statt Listen eigesetzt werden können
    Dabei werden die Ziehung der Lottozahlen, die Eingabe des Tipps und die
    Prüfung des Ergebnisses aus dem Programm lotto2.py vereinfacht """

from random import randint

# Intialisierung der Variablen
ziehung = set()
tipp = { 1, 34, 9, 15, 29, 41, }
zahl = 0
eingabe_string = ''

# Ziehung der Lottozahlen mit Set statt Liste: Da Sets keine Duplikate enthalten können, 
# fällt die Prüfung auf Duplikate weg. Wiederholung,bis 6 Zahlen gezogen wurden
while len(ziehung) < 6 :
    ziehung.add(randint(1, 49))

# Eingabe des Tipps
eingabe_string = input('Geben Sie Ihren Tipp ein. (6 Zahlen von 1 bis 49): ')
eingabe_liste = eingabe_string.split()
for element in eingabe_liste :
    if element.isdecimal() :
        zahl = int(element)
        # Es muss nicht mehr geprüft werden, ob die Zahl schon in tipp existiert
        if zahl >= 1 and zahl <= 49 and len(tipp) < 6 :
            tipp.add(zahl)
        else :
            # Ignorieren, wenn element keine Dezimalzahl ist
            continue

# Das Ergebnis mit Sets auswerten und ausgeben
print( "Ziehung:", sorted(list(ziehung)) )
print( "Tipp:", sorted(list(tipp)) )
print( "Richtige:", len(tipp & ziehung), sorted(list(tipp & ziehung)) )



