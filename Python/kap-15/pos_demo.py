"""pos_demo.py demonstriert einen Funktionsaufruf mit der 
richtigen und der falschen Reihenfolge von Positions-Parametern"""

def doppel( liste: list, zahl: int) -> list :
    for element in liste:
        print(element * zahl)

l = [2, 3, 4]

# Aufruf mit Argumenten in der richtigen Reihenfolge
doppel( l, 2)
# Aufruf mit Argumenten in der falschen Reihenfolge
doppel( 2, l )

