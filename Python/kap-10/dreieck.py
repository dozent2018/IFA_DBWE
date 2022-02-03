zeilen = int ( input('Seitenlänge: '))
for zeile in range(1zeilen + 1):
    # Anzahl Spalten = Nr. der Zeile
    spalten = zeile
    # ausgabe wird auf einen leeren String zurückgesetzt
    ausgabe = ''
    for spalte in range(spalten):
        # Für jede Spalte wird '* ' angehängt
        ausgabe = ausgabe + '* '
    print(ausgabe)