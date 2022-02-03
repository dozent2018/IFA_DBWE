# continue_demo.py zählt von 0 bis zum angegebenen Wert,
# gibt aber nur jeweils volle 10-er Werte aus

zaehlen_bis = int(input("Zählen bis: "))
zahl = 0
while zahl < zaehlen_bis:
    zahl = zahl + 1
    # Es wird geprüft, ob der Divisionsrest ungleich 0 ist
    if zahl % 10 != 0:
        continue
    print(zahl)
