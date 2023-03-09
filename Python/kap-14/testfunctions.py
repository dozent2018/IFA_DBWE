from myfunctions import is_int, is_float, summe, mittel, read_int

print('***** Test is_int() *****')
print(is_int(22))
print(is_int('Zweiundzwanzig'))

print('***** Test is_float() *****')
print(is_float(29.687))
print(is_int('gugus'))

print('***** Test is_float() *****')
print(is_int(111.33))
print(is_int('Blabla'))


print('***** Test summe() *****')
from myfunctions import summe
print(summe())
print(summe(['gugus', 'blabla', 'quatsch']))
print(summe([]))

print('***** Test mittel() *****')
print(mittel([10, 'blabla', 40.0]))
print(mittel(['gugus', 'blabla', 'quatsch']))
print(mittel([]))

print('***** Test read_int *****')
zahl = read_int('Zahl eingeben: ')
print(zahl)
