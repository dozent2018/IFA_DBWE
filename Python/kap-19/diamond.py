class Fahrzeug:
    def fahren(self):
        print('fahren() aus Fahrzeug')

class Motorfahrzeug(Fahrzeug):
    def fahren(self):
        print('fahren() aus Motorfahrzeug')

class Velo(Fahrzeug):
    #def fahren(self):
    #    print('fahren() aus Velo')
    pass

class Pedelec(Motorfahrzeug,Velo):
        pass

p = Pedelec()
p.fahren()