in_str = ''
while in_str != 'End':
    in_str = input('Ganze Zahl: ')
    try:
        zahl = int(in_str)
        print(zahl)
    except ValueError:
        print('Fehler:',in_str, 'ist keine ganze Zahl')



