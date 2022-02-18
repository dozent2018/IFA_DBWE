# computer.py ist ein Lösungsbeispiel für Aufgabe 1 in Kapitel 16

class Computer:
    def __init__(self, inventar_nr : str = '', interfaces : list = [],
                peripherie : list =[], beschreibung : str = ''):
        self.inventar_nr = inventar_nr
        self.interfaces = interfaces
        self.beschreibung = beschreibung
        self.__running = False

    def boot(self):
        self.__running = True

    def shutdown(self):
        self.__running = False

    def ping(self):
        if self.__running :
            print('pong')

    def __str__(self) -> str:
        return "inventar_nr : {}\ninterfaces : {}\nbeschreibung : {}\nrunning: {}".format(
            self.inventar_nr, self.interfaces, self.beschreibung, self.__running)

if __name__ == '__main__':
    c1 = Computer(inventar_nr = 1234, interfaces = ['192.168.0.2'], beschreibung = 'erster Computer')
    print(c1)
    c1.boot()
    c1.ping()
    c1.shutdown()
    c1.ping