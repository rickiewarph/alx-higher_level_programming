-- Script removing all records with a score of less than 5
-- in the table second_table in my MySQL server.
DELETE FROM `second_table`
WHERE `score` <= 5;
