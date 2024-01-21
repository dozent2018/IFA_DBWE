/* Einige Informationen zu den Tabellen in beispiele */
SELECT 
    table_name AS 'Name', 
    table_rows AS 'Rows',   -- Anzahl Zeilen
    avg_row_length AS 'Len',-- Mittlere Zeilengrösse 
    auto_increment AS 'AI', -- höchster AUTO_INCREMENT Wer
    create_time, update_time
FROM information_schema.tables
WHERE table_schema = 'beispiele';


/* Finde alle Views in der DB beispiele*/
SELECT table_schema AS 'Schema', table_name AS 'View'
FROM information_schema.views
WHERE table_schema = 'beispiele'
ORDER BY table_schema, table_name;

/* Finde Tabellen, die von Views benutzt werden */
SELECT vtu.view_schema AS 'DB',
       vtu.view_name AS 'View',
       vtu.table_name AS 'Tabelle'
FROM information_schema.view_table_usage vtu
JOIN information_schema.tables tab ON vtu.table_schema = tab.table_schema
                                   AND vtu.table_name = tab.table_name
WHERE view_schema = 'beispiele'
ORDER BY vtu.view_schema, vtu.view_name;

/* Alle Spalten einer Tabelle */
SELECT DISTINCT
    column_name AS 'Spalte',
    data_type AS 'Typ',
    is_nullable AS 'Null erlaubt?',
    column_key AS 'Schlüssel?',
    extra AS 'Extra'
FROM information_schema.columns
WHERE table_name = 'lehrveranstaltung';

/* Finde alle Tabellen mit Fremdschlüsseln, die 'adresse' referenzieren */
SELECT DISTINCT CONCAT(table_schema, '.', table_name) AS 'Tabelle-FK',
       CONCAT(referenced_table_schema, '.', referenced_table_name) AS 'PK-Tabelle'
FROM information_schema.key_column_usage
WHERE referenced_table_name = 'adresse'
AND table_schema = 'beispiele'
ORDER BY 'Tabelle-FK';

/* alle Fremschlüsselbeziehungen,die in beispiele existieren*/
SELECT CONCAT(fks.constraint_schema, '.', fks.table_name) AS 'Tabelle-FK',
       CONCAT(fks.unique_constraint_schema, '.', fks.referenced_table_name) AS 'Tabelle-PK',
       kcu.column_name AS 'FK-Spalte',
       '=' AS 'JOIN',
       kcu.referenced_column_name AS 'PK-Spalte'
FROM information_schema.referential_constraints fks
JOIN information_schema.key_column_usage kcu
     ON fks.constraint_schema = kcu.table_schema
     AND fks.table_name = kcu.table_name
     AND fks.constraint_name = kcu.constraint_name
     AND fks.constraint_schema = 'beispiele'
ORDER BY fks.constraint_schema,
         fks.table_name,
         kcu.ordinal_position;
         
/* Alle User */
SELECT host,
       user AS username,
       plugin AS auth_typ,
       authentication_string AS auth_string,
       password_last_changed,
       password_expired,
       account_locked
FROM mysql.user;