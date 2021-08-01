-- Database: Bootcamp

-- DROP DATABASE "Bootcamp";

-- CREATE DATABASE "Bootcamp"
--     WITH 
--     OWNER = garyschwartz
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- CREATE TABLE students(
--   id SERIAL PRIMARY KEY,
--   first_name VARCHAR (50) NOT NULL,
--   last_name VARCHAR (100) NOT NULL,
--   birth_date DATE NOT NULL
--  )	
 
--INSERT INTO students (first_name, last_name, birth_date)
--VALUES('Marc','Benichou','02/11/1998');
--VALUES('Yoan','Cohen','03/12/2010');
--VALUES('Lea','Benichou','07/27/1987');
--VALUES('Amelia','Dux','07/04/1996');
--VALUES('David','Grez','01/06/2003');
--VALUES('Omer','Simpson','03/10/1980');
--VALUES('Gary','Schwartz','06/17/1994');


--SELECT * FROM STUDENTS; 
--SELECT first_name,last_name FROM STUDENTS;
--SELECT first_name,last_name FROM students WHERE ID = '2';
--SELECT first_name,last_name FROM STUDENTS WHERE last_name = 'Benichou' AND first_name = 'Marc';
--SELECT first_name,last_name FROM STUDENTS WHERE last_name = 'Benichou' OR first_name = 'Marc';
--SELECT first_name,last_name FROM students WHERE first_name LIKE '%a%';
--SELECT first_name,last_name FROM students WHERE first_name LIKE 'A%';
--SELECT first_name,last_name FROM students WHERE first_name LIKE '%a';
--SELECT first_name,last_name FROM students WHERE first_name LIKE '%a.';
--SELECT first_name,last_name FROM students WHERE ID = '1' or ID = '3';
--SELECT * FROM students WHERE birth_date >= '01-01-2000';