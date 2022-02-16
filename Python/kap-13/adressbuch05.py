"""adressbuch05.py -  Die Funktionen menu(), create(), show(), showall(), 
find(), update() und delete() sowie das Hauptprogramm sind implementiert"""

import csv

def read_file(fname: str) -> None :
    adressen = {}
    with open(fname, 'r', encoding='utf-8-sig') as in_file :
        reader_obj = csv.reader(in_file, dialect = 'excel', delimiter = ';')
        for line in reader_obj :
            adressen[line[0]] = { 'Strasse' : line[1], 'Nr.' : line[2], 'PLZ' : line[3], 'Ort' : line[4] }
    return(adressen)

def menu() -> str:
    """ Gibt das Menu mit den Auswahlmöglichkeiten auf den Bildschirm aus
    Liefert die Auswahl des Benutzers zurück"""
    auswahl = ''
    while True:
        print('(A)lle anzeigen (N)eue Adresse (S)uchen (V)erändern (L)öschen (B)eenden')
        auswahl=input('Ihre Wahl > ').strip()
        if auswahl.lower() in ('a', 's', 'n', 'l', 'v', 'b'):
            return auswahl
        else:
            print('Ungültige Eingabe:', auswahl)
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

def show( name:str, adr: dict ) -> None :
    """ Zeigt einen Eintrag an """
    try:
        s = ( name + ', ' + adr['Strasse'] + ' ' + adr['Nr.'] + 
                ', ' + adr['PLZ'] + ' ' + adr['Ort'] )
        print(s)
    except KeyError:
        pass

def showlist(nlist: list) -> None :
    """ Zeigt alle Einträge für die Namen in der Liste an """
    for name in nlist :
        show(name, adressen[name])

def find(s: str) -> list :
    """ Findet Adressen, deren Namen einen String enthalten.
    Gibt eine Liste mit den gefundenen Namen und Adressen zurück"""
    gefunden = []
    for name in adressen.keys() :
        if s in name:
            gefunden.append(name)
    return gefunden

def update( old_dict: dict ) -> dict:
    """Ein bestehendes Dictionary old_dict wird übergeben und die Schlüssel/Wert-Paare 
    werden nacheinander angezeigt. Der Benutzer kann bestehende Werte übernehmen oder 
    neue Werte setzen. Gibt ein neues Dictionary new_dict mit dem allenfalls geänderten 
    Inhalt zurück. """
    new_dict = dict()
    print('Ändern: neuen Wert eingeben, Übernehmen: Return')
    for key in old_dict.keys() :
        old_val = old_dict[key]
        prompt = key + ': ' + '(' + old_val + ') neu: '
        new_val = input(prompt).strip()
        # Um ein Detail zu belassen, gibt der Benutzer nichts ein. 
        if new_val != old_val and new_val != '' :
            new_dict[key] = new_val
        else :
            new_dict[key] = old_val
    return new_dict

def yes(prompt: str, answers: tuple) -> bool :
    """ Erfragt eine Bestätigung vom Benutzer. Ausgegeben wird
    der Prompt. Wenn Die Eingabe des Benutzer einem String aus dem 
    Tupel inputs entspricht, wird True zurückgegeben, ansonsten False"""
    answer = input(prompt).strip()
    if answer in answers :
        return True
    else :
        return False

# Das Hauptprogramm
auswahl = ''
# adressen = dict()
adressen = read_file('Adressen.csv')
while True:
    auswahl = menu()
    if auswahl == 'b':
        break
    elif auswahl == 'n':
        name = read_name()
        # Überprüfung, ob name schon existiert
        if name in adressen :
            print ('Der Eintrag existiert schon:')
            show(name, adressen[name])
            if not yes('Überschreiben (J/N) ?', ('J','j','Ja','ja') ) :
                continue
        adr = read_adr()
        adressen[name] = adr
    elif auswahl == 'a' :
        nlist = adressen.keys()
        showlist(nlist)
    elif auswahl == 's' :
        such_str = read_name()
        liste = find(such_str)
        showlist(liste)
    elif auswahl == 'v' :
        name = input('Ändern von: ')
        if name in adressen.keys() :
            new_adr = update(adressen[name])
            show(name, new_adr)
            if yes('Änderung übernehmen (J/N)? ', ('J','j','Ja','ja')) :
                adressen[name] = new_adr
        else :
            print(name, ': nicht gefunden')
    elif auswahl == 'l' :
        name = input('Löschen von: ')
        if name in adressen.keys() :
            show(name, adressen[name])
            if yes('Wirklich löschen (J/N)? ', ('J','j','Ja','ja') ) :
                del adressen[name]
        else :
            print(name, ': nicht gefunden')
