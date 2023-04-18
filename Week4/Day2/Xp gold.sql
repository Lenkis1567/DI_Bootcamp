-- -- Exercise 1: DVD Rental
-- select rating, count(film_id) from film
-- group by rating;
-- ==========================================
-- select title, length, rental_rate from film
-- where (rating='G' or rating='PG-13') and length<120 and rental_rate<3
-- order by title
-- ==============================================================

-- update customer set (first_name, last_name)=('Elena', 'Ch')
-- where customer_id=2;

-- update address set (address) = 'Tel Aviv'
-- where address.address_id=customer.address_id and customer.first_name='Elena'

-- ============Exercise 2: students table================================
-- update students set birth_date='02/11/1998'
-- where last_name='Benichou';

-- update students set last_name='Guez'
-- where last_name='Grez' and first_name='David'

-- delete from students
-- where last_name='Benichou' and first_name='Lea'

-- select
-- count (first_name) 
-- from students
-- where birth_date>'2000-01-01';

-- alter table students 
-- add column math_grade int;


-- update students
-- set math_grade=80
-- where id=1

-- update students
-- set math_grade=90
-- where id=2 or id=4

-- update students
-- set math_grade=40
-- where id=6

-- select
-- count (first_name)
-- from students
-- where math_grade>83
-- ======
-- insert into students(first_name, last_name, birth_date, math_grade)
-- values
-- ('Omer', 'Simpson', '1980-10-03', 70)
-- =====
-- select first_name, last_name, count(math_grade) as tota_grade
-- from students
-- group by first_name, last_name
-- ======================
-- select
-- sum(math_grade)
-- from students
-- ==================Exercise 3 : Items and customers======
-- create table purchases (
-- id serial primary key,
-- customer_id int references customers(id),
-- item_id int references items(id),
-- quantity_purchased integer)

-- insert into purchases(customer_id, item_id, quantity_purchased)
-- select
-- 	(select id from customers where personal_name='Scott') as t1, 
-- 	(select id from items where name_item='Fan') as t2,
-- 	8;

-- insert into purchases(customer_id, item_id, quantity_purchased)
-- values
-- 	(5, 2, 10),
-- 	(1, 1, 2)
-- ;

select item_id, name_item, sum(purchases.quantity_purchased) 
from purchases 
join
items
on purchases.item_id = items.id
group by item_id, name_item;

