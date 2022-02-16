def maximum(wert1, wert2) :
    if wert1 > wert2:
        return wert1;
    else:
        return wert2

print(maximum(1, 2))
print(maximum(2, 1))
print(maximum(1,1))      

def ist_zahl(string) :
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

def read_int(prompt) :
    while ist_zahl = False :
        try:
            zahl = int(input(prompt))
            return ist_zahl
        except ValueError:
            print("Die Eingabe ist keine ganze Zahl")

anzahl = read_int('Anzahl: ')
print(anzahl)
alter = read_int('Ihr Alter: ')
print(alter)