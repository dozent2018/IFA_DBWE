# myfunctions.py enthält nützliche Funktionsdefinitionen

import sys

def is_int(string: str) -> bool :
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

def is_float(string: str) -> bool :
    try:
        zahl = float(string)
        return True
    except ValueError:
        return False

def read_int(prompt: str) -> int :
    while is_int == False :
        try:
            zahl = int(input(prompt))
            return ist_zahl
        except ValueError:
            print("Die Eingabe ist keine ganze Zahl")

def read_float(prompt: str) -> int :
    while is_int == False :
        try:
            zahl = float(input(prompt))
            return ist_zahl
        except ValueError:
            print("Die Eingabe ist keine Fliesskommazahl")

def yes(prompt: str, answers: tuple) -> bool :
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
