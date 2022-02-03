# lottoziehung.py zieht die Lottozahlen mit randint()

from random import randint

# Intialisierung der Variablen
ziehung = []
gezogen = 0

# Ziehung der Lottozahlen
while len(ziehung) < 6 :
    gezogen = randint(1, 49)
    if gezogen not in ziehung :
        # Wenn die Zahl noch nicht gezogen wurde, wird Sie der Liste hinzugefügt
        ziehung.append(gezogen)

# Ausgabe der Lottozahlen
print( "Ziehung:", sorted(ziehung))


