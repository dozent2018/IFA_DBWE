def fak_i(n: int) -> int :
    ''' Iterative Berechnung der Fakultät n!'''
    for i in range(1, n):
        n = n * i  
    return n

def fak_r(n: int) -> int :
    ''' Rekursive Berechnung der Fakultät n!'''
    if (n < 1) :
        return 1
    else:
        return n * fak_r(n - 1)

    
# Testprogramm
if __name__ == '__main__':
    import time, sys
    zahl = int(sys.argv[1])
    # Test iterative Version
    startzeit = time.perf_counter()
    f = fak_i(zahl)
    endzeit = time.perf_counter()
    t_fak_i = endzeit - startzeit
    # print(f)
    print('Laufzeit iterativ für fak({0:d}): {1:e} sek'.format(zahl, t_fak_i))
    # Test rekursive Version
    startzeit = time.perf_counter()
    f = fak_r(zahl)
    endzeit = time.perf_counter()
    t_fak_r = endzeit - startzeit
    # print(f)
    print('Laufzeit rekursiv für fak({0:d}): {1:e} sek'.format(zahl, t_fak_r))
    print('Laufzeit rekursiv / Laufzeit iterativ: {0:4.2f}'.format( t_fak_r / t_fak_i) )