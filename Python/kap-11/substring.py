eingabe = input('Eingabe einer Zeichenkette: ')
eingaben_liste = eingabe.split()
string = eingaben_liste[0]
for wort in eingaben_liste[1:] :
    if wort in string :
        print(wort, "gefunden")
