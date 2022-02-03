# zinseszins1.py berechnet für einen Kapitalbetrag,
# einen festen Zinssatz in % und eine Laufzeit in Jahren
# den erreichten Endbetrag
print("Kapitalbetrag nach Verzinsung über eine Anzahl Jahre")
kap_anfang = float(input("Anfangskapital: "))
zinssatz = float(input("Zinssatz in %: "))
jahre = float(input("Anzahl Jahre: "))
kap_ende = kap_anfang * ( 1 + zinssatz / 100 ) ** jahre
print( "Kapital nach", jahre, "Jahren", kap_ende )