# vokale.py prüft, welche Vokale in einem String vorhanden sind

wort = input("Geben Sie etwas Text ein: ")
vokale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U']

# Mit <in> kann geprüft werden, ob ein Buchstabe in einem String enthalten ist
# Mit <in> kann geprüft werden, ob ein Objekt in einer Liste enthalten ist
for buchstabe in wort:
    if buchstabe in vokale:
        print(buchstabe)



