# lotto1.py liest eine Liste mit Zahlen ein und vergleicht
# jede Zahl in der Liste mit einer Liste, die mit randint()
# erzeugt wurde

from random import randint

# Intialisierung der Variablen
ziehung = []
tipp = []
gezogen = 0
richtige = []
zahl_eingaben = 0
zahl = 0
eingabe = ''

# ZIEHUNG der Lottozahlen
while len(ziehung) < 6 :
    gezogen = randint(1, 49)
    if gezogen not in ziehung :
        # Wenn die Zahl noch nicht gezogen wurde, wird Sie der Liste hinzugefügt
        ziehung.append(gezogen)

# EINGABE von 6 Zahlen, eine nach der anderen
print( "Geben Sie Ihren Tipp ein. (6 Zahlen von 1 bis 49)" )
while len(tipp) < 6 :
    print("Bisher eingegeben: ", tipp)
    eingabe = input( "Geben Sie eine neue Zahl von 1 bis 49 ein: ")
    # Es wird geprüft, ob die Eingabe eine Zahl darstellt
    if eingabe.isdecimal():
        zahl = int(eingabe)
        #Prüfung, ob es eine Zahl zwischen 1 und 49 ist
        # und ob die Zahl bereits eingegeben wurde
        if zahl >= 1 and zahl <= 49 and zahl not in tipp :
            tipp.append(zahl)
        else :
            print("Zahl schon vorhanden oder ausserhalb des Bereichs")
    else :
        print("Eingabe war keine ganze Zahl")
    

for zahl in tipp :
    if zahl in ziehung :
        richtige.append(zahl)

print( "Ziehung:", sorted(ziehung))
print( "Ihr Tipp:", sorted(tipp))
print( "Richtige:", len(richtige), richtige)

