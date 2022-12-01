-- script that lists all cities contained in the database hbtn_0d_usa
-- Prints and joins records from two tables with a matching field
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
        ON cities.state_id = states.id
    ORDER BY cities.id ASC;
