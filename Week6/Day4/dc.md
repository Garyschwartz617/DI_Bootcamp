
--  CREATE TABLE items(
--  	id SERIAL PRIMARY KEY,
--  	name VARCHAR(50),
--  	price SMALLINT
--  )

-- CREATE TABLE orders(
-- 	name VARCHAR(50),
-- 	item_id SMALLINT,
-- 	FOREIGN KEY (item_id) REFERENCES items(id)
-- )

--insert into items(name,price) VALUES
--('chips',10)
-- ('milk', 15)
--('yogurt', 20)

SELECT* FROM items;

--insert into orders(name,item_id) VALUES
--('GARY',(SELECT id FROM items WHERE name = 'chips'))
--('GARY',(SELECT id FROM items WHERE name = 'milk'))
--('GARY',(SELECT id FROM items WHERE name = 'yogurt'))
SELECT* FROM orders;

-- CREATE or REPLACE FUNCTION total(fn varchar(50)) 
-- RETURNS smallint AS $total_price$
-- BEGIN
--    RETURN(SELECT sum(items.price) FROM items INNER JOIN orders ON items.id = orders.item_id WHERE orders.name = fn);
-- END;
-- $total_price$ LANGUAGE plpgsql;


SELECT*FROM total('GARY');
