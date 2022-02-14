# fibonacci.py berechnet die eingegebene Anzahl von Fibonacci-Zahlen
# beginnend bei 1 und gibt sie aus
grenze = int(input('Anzahl: '))
a = 0
b = 1
while a <= grenze + 1:
    a,b = b,a+b
    print(a)