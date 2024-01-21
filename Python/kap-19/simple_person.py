class person:
    def __init__(self, der_nachname, der_vorname):
        self.nachname = der_nachname
        self.vorname = der_vorname
    
    def hallo(self):
        print('Hallo, ich heisse',self.vorname, self.nachname)

class student(person):
    def __init__(self,der_nachname, der_vorname, mat_nr):
        # __init__() von person wird aufgerufen
        super().__init__(der_nachname, der_vorname) 
        self.matrikelnummer = mat_nr

    def hallo(self):
        super().hallo() # hallo() von person wird aufgerufen
        print('Matrikelnummer', self.matrikelnummer)

class dozent(person):
    def __init__(self,der_nachname, der_vorname, faecher ):
        # __init__() von person wird aufgerufen
        super().__init__(der_nachname, der_vorname) 
        self.unterrichtet = faecher

    def hallo(self):
        super().hallo() # hallo() von person wird aufgerufen
        print('Unterrichtet', self.unterrichtet)
