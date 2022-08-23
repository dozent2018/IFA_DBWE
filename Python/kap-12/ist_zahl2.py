# ist_zahl2.py nutzt den try - except Mechanismus, um auf
# Fehler bei der Umwandlung str -> int zu reagieren
konvertiert = False

while konvertiert == False :
    try:
        zahl = int(input('Geben Sie eine ganze Zahl ein: '))
        konvertiert = True
    except ValueError :
        print('Ihre Eingabe ist keine ganze Zahl.')

print('Die Zahl ist: ', zahl)
