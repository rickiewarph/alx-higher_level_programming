-- Scrip that lists the no. of records with same score in
-- the table second_table in my MySQL server.
-- Recorded in descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
