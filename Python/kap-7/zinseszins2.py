# zinseszins2.py berechnet für einen Kapitalbetrag,
# einen festen Zinssatz in % und eine Laufzeit in Jahren
# den den am Ende jedes Jahres erreichten Betrag

# Initialisierung der Variablen
kap_anfang = 0
kap_ende = 0
zinssatz = 0
jahre = 0
jahr = 0

print("Kapitalbetrag nach Verzinsung über eine Anzahl Jahre")
kap_anfang = float(input("Anfangskapital: "))
zinssatz = float(input("Zinssatz in %: "))
jahre = float(input("Anzahl Jahre: "))

while jahr < jahre :
    jahr += 1
    kap_ende = kap_anfang * ( 1 + zinssatz / 100 ) ** jahr
    print( "Kapital nach Jahr", jahr, kap_ende )