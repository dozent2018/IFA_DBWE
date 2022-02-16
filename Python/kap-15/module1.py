def func1():
    return('Ergebnis von func1')
    
if __name__ == '__main__':
    print('module1.py wurde direkt gestartet')
    print(func1())
else:
    print(__name__, 'wurde importiert')