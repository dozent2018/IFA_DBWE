from myfunctions import is_int, read_int, mittel

print('***** Test is_int() *****')
print(is_int(22))
print(is_int('Zweiundzwanzig'))

print('***** Test read_int *****')
zahl = read_int('Zahl eingeben: ')
print(zahl)

print('***** Test mittel *****')
liste = [1,2,3.0] # Summe 6, Anzahl 3, Mittelwert 2
print(mittel(liste))
liste = [1,'Hallo',2,3,'X'] # Summe 6, Anzahl 3, Mittelwert 2
print(mittel(liste))
liste = [] # Summe 0, Anzahl 0, Mittelwert 0 - Achtung: Division durch 0 muss abgefangen werden!
print(mittel(liste))