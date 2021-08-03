-- CREATE TABLE one(
-- 	id SERIAL PRIMARY KEY,
-- 	num SMALLINT,
-- 	other_num smallint
	
-- )

--  CREATE TABLE two(
--  	id SERIAL PRIMARY KEY,
--  	NUM SMALLINT,
--  	other_num smallint,
--  	CONSTRAINT FK_ONE_id FOREIGN KEY(id) REFERENCES one(id) 
--  )


-- CREATE TABLE three(
--  	id SERIAL PRIMARY KEY,
--  	num SMALLINT,
--  	other_num smallint,
--  	FOREIGN KEY(num) REFERENCES one(id) , 
--  	FOREIGN KEY(other_num) REFERENCES two(id)
	
--  )

--insert into one(num,other_num) VALUES
--(3,4)
--(4,5)

-- insert into TWO(num,other_num) VALUES
-- (5,6)
-- (6,7)

--insert into THREE(num,other_num) VALUES
--((SELECT id from one Where id = 1),(SELECT id from two Where id = 1))
--(8,9)

select one.id from one inner join two on one.id = two.id;
select * from one left join three on one.id = three.num;
select * from one right join three on one.id = three.num;
select * from one full outer join three on one.id = three.num;

