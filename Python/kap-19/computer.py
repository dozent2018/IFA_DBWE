# computer.py ist ein Lösungsbeispiel für Aufgabe 1 in Kapitel 19
from datetime import date, datetime
from time import strftime
class Computer:
    def __init__(self, inventar_nr : str = '', interfaces : list = [],
                peripherie : list =[], beschreibung : str = ''):
        self.inventar_nr = inventar_nr
        self.interfaces = interfaces
        self.peripherie = peripherie
        self.beschreibung = beschreibung
        self.__running = False

    @property
    def running(self):
        return self.__running

    def boot(self):
        self.__running = True

    def shutdown(self):
        self.__running = False

    def backup(self):
        if self.running :
            print('Backup completed on ' + datetime.strftime(datetime.today(), '%d.%m.%y %H:%M'))
        else :
            print('Device must be running for backup')

    def ping(self):
        if self.running :
            print('pong')

    def __str__(self) -> str:
        return "inventar_nr : {}\ninterfaces : {}\nperipherie: {}\nbeschreibung : {}\nrunning: {}".format(
            self.inventar_nr, self.interfaces, self.peripherie, self.beschreibung, self.running)

class Server(Computer):
        def __init__(self, inventar_nr : str, hostname : str = '', interfaces : list = [],
                peripherie : list =[], beschreibung : str = '' ):
            super().__init__(inventar_nr, interfaces, peripherie, beschreibung)
            self.hostname = hostname

        def __str__(self) -> str:
            return "inventar_nr : {}\nhostname: {}\ninterfaces : {}\nperipherie: {}\nbeschreibung : {}\nrunning: {}".format(
                    self.inventar_nr, self.hostname, self.interfaces, self.peripherie, self.beschreibung, self.running)

        def connect(self):
            if self.__running == True:
                print('Connected to', self.hostname)

class Laptop(Computer):
        def __init__(self, inventar_nr : str, interfaces : list = [],
                peripherie : list =[], beschreibung : str = '' ):
        super().__init__(inventar_nr, interfaces, peripherie, beschreibung)
        self.__batterieladung = 100
        self.__start_time = datetime.today

        @property
        def batterieladung(self):
            time_running = datetime.today() - self.start_time
            batterieladung

        def aufklappen(self):
            self.__running = True

        def zuklappen(self):
            self.running = False


if __name__ == '__main__':
    c1 = Computer(inventar_nr = 1234, interfaces = ['192.168.0.2'], peripherie = ['USB-Stick'], beschreibung = 'erster Computer')
    print(c1)
    c1.backup()
    c1.boot()
    c1.backup()
    c1.ping()
    c1.shutdown()
    c1.ping

    s1 = Server(inventar_nr = 1235, hostname = 'db-serv1', interfaces = ['192.168.0.3'], peripherie = ['Super Storage Array'], beschreibung = 'erster Server')
    print(s1)