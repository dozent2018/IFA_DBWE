"""adressbuch02.py - Die Funktionen read_name() und read_adr()
sind jetzt implementiert"""

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

def read_name() -> str :
    """Fragt nach der Eingabe des Namens. Wiederholt die Aufforderung,
    falls ein leerer String oder nur Leerzeichen eingegeben wurden"""
    name = ''
    while name == '' :
        # strip() entfernt überflüssige Leerzeichen aus der Eingabe
        name = input('Name    : ').strip()
    return name

def read_adr() -> dict :
    """ Fragt die einzelnen Felder für eine Anschrift ab.
    Gbibt ein Dictionary mit den Adressdetails zurück"""
    strasse = input('Strasse : ').strip()
    nr = input('Hausnr. : ').strip()
    plz = input('PLZ     : ').strip()
    ort = input('Ort     : ').strip()
    return {'Strasse' : strasse, 'Nr.' : nr, 'PLZ' : plz, 'Ort' : ort}

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
