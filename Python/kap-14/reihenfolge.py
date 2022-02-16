# reihenfolge.py demonstriert eine falsche Reihenfolge von 
# Funtionsdefinition und Funktionsaufruf

def summe(wert1, wert2):
    return wert1 + wert2


print(summe(10, 20))
print(differenz(10, 20))

def differenz(wert1, wert2):
    return wert1 - wert2


