fibdict = {0:0, 1:1}

def fib_m(n: int) -> int :
    '''Rekursive Berechnung der Fibonacci-Reihe mit merken bereits
    berechneter Werte im Dictionary'''
    if n not in fibdict:
        fibdict[n] = fib_m(n-1) + fib_m(n-2)
    return fibdict[n]

def fib_i(n: int) -> int :
    '''Iterative Berechnung der Fibonacci-Reihe'''
    x, y = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        x, y = y, x + y
    return x

def fib_r(n: int) -> int :
    '''Rekursive Berechnung der Fibonacci-Reihe'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)

    
# Testprogramm
if __name__ == '__main__':
    import time, sys
    zahl = int(sys.argv[1])
    # Test iterative Version
    startzeit = time.perf_counter()
    f = fib_i(zahl)
    endzeit = time.perf_counter()
    t_fib_i = endzeit - startzeit
    print('Laufzeit iterativ für fib({0:d}): {1:e} sek'.format(zahl, t_fib_i))
    # Test rekursive Version
    #startzeit = time.perf_counter()
    #f = fib_r(zahl)
    #endzeit = time.perf_counter()
    #t_fib_r = endzeit - startzeit
    # Test Version mit gemerkten Ergebnissen
    startzeit = time.perf_counter()
    f = fib_m(zahl)
    endzeit = time.perf_counter()
    t_fib_m = endzeit - startzeit
    # print(f)
    #print('Laufzeit rekursiv für fib({0:d}): {1:e} sek'.format(zahl, t_fib_r))
    print('Laufzeit rekursiv mit gemerkten Werten für fib({0:d}): {1:e} sek'.format(zahl, t_fib_m))
    #print('Laufzeit rekursiv / Laufzeit iterativ: {0:4.2f}'.format( t_fib_r / t_fib_i) )
    print('Laufzeit rekursiv mit gemerkten Werten / Laufzeit iterativ: {0:4.2f}'.format( t_fib_m / t_fib_i) )
    #print(fibdict)