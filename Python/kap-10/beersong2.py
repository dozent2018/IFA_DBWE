# beersong2.py ersetzt die while-Schleife in beersong1.py
# mit range() und einer for-Schleife

# Variablen deklarieren
text1 = "Flaschen Bier"
text2 = "Im Kühlschrank"
anzahl_flaschen=0

print("Der Kühlschrank ist leer.")
# Eingabe des Startwerts
anzahl_flaschen= int(input('Wieviele Flaschen Bier kaufen? '))

# Trink-Schleife
for i in range(anzahl_flaschen, 0, -1) :
    if i == 1:
        text1 = "Flasche Bier"
    print(i, text1, text2)
    print(i, text1)
    print("Nimm Eine raus")
    print("Trink Sie aus")
    print()

print("Der Kühlschrank ist leer ...\n")