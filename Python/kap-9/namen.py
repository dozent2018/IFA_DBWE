# namen.py baut eine Liste aus den Eingaben des Benutzers auf

# Eine leere Liste erzeugen
liste = []

while True:
    eingabe = input("Geben Sie einen Namen ein. Abschluss mit ENDE: ")
    if eingabe == 'ENDE':
        break
    liste.append(eingabe)
liste.sort()
print(liste)

max_index = len(liste) - 1
while True:
    index = int(input("Index?. Abschluss mit einer Zahl > " + str(max_index)))
    if index > max_index :
        break
    print(liste[index])
