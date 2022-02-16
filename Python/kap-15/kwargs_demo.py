"""kwargs_demo.py demonstriert den Aufruf einer
Funktion mit Schlüsselwort-Argumenten"""

def mult_list( liste: list, zahl: int) -> list :
    """ Multipliziert jedes Element in
    liste mit zahl """
    for element in liste:
        print(element * zahl)

l = [2, 3, 4]

# Aufruf mit den Namen der Parameter
mult_list( zahl=2, liste=l )

