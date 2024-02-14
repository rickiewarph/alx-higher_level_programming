-- lists all cities contained in the db hbtn_0d_usa
-- lists all rows of a column in a db
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
