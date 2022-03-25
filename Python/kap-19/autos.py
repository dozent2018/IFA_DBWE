# autos.py demonstriert Klassen

class Auto:
    """ Die Basisklasse aller Autos """
    def __init__(self, kennz, tank_groesse=50.0, verbrauch_auf_100=8.0):
        """ wird immer dann ausgeführt, wenn ein neues Objekt
        dieser Klasse erzeugt wird. Das Objekt hat zu diesem
        Zeitpunkt noch keinen Namen. Deshalb muss in der
        Klassendefinition der Plathalter .self verwendet werden
        Für tank_groesse und verbrauch sind Default-Werte angegeben.
        Sie kommen zum Einsatz, falls beim Erzeugen eines Auto-Objekts
        keine Angaben gemacht werden. Parameter mit Default-Werten
        kommen immer am Ende der Parameterliste.
        """
        self.kennzeichen = kennz
        self.tank_groesse = tank_groesse
        self.km_stand = 0.0     # Ein neues Auto hat den Kilometerstand 0
        self.tank_inhalt = 0.0  # Ein neues Auto hat den Tankinhalt 0
        self.verbrauch_pro_km = verbrauch_auf_100 / 100

    def tanken(self, liter):
        """Das Auto tankt so viele Liter, wie in den Tank passen"""
        platz_im_tank = self.tank_groesse - self.tank_inhalt
        if liter <= platz_im_tank:
            self.tank_inhalt += liter
        else:
            self.tank_inhalt += platz_im_tank

    def volltanken(self):
        """Vereinfacht das Tanken"""
        self.tank_inhalt = self.tank_groesse

    def fahren(self, km):
        """Das Auto fährt so weit, wie die Tankfüllung und er Verbrauch hergeben"""
        self.reichweite = self.tank_inhalt / self.verbrauch_pro_km
        if km <= self.reichweite:
            self.km_stand += km
            self.tank_inhalt = self.tank_inhalt - km * self.verbrauch_pro_km
        else:
            self.km_stand += self.reichweite
            self.tank_inhalt = 0.0

    def __repr__(self):
        """Ermöglicht die einfache Ausgabe der Informationen
        für ein Auto-Objekt"""
        return 'Auto: {} km: {:.1f} tank_inhalt: {:.1f}'.format(
        self.kennzeichen, self.km_stand, self.tank_inhalt)

class Cabrio(Auto):
    """wenn eine Klasse zuächst keinen anderen code hat, kann man provisorisch
    erst einmal 'pass' schreiben. Das ist notwendig, weil nach : mindestens
    eine Zeile Code stehen muss"""
    pass

class Transporter(Auto):
    """Die Klasse Transporter ist von Auto abgeleitet.
       Zusätzlich hat sie das Attribut nutzlast"""
    def __init__(self, kennz, nutzlast, tank_groesse=80.0, verbrauch=12.0):
        """hier wird die __init__() Methode der Klasse Auto aufgerufen"""
        super().__init__(kennz, tank_groesse, verbrauch)
        self.nutzlast = nutzlast

    def beladen(self, kg):
        """Die methode beladen() erweitert die Klasse Auto.
        Damit kann Nutzlast hinzugefügt werden"""
        nutzlast += kg

    def entladen(self, kg):
        """Die methode entladen() erweitert die Klasse Auto
        Damit kann Nutzlast vermindert werden"""
        nutzlast -= kg

    def __repr__(self):
        """Die Methode __repr__() überschreibt __repr__() aus der Klasse Auto"""
        return 'Transporter: {} km: {:.1f} tank_inhalt: {:.1f} nutzlast: {}'.format(
        self.kennzeichen, self.km_stand, self.tank_inhalt, self.nutzlast)