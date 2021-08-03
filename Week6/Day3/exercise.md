
--DAY 3
--SELECT name FROM language;
--SELECT language.name,film.title, film.description FROM film FULL outer JOIN language ON LANGUAGE.LANGUAGE_ID = film.language_id;

-- CREATE TABLE new_film(
-- 	new_film_id SERIAL PRIMARY KEY,
-- 	new_film_name VARCHAR (50)
-- )

--INSERT INTO new_film(new_film_name)
--VALUES('The Matrix')
--VALUES('Free Willy')
--SELECT * FROM new_film;

--  CREATE TABLE review(
--  	review_id serial primary key,
--  	film_id SMALLINT,
--  	language_id SMALLINT,
--  	title VARCHAR (50),
--  	score SMALLINT,
--  	review_text TEXT,
--  	last_update DATE,
--  	FOREIGN KEY(film_id) REFERENCES new_film(new_film_id) ON DELETE CASCADE,
--  	FOREIGN KEY(language_id) REFERENCES language(language_id)
	
-- )

--INSERT INTO review(film_id,language_id,title,score,review_text,last_update)
--VALUES((SELECT new_film_id FROM new_film WHERE new_film_name = 'The Matrix'),(SELECT language_id FROM language WHERE name = 'English'),'THE BEST MOVIE EVER',10,'WHY THIS MOVIE WAS SO GOOD','09/03/2021')
--VALUES((SELECT new_film_id FROM new_film WHERE new_film_name = 'Free Willy'),(SELECT language_id FROM language WHERE name = 'English'),'worste movie EVER',10,'WHY THIS MOVIE WAS SO bad','09/03/1970')

--SELECT * FROM review;
--SELECT new_film.new_film_name, review.score FROM new_film INNER JOIN review on new_film.new_film_id = review.film_id;

--DELETE FROM new_film WHERE new_film_name = 'Free Willy';


--part2

--UPDATE film SET language_id = 3 WHERE film_id = 1;
--SELECT*FROM film order by film_id asc;
-- conects to address_id, store id ie where bought from and where he lives, while rental and paymet bpoth referemce this person

--DROP TABLE IF EXISTS review;
--seemingly easy bc only refences and isnt referenced
--SELECT inventory.inventory_id FROM inventory INNER JOIN rental on inventory.inventory_id = rental.inventory_id ORDER BY inventory_id asc;

--SELECT inventory.inventory_id, payment.amount FROM inventory INNER JOIN rental on inventory.inventory_id = rental.inventory_id INNER JOIN payment  ON payment.rental_id = rental.rental_id ORDER BY payment.amount desc limit 33;
--SELECT title FROM film INNER JOIN film_actor on film.film_id = film_actor.film_id INNER JOIN actor on film_actor.actor_id = actor.actor_id WHERE actor.first_name  = 'Penelope' and actor.last_name = 'Monroe' AND film.description ilike '%wrestler%'
--SELECT TITLE FROM FILM where rating = 'R' AND length < 60;
SELECT film.title FROM film INNER JOIN inventory on film.film_id = inventory.film_id INNER JOIN rental on inventory.inventory_id = rental.inventory_id INNER JOIN payment on rental.rental_id = payment.rental_id INNER JOIN customer on customer.customer_id = payment.customer_id WHERE payment.amount > 4.00 AND customer.first_name = 'Matthew'AND customer.last_name = 'Mahan' AND rental.return_date >'07/28/2005'AND rental.return_date <'08/01/2005';
--SELECT film.title FROM film INNER JOIN inventory on film.film_id = inventory.film_id INNER JOIN rental on inventory.inventory_id = rental.inventory_id INNER JOIN payment on rental.rental_id = payment.rental_id INNER JOIN customer on customer.customer_id = payment.customer_id WHERE payment.amount > 4.99 AND customer.first_name = 'Matthew'AND customer.last_name = 'Mahan' AND FILM.description ilike '%boat%'
--select payment_date from payment
