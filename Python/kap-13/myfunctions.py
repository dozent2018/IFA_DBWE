# myfunctions.py enthält Lösungsvorschläge zu den Aufgaben in Kap. 13

# Aufgabe 1
def is_int(string: str) -> bool :
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

# Aufgabe 2
def is_float(string: str) -> bool :
    try:
        zahl = float(string)
        return True
    except ValueError:
        return False

# Aufgabe 3
def summe(zahlen: list) -> float :
    sum = 0.0
    for element in zahlen :
        if is_float(element) :
            sum = sum + float(element)
    return sum

# Aufgabe 4
def mittel( zahlenliste: list ) -> float :
    return summe(zahlenliste) / len(zahlenliste)

# Aufgabe 5
def read_int(prompt: str) -> int :
    while is_int == False :
        try:
            return int(input(prompt))
        except ValueError:
            print("Die Eingabe ist keine ganze Zahl")

# Aufgabe 6
def read_float(prompt: str) -> int :
    while is_int == False :
        try:
            return float(input(prompt))
        except ValueError:
            print("Die Eingabe ist keine Fliesskommazahl")

# Aufgabe 7
def yes(prompt: str, antworten: list) -> bool :
    antwort = input(prompt).strip()
    if antwort in antworten :
        return True
    else :
        return False

# Aufgabe 8
def is_prime(x: int) -> bool: 
    # Einfache Version:
    # Für alle Teiler von 2 bis x-1 ausprobieren, 
    # ob x durch Teiler ohne Rest teilbar ist. 
    # Läuft für grosse Zahlen sehr lange
    if x == 2 : return True
    for teiler in range( 2, x ):
        if x % teiler == 0:
            # Die Zahl ist ohne Rest durch eine andere Zahl teilbar 
            # -> keine Primzahl, es ist nicht nowendig, weiter zu probieren
            return False
    return True

# Aufgabe 9
def ggt(x: int, y: int) -> int :
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x

# Aufgabe 10
def kgv(x: int, y: int) -> int :
    return ggt(x) * x

# Aufgabe 11
def prime_factors(x: int) -> list :
    # Einfache Version:
    # Für alle Teiler von 2 bis x ausprobieren, 
    # ob x durch Teiler ohne Rest teilbar ist. 
    # Läuft für grosse Zahlen sehr lange
    factors = []
    for factor in range( 2, x + 1 ) :
        while x % factor == 0:
            factors.append(factor)
            x = x // factor     
    return factors