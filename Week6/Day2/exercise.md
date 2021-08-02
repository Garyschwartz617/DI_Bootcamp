question1
--ALTER TABLE items ADD items_id  SERIAL PRIMARY KEY;
--ALTER TABLE customers ADD customer_id  SERIAL PRIMARY KEY;

-- CREATE TABLE purchases(
-- 	items_id SMALLINT,
-- 	customer_id SMALLINT,
-- 	FOREIGN KEY (items_id) REFERENCES items (items_id),
-- 	FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
--)

--SELECT *FROM PURCHASES;
--INSERT INTO purchases(items_id,customer_id)
-- NEED TWO ARGUMENT ERROR
--VALUES(1,1);
--VALUES(2,2);
--VALUES(3,3);
--VALUES(1,3);
--VALUES(2,4);

--SELECT *FROM PURCHASES;
--SELECT * FROM purchases INNER JOIN customers on purchases.customer_id = customers.customer_id;
--SELECT * FROM purchases INNER JOIN customers on purchases.customer_id = customers.customer_id WHERE purchases.customer_id = 4;
--SELECT * FROM purchases INNER JOIN items on purchases.items_id = items.items_id WHERE items.item_name = 'small desk' or items.item_name = 'large desk';

--INSERT INTO items(item_name, price)
--VALUES('hard drive',400)
--INSERT INTO purchases(items_id,customer_id)
--VALUES((SELECT items_id from items WHERE items_id = '4'),(SELECT customer_id from customers WHERE customer_id = '3'));
SELECT DISTINCT customers.first_name, customers.last_name, items.item_name FROM PURCHASES INNER JOIN customers on purchases.customer_id = customers.customer_id  INNER JOIN items on purchases.items_id = items.items_id; 




question 2
--SELECT * FROM customer;
--SELECT (first_name, last_name) as full_name FROM customer;
--SELECT distinct create_date From customer;
--SELECT * FROM customer ORDER BY first_name DESC;
--SELECT film_id,title,description,release_year,rental_rate FROM FILM ORDER BY rental_rate ASC;
--SELECT address, phone FROM address WHERE district = 'Texas';
--SELECT * FROM film WHERE film_id in (15,150);
--SELECT film_id, title, description,length, rental_rate FROM film WHERE title = 'The Matrix';
--SELECT film_id, title, description,length, rental_rate FROM film WHERE title LIKE 'Th%';
--SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;
--SELECT * FROM film ORDER BY rental_rate ASC LIMIT 20;
--SELECT customer.customer_id,amount,payment_date from payment INNER JOIN customer ON payment.customer_id = customer.customer_id ORDER BY customer.customer_id;
SELECT film.film_id, title FROM film LEFT JOIN inventory ON inventory.film_id = film.film_id WHERE inventory.film_id IS NULL;
--SELECT f.film_id, title FROM film f LEFT JOIN inventory i ON i.film_id = f.film_id WHERE i.film_id IS NULL ORDER BY title;
--select distinct title from film where film.film_id not in (inventory.film_id);
--SELECT city.city, country.country FROM city inner JOIN country on city.country_id = country.country_id;


