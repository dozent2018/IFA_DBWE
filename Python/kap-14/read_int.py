# read_int.py demonstriert die
# Definition und Verwendung einer Funktion
def read_int(prompt) :
    while True :
        try:
            zahl = int(input(prompt))
            return zahl
        except ValueError:
            print("Die Eingabe ist keine ganze Zahl")
anzahl = read_int('Anzahl: ')
print(anzahl)
alter = read_int('Ihr Alter: ')
print(alter)

