/* Kap. 6.3 - Aufgabe 2 */
SELECT DISTINCT r.bezeichnung, r.kapazitaet, s.name
FROM 
	raum r JOIN standort s ON r.standort = s.standort_id
	JOIN lehrveranstaltung l ON l.raum = r.raum_id
WHERE s.name = 'Bern 1'  AND r.kapazitaet >= 20 AND
	r.raum_id NOT IN (select raum from lehrveranstaltung where beginn BETWEEN '2022-10-04 13:00:00' AND '2022-10-04 17:30:00' );
    