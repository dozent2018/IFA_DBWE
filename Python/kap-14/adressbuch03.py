"""adressbuch.py - Erste Version. Nur die Funktionen menu(), create() und 
ein kleines Hauptprogramm sind bisher implementiert"""

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
    Gbibt eine Liste mit dem Namen und einem Dictionary 
    mit den Adressdetails zurück"""
    strasse = input('Strasse : ').strip()
    nr = input('Hausnr. : ').strip()
    plz = input('PLZ     : ').strip()
    ort = input('Ort     : ').strip()

    return {'Strasse' : strasse, 'Nr.' : nr, 'PLZ' : plz, 'Ort' : ort}


# Das Hauptprogramm
auswahl = ''
adressen = dict()

# Die Hauptschleife des Programms
while True:
    auswahl = menu()
    if auswahl == 'b':
        break
    elif auswahl == 'n':
        name = read_name()
        # Überprüfung, ob name schon existiert
        if name in adressen :
            antwort = input(name + ' existiert schon. Überschreiben (J/N) ?')
            if antwort.lower() != 'j' :
                continue
        # Ansonsten restliche Informationen einlesen und 
        # den Eintrag hinzufügen oder überschreiben
        adr = read_adr()
        adressen[name] = adr
    elif auswahl == 'a' :
        # zum Testen wird der Eintrag mit pprint ausgegeben
        pprint(adressen)
    else :
        print('Noch nicht implementiert')
        continue
