# return_list.py demonstriert die Funktion reihe(anzahl). 
# Sie gibt die Folge der Zahlen von 0 bis anzahl als Liste zurück
def reihe(zahl):
    # Mit leerer Liste starten
    zahlen=[]
    for zahl in range(zahl+1):
        # Die nächste zahl an die Liste anhängen
        zahlen.append(zahl)
    # Die Liste mit return zurückgeben
    return zahlen

# Aufruf von reihe()
ergebnis = reihe(8)
print(ergebnis)
