"""adressbuch07.py -  Wie adressbuch06.py 
aber mit zusätzlicher Abfrage if __name == '__main__': """

import csv, os, pprint

def choose_file(path: str, ext: str) -> str :
    choice = ''
    file_list = os.listdir(path)
    for file_name in file_list:
        if file_name.endswith(ext):
            print(file_name)
    choice = input("Geben Sie den Dateinamen ein: ")
    return choice

def read_csv_data(file_name: str) -> dict :
    """Liest die CSV-Datei mit dem Namen file_name und liefert ein Dictionary mit 
    Einträgen oder ein leeres Dictionary zurück"""
    adressen = {}
    try :
        with open(file_name, 'r', encoding='utf-8-sig') as in_file :
            reader_obj = csv.reader(in_file, dialect = 'excel', delimiter = ';')
            for zeile in reader_obj :
                adressen[zeile[0]] = { 'Strasse' : zeile[1], 'Nr.' : zeile[2], 'PLZ' : zeile[3], 'Ort' : zeile[4] }
        return(adressen)
    except FileNotFoundError :
        print('Datei', file_name, ': nicht gefunden' )
    except PermissionError :
        print('Datei', file_name, ': keine Berechtigung' )
    except IsADirectoryError :
        print(file_name, ': ist ein Verzeichnis' )
    return {}

def write_csv_data(file_name: str, adressen: dict) -> bool :
    """Schreibt den Inhalt des Directory adressen in eine CSV-Datei mit dem Namen file_name. Die Datei 
    wird dabei angelegt oder überschrieben, wenn sie bereits existiert"""
    zeilen = to_list(adressen)
    try:
        with open(file_name, 'w', encoding='utf-8-sig') as out_file :
            writer_obj = csv.writer(out_file, dialect = 'excel', delimiter = ';')
            for zeile in zeilen :
                writer_obj.writerow(zeile)
        return(True)
    except FileNotFoundError :
        print('Datei', file_name, ': nicht gefunden' )
    except PermissionError :
        print('Datei', file_name, ': keine Berechtigung' )
    except IsADirectoryError :
        print(file_name, ': ist ein Verzeichnis' )
    return False

def to_list(adressen: dict ) -> list :
    """Bekommt das adressen-Dictionary übergeben und wandelt es in eine Liste von
    Listen um. Jede Teilliste enthält einen Eintrag mit Namen und Adresse"""
    zeilen = []
    for name, adresse in adressen.items() :
        zeile = [name]
        zeile += list(adresse.values())
        zeilen.append(zeile)
    return zeilen

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
    print('Ändern: neuen Wert eingeben. Alten Wert Übernehmen: Return')
    for key, old_val in old_dict.items() :
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
if __name__ == '__main__':
    adressen = dict()
    if yes('Daten aus CSV-Datei übernehmen (J/N)? ', ('J','j','Ja','ja')) :
        file_name = choose_file('.', '.csv')
        if file_name != '' :
            adressen = read_csv_data(file_name)

    auswahl = ''
    geaendert = False
    while True:
        auswahl = menu()
        if auswahl == 'b':
            if geaendert:
                print('Sie haben Änderungen gemacht')
                if yes('Änderungen speichern (J/N)? ', ('J','j','Ja','ja')) :
                    file_name = choose_file('.', '.csv')
                    if file_name == '':
                        file_name = 'Adressbuch.csv'
                    write_csv_data(file_name, adressen)
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
            geaendert = True
        elif auswahl == 'a' :
            name_list = adressen.keys()
            showlist(name_list)
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
                geaendert = True
            else :
                print(name, ': nicht gefunden')
        elif auswahl == 'l' :
            name = input('Löschen von: ')
            if name in adressen.keys() :
                show(name, adressen[name])
                if yes('Wirklich löschen (J/N)? ', ('J','j','Ja','ja') ) :
                    del adressen[name]
                    geaendert = True
            else :
                print(name, ': nicht gefunden')
