# kreis_flaeche.py berechtet die Fläche eines Kreises
print("Fläche eines Kreises in Quadratzentimeter")
durchmesser = float(input("Durchmesser in cm: "))
radius = durchmesser / 2
pi = 3.1416
flaeche = radius ** 2 * pi
print("Fläche in Quadratzentimeter:", flaeche)