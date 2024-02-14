-- Script listing all cities of California found in the database hbtn_0d_usa
-- Script lists all rows of a column in a db
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
