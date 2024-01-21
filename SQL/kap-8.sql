# Kap 8.2 Beispiel Benutzer-Account anlegen
CREATE USER 'jochen'@'localhost' IDENTIFIED BY 'd8St5g38m';

# Kap. 8.2 Passwort ändern
ALTER USER 'jochen'@'localhost' IDENTIFIED BY 'n33s0w94d';

# Kap 8.3 Beispiel alle Berechtigungen für alle Objekte einer Datenbank
GRANT ALL ON jochen.* TO jochen@localhost;
FLUSH PRIVILEGES;

# Kap 8.3 Beispiel nur SELECT für alle Objekte der Datenbank beispiele
GRANT SELECT ON beispiele.* TO jochen@localhost;
FLUSH PRIVILEGES;

# Kap. 8.3 Beispiel UPDATE nur für eine Tabelle erlauben
GRANT UPDATE ON beispiele.student TO jochen@localhost;
FLUSH PRIVILEGES;

# Kap. 8.3 Beispiel REVOKE
REVOKE UPDATE ON beispiele.student FROM jochen@localhost;

# Kap 8.4 Rolle erzeugen
CREATE ROLE 'simple'@'localhost';

# Kap. 8.4 Berechtigung an Rolle zuweisen
GRANT SELECT ON beispiele.* TO simple@localhost;

CREATE USER 'paula'@'localhost' IDENTIFIED BY 'PaulasGeheimnis';

GRANT 'simple'@'localhost' TO 'paula'@'localhost';

REVOKE 'simple'@'localhost' FROM 'paula'@'localhost';