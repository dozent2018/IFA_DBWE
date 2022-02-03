""" wordstat2.py ermittelt die Häufigkeit der Wörter die in einem Text vorkommen.
Dabei werden Gross / Kleinschreibung sowie Zeichen wie Satzzeichen, Klammern, 
Anführungszeichen usw. ignoriert. Die Ausgabe erfolgt soriert nach Häufigkeit"""

import sys

def clean_string1( origstr: str, rmstr: str ) -> str :
    """Entfernt aus origstr alle Zeichen, die in rmstr stehen. Verwendet str.replace()"""
    newstr = ''
    for zeichen in rmstr :
        if zeichen in origstr :
            newstr = origstr.replace(zeichen, ' ')
            origstr = newstr
    # Durch split() werden mehrfache Leerzeichen eliminiert        
    return ' '.join(newstr.split())

def clean_string2( origstr: str, rmstr: str ) -> str:
    """Entfernt aus origstr alle Zeichen, die in rmstr stehen.
    Verwendet str.maketrans() und str.translate()"""
    # Einen String aus Blanks erzeugen, der die gleiche Länge wie rmstr hat
    blankstr = len(rmstr) * ' '
    # Übersetzungstabelle für translate() erzeugen
    tr_table = str.maketrans(rmstr,blankstr)
    newstr = origstr.translate(tr_table)
    # Durch split() werden mehrfache Leerzeichen eliminiert        
    return ' '.join(newstr.split())

def file_to_list(filename: str) -> list :
    """ Öffnet eine Textdatei und liefert die lines der Datei
    als Liste von Strings zurück"""
    try:
        with open(in_fname, 'rt', encoding='utf-8-sig') as in_file :
            lines = in_file.readlines()
    except NotADirectoryError :
        print('Fehler:', in_dname, 'Verzeichnis nicht gefunden')
        return None
    except IsADirectoryError :
        print('Fehler:', in_dname, 'ist ein Verzeichnis')
        return None
    except FileNotFoundError :
        print('Fehler:', in_dname, '- Datei nicht gefunden')
        return None
    except PermissionError :
        print('Fehler:', in_dname, '- keine Berechtigung')
        return None
    else:
        return lines

in_fname = ''
lines = ''
words = []
count = 0
unique_words = dict()
statistics = []

in_fname = input('Dateiname: ')
lines = file_to_list(in_fname)
for line in lines :
    # Satzzeichen, spezielle Zeichen und Zahlen sollen nicht mitgezählt werden
    line = clean_string2( line, '.!?,:;"\'^"§$%&/\\\(\)+-*=`´«»‘’„“ø><–…•|[]\{\}0123456789' )
    # str.split() trennt die Wörter zwischen Leerzeichen und gibt eine Liste der Wörter zurück
    words = line.split()
    # Die Anzahl der Wörter in der Liste ist die Anzahl der Wörter in der Zeile
    count += len(words)
    # Neue Wörter zum Dictionary
    # hinzufügen. Kleinschreibung erzwingen
    for word in words :
        word = word.lower()
        if word not in unique_words :
            # Das Wort ist noch nicht bekannt, anlegen in Kleinschreibung
            unique_words[word] = 1
        else :
            # Das Wort ist schon bekannt, Zähler erhöhen
            unique_words[word] += 1 
    
print(count, 'Wörter gezählt')
print('Davon', len(unique_words), 'verschiedene Wörter')
for key in unique_words :
    statistics.append((unique_words[key], key))
    # print(key, unique_words[key])

for item in statistics.sorted(reverse=True) :
    print(item[0], item[1])