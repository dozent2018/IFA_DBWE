# myfunctions.py enthält nützliche Funktionsdefinitionen

import sys

def is_int(string: str) -> bool :
    """ Prüfung, ob ein String in int umgewandelt werden kann"""
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

def is_float(string: str) -> bool :
    """ Prüfung, ob ein String in int umgewandelt werden kann"""
    try:
        zahl = float(string)
        return True
    except ValueError:
        return False

def read_int(prompt: str) -> int :
    """ Einlesen Input, bis der Benutzer eine ganze Zahl eingegeben hat"""
    instring = input(prompt)
    while not is_int(instring) :
        instring = input(prompt)
    zahl = int(instring)
    return zahl

def summe(l: list) -> float:
    """Summe von Zahlen in einer Liste. Element überspringen, falls es keine Zahl ist"""
    summe = 0
    #Liste l in einer for-schleife durchlaufen
    for element in l:
        # Prüfen, ob das element in float umgewandelt werden kann
        if is_float(element):
            summe = summe + element
    return (summe)


def mittel(l: list) -> float:
    """Mittelwert von Zahlen in einer Liste. Überspringen, falls keine Zahl"""
    summe = 0
    anzahl = 0
    #Liste l in einer for-schleife durchlaufen
    for element in l:
        # Prüfen, ob das element in float umgewandelt werden kann
        if is_float(element):
            summe = summe + element
            anzahl = anzahl + 1
    
    if anzahl == 0:
        return 0.0
    return (summe / anzahl)

def yes(prompt: str, answers: tuple) -> bool :
    """Abfrage einer Eingabe. Die Eingabe muss im Tupel answers enthalten sein"""
    answer = input(prompt).strip()
    if answer in answers :
        return True
    else :
        return False

def menu(info: str, prompt: str, choices: str) -> str:
    """ Gibt das Menu mit Auswahlmöglichkeiten auf den Bildschirm aus.
    Angezeigt wird der Inhalt von info und einen prompt für die Benutzereingabe
    Zur Auswahl stehen alle einzelnen Zeichen, die in choices enthalten sind.
    Liefert die Auswahl des Benutzers zurück. Wiederholt die Abfrage, solange
    bis eine gültige Eingabe erfolgt"""
    auswahl = ''
    while True:
        print(info)
        choice=input(prompt + ' > ').lower()
        if choice in list(choices) :
            return choice
        else:
            print('Ungültige Eingabe:', choice)
            continue
