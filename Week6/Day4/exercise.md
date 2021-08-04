
--SELECT first_name,last_name FROM employees;
SELECT DISTINCT department_id FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
--SELECT first_name,last_name,salary, salary/15 as pf from employees ;
--SELECT employee_id, first_name,last_name,salary from employees ORDER BY salary ASC;
--SELECT sum(salary) from employees;
--SELECT MAX(salary), min(salary) from employees;
SELECT AVG(salary) from employees;
SELECT COUNT(FIRST_NAME) from employees;
SELECT UPPER(FIRST_NAME) from employees;
SELECT LEFT(FIRST_NAME,3) from employees;
SELECT (first_name,last_name) as Full_name FROM employees;
SELECT first_name, last_name, LENGTH(FIRST_NAME) + LENGTH(last_name) as full_name FROM employees ;
SELECT * FROM employees where first_name like ('%#%');
SELECT * FROM employees LIMIT 11;


SELECT first_name,last_name,salary from employees WHERE salary >= 10000 AND salary <= 15000 ;
SELECT first_name,last_name,hire_date from employees WHERE hire_date >= '01/01/1987' AND hire_date < '01/01/1988' ;
SELECT * FROM employees WHERE first_name ILIKE '%e%' AND first_name ILIKE '%c%';
SELECT * FROM jobs;
SELECT employees.last_name, employees.salary, jobs.job_title FROM employees INNER JOIN jobs on employees.job_id = jobS.job_id WHERE jobs.job_title NOT IN ('Shipping Clerk','Programmer') AND employees.salary NOT IN(4500,10000,15000);
SELECT LAST_NAME FROM employees WHERE LENGTH(last_name) = 6;
SELECT last_name FROM employees WHERE POSITION('e' IN last_name) = 3;
SELECT  jobs.job_title FROM employees Full outer JOIN jobs on employees.job_id = jobS.job_id WHERE jobs.job_id NOT IN (employees.job_id);
SELECT  jobs.job_title FROM employees Full outer JOIN jobs on employees.job_id = jobS.job_id WHERE employees.job_id is null;
SELECT * FROM employees Where last_name IN ('Jones','Blake','King','Ford','Scott');


