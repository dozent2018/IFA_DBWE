/* Beispiele Kap 7.2 */
CREATE VIEW v_standorte AS (
  SELECT standort_id, name, strasse, nr, plz, ort
  FROM standort s JOIN adresse a
  ON s.adresse = a.adresse_id
);

SELECT * FROM v_standorte;

INSERT INTO standort (standort_id, name, adresse)
VALUES (NULL, 'Basel', 14);

/* Beispiele Kap 7.3 bis 7.4*/
CREATE VIEW v_klassen (
  klasse,
  studenten )
  AS SELECT k.bezeichnung, count(*)          
  FROM klasse k JOIN student s ON s.klasse = k.klasse_id   
  GROUP BY k.bezeichnung;
  
  CREATE VIEW v_ma_liste (
	name,
	funktion,
	email,
	telefon )
  AS SELECT name, funktion, email, telefon FROM mitarbeiter;
  
CREATE VIEW v_raum (
  standort,
  raum,
  belegung )
AS SELECT s.name Standort, r.bezeichnung Raum, count(*) Belegungen
  FROM standort s JOIN raum r ON s.standort_id = r.standort
       JOIN lehrveranstaltung l ON l.raum = r.raum_id
  GROUP BY s.name, r.bezeichnung
  ORDER BY Standort, Belegungen DESC;
  
describe v_standorte;
show create view v_standorte;
  
/* Beispiele Kap 7.5 */
CREATE VIEW v_ma_liste (
	name,
	funktion,
	email,
	telefon )
AS SELECT name, funktion, email, telefon FROM mitarbeiter;
  
SELECT * FROM v_ma_liste WHERE name = 'Jörg Graf';
  
UPDATE v_ma_liste SET telefon = '058 211 222' WHERE name = 'Jörg Graf';
  
SELECT telefon FROM mitarbeiter WHERE name = 'Jörg Graf';
  
UPDATE v_standorte SET name = 'Basel 1' WHERE name = 'Basel';
  
INSERT INTO v_standorte ( name, strasse, nr, plz, ort)
VALUES ('Neu', 'Neustrasse', '1', '1111', 'Neustadt');
  

  
  