"""adressbuch01.py - Erste Version. Nur die Funktion menu() und 
ein kleines Hauptprogramm sind bisher implementiert"""

def menu() -> str:
    """ Gibt das Menu mit den Auswahlmöglichkeiten auf den Bildschirm aus
    und liefert die Auswahl des Benutzers zurück"""
    auswahl = ''
    while True:
        print('(A)zeigen (N)eue Adresse (S)uchen (V)erändern (L)öschen (B)eenden')
        auswahl=input('Ihre Wahl > ').lower().strip()
        if auswahl in ('a', 's', 'n', 'l', 'v', 'b'):
            return auswahl
        else:
            print('Ungültige Eingabe')
            continue

# Das Hauptprogramm
auswahl = ''
adressen = dict()

# Die Hauptschleife des Programms. Hier wird nur menu() aufgerufen und getestet
while True :
    auswahl = menu()
    if auswahl == 'b' :
        break
    else :
        print(auswahl, ': Noch nicht implementiert')
