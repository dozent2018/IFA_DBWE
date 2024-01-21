/* Kap. 6 Beispiele Subqueries */

SELECT bezeichnung, kapazitaet FROM raum 
WHERE standort = 1 AND 
kapazitaet >= ( SELECT COUNT(*) FROM student WHERE klasse = 3 );

SELECT s.name, p.note
FROM student s JOIN klasse k ON k.klasse_id = s.klasse
               JOIN pruefung p ON s.student_id = p.student
               JOIN fach f ON f.fach_id = p.fach
WHERE f.titel = 'Systems Engineering' 
	AND k.bezeichnung = 'HFWI.BE.2'
	AND note > ( SELECT AVG(note) FROM pruefung WHERE fach = p.fach ); 
    
/* Beispiel EXISTS: Fächer im fachplan für den Lehrgang HFSNT, die auch für den Lehrgang HFWI gelten */
SELECT fa1.titel 
FROM fach fa1 JOIN fachplan fp ON fa1.fach_id = fp.fach
              JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
WHERE lg.kuerzel = 'HFSNT' AND EXISTS ( 
	SELECT * 
    FROM fach fa2 JOIN fachplan fp ON fa2.fach_id = fp.fach
                 JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
	WHERE lg.kuerzel = 'HFWI' AND fa1.fach_id = fa2.fach_id
);

/* Beispiel NOT EXISTS: Fächer im fachplan für den Lehrgang HFSNT, die NICHT für den Lehrgang HFWI gelten */
SELECT fa1.titel 
FROM fach fa1 JOIN fachplan fp ON fa1.fach_id = fp.fach
              JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
WHERE lg.kuerzel = 'HFSNT' AND NOT EXISTS ( 
	SELECT *
	FROM fach fa2 JOIN fachplan fp ON fa2.fach_id = fp.fach
                  JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
	WHERE lg.kuerzel = 'HFWI' AND fa1.fach_id = fa2.fach_id
);

/* Beispiel ANY: Fächer im fachplan für den Lehrgang HFSNT, die NICHT für den Lehrgang HFWI gelten */
SELECT titel 
FROM fach fa JOIN fachplan fp ON fa.fach_id = fp.fach
			 JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
WHERE lg.kuerzel = 'HFSNT' AND
fp.fach = ANY ( 
	SELECT fach
	FROM fachplan fp JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
	WHERE lg.kuerzel = 'HFWI'
);

/* Beispiel ALL */

SELECT titel 
FROM fach fa JOIN fachplan fp ON fa.fach_id = fp.fach
			 JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
WHERE lg.kuerzel = 'HFSNT' AND
fp.fach = ALL ( 
	SELECT fach
	FROM fachplan fp JOIN lehrgang lg ON lg.lehrgang_id = fp.lehrgang
	WHERE lg.kuerzel = 'HFWI'
);

/* Kap. 6.3 - Aufgabe 1 */
SELECT DISTINCT r.bezeichnung, r.kapazitaet, s.name
FROM 
	raum r JOIN standort s ON r.standort = s.standort_id
	JOIN lehrveranstaltung l ON l.raum = r.raum_id
WHERE s.name = 'Bern 1'  AND r.kapazitaet >= 20 AND
	r.raum_id NOT IN (SELECT raum FROM lehrveranstaltung WHERE beginn BETWEEN '2022-10-04 13:00:00' AND '2022-10-04 17:30:00' );

/* Kap. 6.3 - Aufgabe 2 */
SELECT DISTINCT r.bezeichnung, r.kapazitaet, s.name
FROM 
	raum r JOIN standort s ON r.standort = s.standort_id
	JOIN lehrveranstaltung l ON l.raum = r.raum_id
WHERE s.name = 'Bern 1'  AND r.kapazitaet >= 20 AND
	r.raum_id NOT IN (SELECT raum FROM lehrveranstaltung WHERE beginn BETWEEN '2022-10-04 13:00:00' AND '2022-10-04 17:30:00' );
    