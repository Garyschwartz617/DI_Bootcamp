-- Database: exercise1

-- DROP DATABASE exercise1;

-- CREATE DATABASE exercise1
--     WITH 
--     OWNER = garyschwartz
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;
	
-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )	

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(' George',' Clooney','06/05/1961 ', 2);

--SELECT actor_id FROM actors ORDER BY actor_id DESC LIMIT 1;

--INSERT INTO actors (first_name, age )
--VALUES('Gary','07/15/1978 ');
-- violates the not null constarints