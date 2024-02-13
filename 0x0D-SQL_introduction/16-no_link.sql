-- script listing all records of table second_table containing
-- a name value in my MySQL server.
-- Recorded in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
