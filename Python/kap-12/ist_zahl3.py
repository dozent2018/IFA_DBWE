# ist_zahl3.py nutzt den try - except Mechanismus, um auf
# Fehler bei der Umwandlung str -> int zu reagieren
# Um auch auf Eingaben wie 4.0 oder 5.33 zu reagieren, wird
# zunächst in float umgewandelt, anschliessen in int
konvertiert = False

while konvertiert == False :
    try:
        zahl = int(float(input('Geben Sie eine ganze Zahl ein: ')))
        # int(float) schneidet die Nachkommastellen ab
        konvertiert = True
    except ValueError :
        print('Ihre Eingabe ist keine Zahl.')

print('Die Zahl ist: ', zahl)