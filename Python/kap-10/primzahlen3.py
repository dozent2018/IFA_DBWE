# primzahlen3.py Primzahlen finden mit timer
import time
untere_grenze = int(input("Primzahlen im Bereich von: "))
obere_grenze = int(input("bis: ")) + 1
# Eine untere Grenze < 2 ist nicht sinnvoll
if untere_grenze < 2:
    untere_grenze = 2
startzeit = time.perf_counter()
# Zahl für Zahl prüfen
for zahl in range(untere_grenze, obere_grenze):
    ist_prim = True
    # Für jede Zahl alle Teiler von 2 bis Zahl ausprobieren
    for teiler in range( 2, zahl):
        if zahl % teiler == 0:
            # Die Zahl ist ohne Rest teilbar -> keine Primzahl
            # es ist nicht nowendig, weiter zu probieren
            ist_prim = False
            break;
    if ist_prim == True:
        pass
        #print(zahl)
stopzeit = time.perf_counter()
print('Laufzeit in Sekunden: ', stopzeit - startzeit)