/* Code-Beispiele zum Kapitel Grundoperationen */

/* Datenbank anlegen */
CREATE DATABASE jochen;

/* Datenbanken anzeigen */
show databases;

/* Zur neuen Datenbank wechseln */
use jochen;

/* Tabelle student anlegen */
CREATE TABLE student (
  student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name       VARCHAR(255) NOT NULL,
  vorname    VARCHAR(255) NOT NULL,
  email      CHAR(100)
);

/* Tabellenstruktur anzeigen */
describe student;


/* Tabelle fach anlegen */
CREATE TABLE fach (
  fach_id    INTEGER PRIMARY KEY AUTO_INCREMENT,
  name       VARCHAR(255) NOT NULL,
  beginn     DATE,
  semester   INTEGER NOT NULL
);

/* Die vorhandenen Tabellen anzeigen */
show tables;

/* 3 Zeilen in die Tabelle student einfügen */
INSERT INTO student (name, vorname, email)
VALUES
  ('Schmid','Norina','n.schmid@schule.ch'),
  ('Mäder','Klaus','k.maeder@schule.ch'),
  ('Kunz','Paula','p.kunz@schule.ch')
;

/* 3 Zeilen in die Tabelle fach einfügen */
INSERT INTO fach (name, beginn, semester)
VALUES
  ('Netzwerke','2021-09-30',2),
  ('Mathematik','2008-01-01',2),
  ('Datenbanken',NULL,2)
;  

/* Alle Zeilen und Spalten von fach */
SELECT * FROM fach;

/* Nur die Spalten vorname und name in student */
SELECT vorname, name from student;

/* Alle Fächer im 2. Semester */
SELECT * FROM fach WHERE semester = 2;

/* Alle Fächer, die ab dem 01.01.2021 beginnen */
SELECT name, beginn FROM fach WHERE beginn >= '2021-01-01';

/* Neue Fächer einfügen */
INSERT INTO fach (name,beginn,semester)
VALUES
  ('Linux','2018-01-15',1),
  ('Shell Scripting','2018-01-15',2),
  ('IT-Architektur',NULL,6),
  ('Mathematik 2','2008-06-01',2),
  ('Mathematik 2','2008-06-01',2),
  ('Cloud Computing','2022-06-15',6)
;

/* Abfrage mit AND in der WHERE-Klausel 1 */
SELECT * FROM fach 
WHERE semester BETWEEN 1 AND 3
AND name LIKE 'Mathe%';

/* Abfrage mit AND in der WHERE-Klausel 2 */
SELECT * FROM fach 
WHERE semester > 4
AND beginn > '2021-06-01';

/* Abfrage NULL-Werte, 1. Versuch */
SELECT * FROM fach WHERE beginn = NULL;

/* Abfrage NULL-Werte, 2. Versuch */
SELECT * FROM fach WHERE beginn IS NULL;

/* Abfrage mit OR in der WHERE-Klausel */
SELECT * FROM fach 
WHERE semester > 4
AND beginn > '2021-06-01'
OR beginn IS NULL;

/* Sortieren mit ORDER BY */
SELECT name, vorname, email FROM student
ORDER BY name ASC, vorname ASC;

/* Duplikate unterdrücken mit SELECT DISTINCT */
SELECT DISTINCT name FROM student
WHERE email IS NOT NULL
ORDER BY name;

/* Neue Studenten einfügen */
INSERT INTO student (name, vorname, email)
VALUES
  ('Kunz','Peter','n.schmid@example.com'),
  ('Sorglos','Susi','susi@sorglos.com'),
  ('Kraus','Karl',NULL)
;

/* Alle Studenten mit .com E-Mail Adresse finden*/
SELECT * FROM student WHERE email LIKE '%.com';

/* Alle Studenten mit fehlender E-Mail Adresse */
SELECT * FROM student WHERE email IS NULL;

/* Fächer, deren Beginn im Jahr 2008 lag */
SELECT * FROM fach 
WHERE beginn >= '2008-01-01' AND beginn <= '2008-12-31';
/* oder: */
SELECT * FROM fach 
WHERE beginn BETWEEN '2008-01-01' AND '2008-12-31';

/* Tabelle 'fach': alle Zeilen, bei denen der Beginn vor dem 1.1.2021 liegt und
das Semester 1 ist */
SELECT * FROM fach
WHERE beginn < '2021-01-01' AND semester = 1;

/* Zeilen der Tabelle 'fach' zuerst nach Semester, dann nach Beginn sortiert aus, aber
nur solche Zeilen, die als Beginn ein Datum vor dem Jahr 2022 haben */
SELECT * FROM fach
WHERE beginn < '2022-01-01'
ORDER BY beginn, semester;

/* Ändern E-Mail Adresse Studentin */
UPDATE student SET email = 'paula@home.ch'
WHERE name = 'Kunz' and vorname = 'Paula';

/* Student mit der ID 6 löschen */
DELETE FROM student WHERE student_id = 6 

/* Tabelle für Demo ALTER TABLE */
create table kunde (
  kunde_id INT primary key auto_increment,
  name char(40),
  kunde_seit date,
  email varchar(255) not null
);

/* Beispiel für ALTER TABLE */
ALTER TABLE kunde
  ADD website VARCHAR(255),
  MODIFY name VARCHAR(255) NOT NULL
);
