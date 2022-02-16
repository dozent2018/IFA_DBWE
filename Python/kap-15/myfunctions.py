""" Eine Sammlung von Funktionen für Dateneingaben und
Die Validierung von Eingabewerten"""

def is_int(string: str) -> bool :
    """Prüft, ob das Argument string in ein int umgewandelt werden kann.
    Bei Erfolg ist der Rückgabewert True, ansonsten False"""
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

def is_float(string: str) -> bool :
    """Prüft, ob das Argument string in ein float umgewandelt werden kann.
    Bei Erfolg ist der Rückgabewert True, ansonsten False"""
    try:
        zahl = float(string)
        return True
    except ValueError:
        return False

def read_int(prompt: str) -> int :
    """Fragt solange nach der Eingabe einer ganzen Zahl, bis eine eingegeben wird.
    Das Argument prompt wird dabei als Eingabeaufforderung ausgegeben."""
    while True :
        eingabe = (input(prompt))
        if is_int(eingabe):
            return int(zahl)
        else:
            print("Die Eingabe ist keine ganze Zahl")
            continue
        

def read_float(prompt: str) -> float :
    """Fragt solange nach der Eingabe einer Fliesskommazahl, bis eine eingegeben wird.
    Das Argument prompt wird dabei als Eingabeaufforderung ausgegeben.
    Rückgabewert ist ein Objekt vom Typ float"""
    while True :
        eingabe = (input(prompt))
        if is_float(eingabe):
            return float(zahl)
        else:
            print("Die Eingabe ist keine Zahl")
            continue

def summe(zahlen: list) -> float :
    ergebnis = 0
    for zahl in zahlen:
        if is_float(zahl):
            ergebnis += zahl
    return ergebnis

def yes(prompt: str) -> bool :
    """Fragt solange nach der Bejahung einer Frage, bis entweder 
    'Yes', 'No', 'yes', 'no', 'Y', 'y', 'N' oder 'n' eingegeben wird
    Das Argument prompt wird dabei als Eingabeaufforderung ausgegeben.
    Rückgabewert ist True bei Bejahung, False bei Verneinung"""
    while True :
        antwort = input(prompt)
        if antwort in ('Y', 'y', 'Yes', 'yes') :
            return True
        elif antwort in ('N', 'n', 'No', 'no') :
            return False
        else :
            continue
