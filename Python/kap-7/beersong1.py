#!/usr/local/bin/python3

# Variablen deklarieren
text1 = "Flaschen Bier"
text2 = "Im Kühlschrank"
anzahl_flaschen=0

print("Der Kühlschrank ist leer.")
# Eingabe des Startwerts
anzahl_flaschen= int(input('Wieviele Flaschen Bier kaufen? '))

# Trink-Schleife
while anzahl_flaschen > 0:
    if anzahl_flaschen == 1:
        text1 = "Flasche Bier"
    print(anzahl_flaschen, text1, text2)
    print(anzahl_flaschen, text1)
    print("Nimm Eine raus")
    print("Trink Sie aus")
    print()
    anzahl_flaschen -= 1

print("Der Kühlschrank ist leer ...\n")