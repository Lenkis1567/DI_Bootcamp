-- create table customers(
-- id serial primary key,
-- Personal_name varchar(8),
-- Family_name varchar(12)
-- );
-- insert into customers(Personal_name, Family_name)
-- values 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');
-- select * from items;
-- select * from customers;
-- drop table items;
-- create table items(
-- id serial primary key,
-- name_item varchar(15),
-- price float
-- )

-- insert into items(name_item, price)
-- values ('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fun', 80);

-- select * from items where price>80;
-- select * from items where price<=300;

-- select Personal_name, Family_name from customers where family_name='Smith';
-- select Personal_name, Family_name from customers where family_name='Jones';
select Personal_name, Family_name from customers where family_name!='Scott';