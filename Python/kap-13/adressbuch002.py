"""adressbuch.py - Zweite Version. Die Funktion create() und die Abfrage des Namens im 
Hauptprogramm wurden hinzugefügt. Anzeige der Eingaben mit pprint()"""

from pprint import pprint

def menu() -> str:
    """ Gibt das Menu mit den Auswahlmöglichkeiten auf den Bildschirm aus
    Liefert die Auswahl des Benutzers zurück"""
    auswahl = ''
    while True:
        print('(A)zeigen (N)eue Adresse (S)uchen (V)erändern (L)öschen (B)eenden')
        auswahl=input('Ihre Wahl > ').lower()
        if auswahl in ('a', 's', 'n', 'l', 'v', 'b'):
            return auswahl
        else:
            print('Ungültige Eingabe')
            continue
def read_name() -> str :
    """Fragt nach der Eingabe des Namens. Wiederholt die Aufforderung
    falls ein leerer String oder nur Leerzeichen eingegeben wurden"""
    name = ''
    while name == '' :
        # strip() entfernt überflüssige Leerzeichen aus der Eingabe
        name = input('Name    : ').strip()
    return name

def read_adr() -> dict :
    """ Fragt die einzelnen Felder für eine Anschrift ab.
    Gibt ein Dictionary mit den Adressdetails zurück"""
    adr = {'Strasse' : '', 'Nr.' : '', 'PLZ' : '', 'Ort' : ''}
    # strip() entfernt überflüssige Leerzeichen in der Eingabe
    adr['Strasse'] = input('Strasse : ').strip()
    adr['Nr.'] = input('Hausnr. : ').strip()
    adr['PLZ'] = input('PLZ     : ').strip()
    adr['Ort'] = input('Ort     : ').strip()
    return adr


# Das Hauptprogramm
auswahl = ''
adressen = dict()

# Die Hauptschleife des Programms
while True:
    auswahl = menu()
    if auswahl == 'b':
        break
    elif auswahl == 'n':
        name = ''
        # Zuerst den Namen einlesen
        name = read_name()
        # Dann die Anschriftdetails einlesen
        adr = read_adr()
        # Den Eintrag zum Adressbuch hinzufügen
        adressen[name] = adr
    elif auswahl == 'a' :
        # zum Testen wird der Eintrag ausgegeben
        pprint(adressen)
    else :
        print('Noch nicht implementiert')
        continue
