/* Code-Beispiele für das Kapitel Daten verknüpfen */

/* Anlegen der Tabelle Pruefung mit Fremdschlüsselspalten */
CREATE TABLE pruefung (
  teilnehmer    INTEGER NOT NULL,
  pruefungsfach INTEGER NOT NULL,
  note          DECIMAL(2,1) NOT NULL,
  pruefung_am   DATE NOT NULL,
  FOREIGN KEY (teilnehmer) REFERENCES student(student_id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (pruefungsfach) REFERENCES fach(fach_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

/* Einfügen von zwei Zeilen */
INSERT INTO pruefung 
  (teilnehmer, pruefungsfach, pruefung_am, note)
VALUES
  (1,1,'2021-09-27', 4.5),
  (5,1,'2021-09-27', 4.0)
;

/* Überprüfung */
SELECT * FROM pruefung;

/* Einfügen einer Zeile mit ungültigem Fach */
INSERT INTO pruefung
  (teilnehmer, pruefungsfach, pruefung_am, note)
VALUES
  (1,7777, '2021-09-27', 4.5)
;

/* Versuch, die Studentin mit der id 1 zu löschen */
DELETE from student WHERE student_id = 1;

/* Ändern einer Fach-ID von 1 auf 9 */
UPDATE fach SET fach_id = 9 WHERE fach_id = 1;

/* Prüfung, ob ON UPDATE CASCADE funktioniert hat */
SELECT * FROM pruefung;

/* Kap  4.3.1 SELECT mit JOIN */
SELECT student.vorname, 
       student.name, 
       pruefung.pruefung_am, 
       fach.name,
       pruefung.note
FROM   pruefung 
       JOIN student ON pruefung.teilnehmer = student.student_id
       JOIN fach ON pruefung.pruefungsfach = fach.fach_id;
     
       
/* Kap. 4.3.4 Aufgabe 1 */
SELECT s.name, s.email
FROM student s JOIN klasse k ON s.klasse = k.klasse_id
WHERE k.bezeichnung = 'HFSNT.SG.2';

/* Kap. 4.3.4 Aufgabe 2 */
SELECT r.bezeichnung, r.kapazitaet
FROM raum r JOIN standort s ON r.standort = s.standort_id
WHERE s.name = 'Zürich 1';

/* Kap. 4.3.4 Aufgabe 3 */
SELECT s.name, a.strasse, a.nr, a.plz, a.ort
FROM student s JOIN adresse a ON s.adresse = a.adresse_id
WHERE a.ort = 'St. Gallen';

/* Kap. 4.3.4 Aufgabe 4 */
SELECT s.name Standort, r.bezeichnung Raum , lv.titel Veranstaltung, lv.beginn Von, lv.ende Bis   
FROM lehrveranstaltung lv 
  JOIN  raum r ON lv.raum = r.raum_id                          
  JOIN  standort s ON r.standort = s.standort_id 
WHERE s.name = 'Bern 1' AND lv.beginn BETWEEN '2024-01-24 13:00:00' AND '2024-01-24 17:30:00';

/* Kap. 4.3.4 Aufgabe 5 */
SELECT s.name Standort, r.bezeichnung Raum , f.titel Fach, lv.beginn Von, lv.ende Bis   
FROM lehrveranstaltung lv 
  JOIN  raum r ON lv.raum = r.raum_id                          
  JOIN  fach f ON f.fach_id = lv.fach
  JOIN  standort s ON r.standort = s.standort_id 
WHERE s.name = 'Bern 1' AND lv.beginn BETWEEN '2024-01-24 13:00:00' AND '2024-01-24 17:30:00';

/* Kap. 4.3.4 Aufgabe 6 */
SELECT d.name Name, lv.titel Veranstaltung , s.name Standort, r.bezeichnung Raum , lv.beginn, lv.ende 
FROM raum r JOIN lehrveranstaltung lv ON r.raum_id = lv.raum 
            JOIN standort s ON s.standort_id = r.standort
            JOIN dozent d ON d.dozent_id = lv.dozent
ORDER BY d.name, lv.beginn;

/* Kap. 4.3.4 Aufgabe 7 */
SELECT lv.beginn Beginn, lv.ende Ende , s.name Standort, r.bezeichnung Raum, lv.titel Veranstaltung, f.titel Fach
FROM lehrveranstaltung lv JOIN klasse k ON lv.klasse = k.klasse_id
                          JOIN raum r ON r.raum_id = lv.raum
                          JOIN standort s ON s.standort_id = r.standort
                          JOIN fach f ON f.fach_id = lv.fach
WHERE k.bezeichnung = 'HFSNT.ZH.1'
ORDER BY lv.beginn;

/* Kap 4.4 INNER und OUTER JOIN */
SELECT k.bezeichnung, lv.titel, d.name
FROM klasse k JOIN lehrveranstaltung lv ON lv.klasse = k.klasse_id
              JOIN dozent d ON lv.dozent = d.dozent_id
WHERE lv.titel = 'ITAR1';

SELECT titel, dozent FROM lehrveranstaltung WHERE titel = 'ITAR1';

/* Ausführliche Schreibweise INNER JOIN */
SELECT k.bezeichnung, lv.titel, d.name
FROM klasse k INNER JOIN lehrveranstaltung lv ON lv.klasse = k.klasse_id
              INNER JOIN dozent d ON lv.dozent = d.dozent_id
WHERE lv.titel = 'ITAR1';

/* Kap 4.4 LEFT JOIN findet auch Veranstaltungen ohne Dozent */
SELECT k.bezeichnung, lv.titel, d.name
FROM klasse k JOIN lehrveranstaltung lv ON lv.klasse = k.klasse_id
              RIGHT JOIN dozent d ON lv.dozent = d.dozent_id
WHERE lv.titel = 'ITAR1';

/* Kap 4.4 RIGHT JOIN findet auch Veranstaltungen ohne Dozent 
   wenn die Reihenfolge der Tabellen umgestellt wird */
SELECT k.bezeichnung, lv.titel, d.name
FROM dozent d LEFT JOIN lehrveranstaltung lv ON d.dozent_id = lv.dozent
              JOIN  klasse k ON lv.klasse = k.klasse_id
WHERE lv.titel = 'ITAR1';

/* Kap 4.5 SELF JOIN */
SELECT 
	ma.name 'Mitarbeiter/in', 
	vg.name 'Vorgesetzte/r', 
    ma.funktion 'Funktion' 
FROM mitarbeiter ma LEFT JOIN mitarbeiter vg ON ma.vorgesetzter = vg.ma_id;

/* Kap 4.6 Beispiel kartesisches Produkt */
CREATE TABLE vornamen (vorname VARCHAR(255));
CREATE TABLE nachnamen (nachname VARCHAR(255));
INSERT INTO vornamen VALUES ('Paula'), ('Peter'), ('Klara');
INSERT INTO nachnamen VALUES ('Meier'), ('Schmidt'), ('Kunze');
SELECT vorname, nachname FROM vornamen JOIN nachnamen;

/* Kap 4.7 Beispiel UNION */
SELECT fach_id, titel  FROM fach 
UNION 
SELECT fach_id, titel  FROM fach_alt 
ORDER BY fach_id;

/* Kap. 4.8 Aufgabe 1 - Stundenplan mit Lehrveranstaltungen und Prüfungsterminen für 
die Studentin Hanna Wirz*/
SELECT l.titel, l.beginn, l.ende , sta.name 'Standort', r.bezeichnung 'Raum'
FROM lehrveranstaltung l 
	JOIN klasse k ON l.klasse = k.klasse_id 
	JOIN student s ON s.klasse = k.klasse_id
	JOIN raum r ON r.raum_id = l.raum
	JOIN standort sta ON sta.standort_id = r.standort
WHERE s.name = 'Hanna Wirz'
UNION 
SELECT p.titel, p.beginn, p.ende, sta.name 'Standort', r.bezeichnung 'Raum'
FROM pruefung p 
	JOIN student s ON p.student = s.student_id 
	JOIN raum r ON r.raum_id = p.raum
	JOIN standort sta ON sta.standort_id = r.standort
WHERE s.name = 'Hanna Wirz'
ORDER BY beginn;

/* Kap. 4.8 Aufgabe 2 - Self JOIN, um mehrfach vergebene Räume zu finden */
SELECT lv1.titel, lv1.klasse, lv1.raum, lv1.dozent, lv1.beginn, lv2.titel,  lv2.klasse, lv2.raum, lv2.dozent, lv2.beginn
FROM lehrveranstaltung lv1 join lehrveranstaltung lv2 ON lv1.beginn = lv2.beginn AND lv1.raum = lv2.raum AND lv1.klasse != lv2.klasse;

/* Kap. 4.8 Aufgabe 3 - Self JOIN, um doppelt gebuchte Dozenten zu finden */
SELECT lv1.titel, lv1.klasse, lv1.raum, lv1.dozent, lv1.beginn, lv2.titel,  lv2.klasse, lv2.raum, lv2.dozent, lv2.beginn
FROM lehrveranstaltung lv1 join lehrveranstaltung lv2 ON lv1.beginn = lv2.beginn AND lv1.dozent = lv2.dozent AND lv1.klasse != lv2.klasse;

/* Kap. 4.8 Aufgabe 3 - 64 künstliche Adressen erzeugen */
CREATE TABLE strasse (strasse VARCHAR(255));
CREATE TABLE hausnr (hausnr VARCHAR(255));
CREATE TABLE ort (ort VARCHAR(255));
INSERT INTO strasse VALUES ('Bahnhofstrasse'), ('Poststrasse'), ('Bergstrasse'), ('Kirchweg');
INSERT INTO hausnr VALUES ('11'), ('22'), ('33'), ('44');
INSERT INTO ort VALUES ('A-Stadt'),  ('B-Stadt'), ('C-Dorf'), ('Nirgendwo');
SELECT strasse, hausnr, ort FROM strasse JOIN hausnr JOIN ort;


