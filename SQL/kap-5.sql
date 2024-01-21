/* Kap 5.2 Beispiele für Aggregatfunktionen */
SELECT COUNT(*) FROM student;

SELECT MAX(note) FROM pruefung;

SELECT MIN(note) FROM pruefung;

SELECT AVG(note) FROM pruefung;

SELECT AVG(note) 
FROM pruefung p 
	JOIN student s ON p.student = s.student_id
	JOIN klasse k ON s.klasse = k.klasse_id
    JOIN fach f ON p.fach = f.fach_id
WHERE k.bezeichnung = 'HFWI.BE.2' AND f.titel = 'Systems Engineering';

/* Kap 5.3 Beispiel für GROUP BY */
SELECT k.bezeichnung Klasse, count(*) Anzahl 
FROM klasse k JOIN student s ON s.klasse = k.klasse_id 
WHERE k.semester = 5 
GROUP BY k.bezeichnung;

/* Kap 5.4 Beispiel für GROUP BY ... HAVING */
SELECT k.bezeichnung Klasse, count(*) Anzahl 
FROM klasse k JOIN student s ON s.klasse = k.klasse_id 
WHERE k.semester = 5 
GROUP BY k.bezeichnung
HAVING k.bezeichnung LIKE 'HFSNT%';

/* Kap 5.5 Beispiele Weitere Funktionen */
SELECT ROUND(3.3567, 2);
SELECT CEIL(25.2);
SELECT FLOOR(25.2);
SELECT CURDATE();

SELECT DATE_FORMAT('2021-11-18', '%d.%m.%y');
SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);

SELECT CONCAT( 'Die Klasse heisst ', bezeichnung ) FROM klasse;

SELECT DATE_FORMAT(CURDATE(), '%d.%m.%y');
SELECT ROUND(AVG(note), 1) FROM pruefung;

/* Kap 5.6 Beispiel Literale und Operatoren */
SELECT 'Eins plus Eins =', 2;
SELECT 7 + 4;
SELECT 3 * 3;
SELECT 30 / 5;
SELECT COUNT(*) + 1 FROM student WHERE klasse = 1;
SELECT 'Die Klasse ', bezeichnung, 'hat noch ', 6 - semester + 1, 'Semester vor sich' FROM klasse;
UPDATE raum SET kapazitaet = kapazitaet - 5 WHERE kapazitaet < 20;
SELECT ROUND( RAND() * (100 - 20) );

/* Kap 5.7 Aufgaben */
-- 1. Titel und Beginn der Prüfungen, Beginn im Format Tag.Monat.Jahr Stunde:Minute 
SELECT titel, DATE_FORMAT(beginn, '%d.%m.%Y %H:%i') 
FROM pruefung;

-- 2.	Finden Sie die zeitlich erste und die letzte Prüfung in der Datenbank. Geben Sie Titel, Standort und Datum aus.
SELECT 
	titel AS 'Prüfung',
	MIN(pruefung.beginn) AS 'Frühester Termin', MAX(pruefung.beginn) AS 'Spätester Termin'
FROM pruefung
GROUP BY titel
ORDER BY titel;

-- 3. Wie ist die Durchschnittsnote der verschiedenen Klassen im Fach Deutsch?
SELECT k.bezeichnung, AVG(p.note)
FROM klasse k JOIN student s ON s.klasse = k.klasse_id
              JOIN pruefung p ON p.student = s.student_id
              JOIN fach f ON f.fach_id = p.fach
WHERE f.titel = 'Deutsch'
GROUP by k.bezeichnung;

-- 4. Wie ist die Auslastung der Räume am Standort Bern mit Lehrveranstaltungen?
SELECT r.bezeichnung, count(lv.klasse) 
FROM raum r LEFT JOIN lehrveranstaltung lv ON r.raum_id = lv.raum
            JOIN standort s ON s.standort_id = r.standort
WHERE s.name = 'Bern 1'
GROUP BY r.bezeichnung;

Select distinct raum_id, bezeichnung from raum where standort = 2;




