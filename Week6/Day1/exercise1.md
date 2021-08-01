-- CREATE TABLE customers(
-- 	first_name VARCHAR (50) NOT NULL,
-- 	last_name VARCHAR (100) NOT NULL	
-- )

--INSERT INTO items(item_name, price)
-- VALUES('small desk',100)
--VALUES('large desk', 300)
-- VALUES('fan', 80)

--INSERT INTO customers(first_name, last_name)
--VALUES('Greg', 'Jones')
--VALUES('Sandra', 'Jones')
--VALUES('Scott', 'Scott')
-- VALUES('Trevor', 'Green')
--VALUES('Melanie', 'Johnson')

--SELECT * FROM customers;
--SELECT * FROM ITEMS;
--SELECT * FROM items where price >80;
--SELECT * FROM items where price <=300;
--SELECT * FROM customers where last_name = 'Smith';
SELECT * FROM customers where first_name != 'Scott';
