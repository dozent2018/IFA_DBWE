"""adressbuch.py - Erste Version. Nur die Funktionen menu(), create() und 
ein kleines Hauptprogramm sind bisher implementiert"""

from pprint import pprint

def menu() -> str:
    """ Gibt das Menu mit den Auswahlmöglichkeiten auf den Bildschirm aus
    Liefert die Auswahl des Benutzers zurück"""
    auswahl = ''
    while True:
        print('(A)zeigen (S)uchen (N)eue Adresse (L)öschen (V)erändern (B)eenden')
        auswahl=input('Ihre Wahl > ').lower()
        if auswahl in ('a', 's', 'n', 'l', 'v', 'b'):
            return auswahl
        else:
            continue

def create() -> list :
    """ Fragt die einzelnen Felder für einen Eintrag ab.
    Gbibt eine Liste mit dem Namen und einem Dictionary 
    mit den Adressdetails zurück"""  
    name =''
    # Ein Dictionary mit Schlüsseln und leeren Werten
    adresse = {'Strasse' : '', 'Nr.' : '', 'PLZ' : '', 'Ort' : ''}
    # Ein Name muss angegeben werden
    while name == '' :
        # strip() entfernt überflüssige Leerzeichen bei der Eingabe
        name = input('Name: ').strip()
    for key in adresse.keys() :
        adresse[key] = input(key + ': ').strip()
    return [ name, adresse ]

def show( name: str, adr: dict, form: str ) -> None :
    """ Zeigt eine Adresse formatiert an """
    formatstr = '{0:15s} {1:15s} {2:4s} {3:4s} {4:20s}'
    ueberschrift = formatstr.format('Name', 'Strasse', 'Nr.', 'PLZ', 'Ort' )
    ausgabe = form.format(name, adr['Strasse'], adr['Nr.'], adr['PLZ'], adr['Ort'] )
    print(ausgabe)

def find( name:str, adressen: dict ) -> dict :
    """ Sucht einen Schlüssel in der Adressen-Sammlung und gibt
    bei Erfolg das Dictionary mit der Adresse zurück, bei
    Misserfolg ein leeres Dictionary """
    if name in adressen.keys():
        adresse = adressen[name]
    else: 
        adresse = None
    return adresse

def update( name: str, adressen: dict ) -> dict :
    """ Sucht einen Schlüssel in der Adressen-Sammlung und
    zeigt den Derzeitigen Inhalt an. Erlaubt dem Benutzer 
    die einzelnen Bestandteile der Adresse zu überschreiben
    und gibt das allenfalls veränderte Dictionary zurück"""
    adresse = find( name, adressen)
    if adresse != None :
        for key in adresse.keys() :
            eingabe = input(key + 'bisher:' + adresse[key]).strip()
            if eingabe != '' :
                adresse[key] = eingabe
        return adresse
    else :
        print(name, 'nicht gefunden')
        return None


# Das Hauptprogramm
auswahl = ''
adressen = dict()

# Die Hauptschleife des Programms
while auswahl != 'b':
    auswahl = menu()
    if auswahl == 'n':
        eintrag = create()
        adressen[eintrag[0]] = eintrag[1]
        # zum Testen wird der Eintrag ausgegeben
        pprint(adressen)
    elif auswahl == 'a' :
        # Alle Adressen anzeigen
        print(ueberschrift)
        for name in adressen.keys() :
            show(name, adressen[name], formatstr)
    elif auswahl == 's':
        name = input('Name >').strip()
        if find(name, adressen) != None :
            show(name, adressen[name], formatstr)
        else : 
            print (name, 'nicht gefunden')
    elif auswahl == 'v' :
        name = input('Name >').strip()
        adressen[name] = update(name, adressen)
    elif auswahl == 'b' :
        break
    else :
        print('Noch nicht implementiert')
        continue
