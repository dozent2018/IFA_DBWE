# volumen.py fragt die Form und die Abmessungen für verschiedene Blumenkübel ab
# und berechnet daraus das Volumen in Litern
pi = 3.142
volumen = 0
anzahl_5l = 0
anzahl_10l = 0
anzahl_20l = 0

form = input('Form: (Ku)bus (Zy)linder oder (Ke)gelstumpf: ')
if form == 'Ku' :
    laenge = float(input('Länge in cm: '))
    breite = float(input('Breite in cm: '))
    hoehe = float(input('Höhe in cm: '))
    volumen = laenge * breite * hoehe / 1000
elif form == 'Zy' :
    durchmesser = float(input('Durchmesser in cm: '))
    hoehe = float(input('Höhe in cm: '))
    volumen = pi * (durchmesser / 2 ) ** 2 * hoehe / 1000
elif form == 'Ke' :
    durchm_oben = float(input('Durchmesser oben in cm: '))
    durchm_unten = float(input('Durchmesser unten in cm: '))
    hoehe = float(input('Höhe in cm: '))
    volumen = hoehe * pi / 12 * (durchm_oben ** 2 + durchm_oben *
              durchm_unten + durchm_unten ** 2) / 1000
else :
    print('Ungültige Eingabe')
if volumen != 0 :
    print('Volumen:', volumen, 'Liter')

# Berechnung der Anzahl Säcke Blumenerde
anzahl_20l = int(volumen // 20)
volumen = volumen - 20 * anzahl_20l
# ist das verbleibende Volumen > 15L ? Dann ist ein weiterer 20L-Sack günstiger
if volumen > 15 :
    anzahl_20l += 1
    volumen -= 20
# ist das verbleibende Volumen >= 10L ? Dann ist mindestens ein 10L-Sack erforderlich
if volumen >= 10 :
    anzahl_10l += 1
    volumen = volumen - 10
# Ist das verbleibende Volumen > 5L ? Dann ist der 2. 10L-Sack günstiger
if volumen > 5 :
    anzahl_10l += 1
    volumen = volumen - 10
# Ansonsten: Für den Rest reicht ein 5L-Sack
if volumen > 0:
    anzahl_5l = 1

print(anzahl_20l, 'x 20L kosten', anzahl_20l * 14.0)
print(anzahl_10l, 'x 10L kosten', anzahl_10l * 8.0)
print(anzahl_5l,  'x 5L  kostet ', anzahl_5l * 5.0)
print('Gesamtkosten:', anzahl_20l * 14.0 + anzahl_10l * 8.0 + anzahl_5l * 5.0)



