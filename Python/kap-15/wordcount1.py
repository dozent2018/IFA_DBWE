""" wordcount1.py zählt die Geamtzahl der Wörter, die in einem Text vorkommen.
Dabei werden Zeichen wie Satzzeichen, Klammern, Anführungszeichen usw. ignoriert"""

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
    """ Öffnet eine Textdatei und liefert die Zeilen der Datei
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

words = []
count = 0
unique_words = set()
in_fname = input('Dateiname: ')
lines = file_to_list(in_fname)
for line in lines :
    # Satzzeichen, spezielle Zeichen und Zahlen sollen nicht mitgezählt werden
    line = clean_string2( line, '.!?,:;"\'^"§$%&/\\\(\)+-*=`´><|[]\{\}0123456789' )
    # str.split() trennt die Wörter zwischen Leerzeichen und gibt eine Liste der Wörter zurück
    words = line.split()
    # Die Anzahl der Wörter in der Liste ist die Anzahl der Wörter in der Zeile
    count += len(words)
    
print(count, 'Wörter gezählt')

