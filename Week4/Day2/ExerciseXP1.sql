-- select * from items
-- order by price asc;

-- select * from items
-- where price>=80
-- order by price desc;

-- select personal_name, family_name from customers
-- where id<4
-- order by personal_name asc;

-- select family_name from customers
-- order by family_name desc;

-- Exercise 2 : DVRENTAL database
-- select * from customer;

-- select concat(first_name, ' ', last_name) as full_name from customer ;

-- select create_date from customer
-- group by create_date;
-- select * from customer
-- order by first_name asc; 

-- select film_id, title, description, release_year, rental_rate 
-- from film
-- order by rental_rate asc;

-- select address, phone from address
-- where district='Texas'
-- =================================
-- select address.address, address.phone
-- FROM
-- 	customer
-- 	INNER JOIN
-- 	address
-- 	ON 
-- 	customer.address_id = address.address_id
-- where
-- 	address.district = 'Texas'
-- ==========================
-- select * from film
-- where film_id in (15,150);

-- =======8,9=======
-- select film_ID, title, description, length, rental_rate	
-- from film
-- where title like 'Lor%';

-- =======10=======
-- select film_ID, title, rental_rate from film
-- order by rental_rate asc limit 10
-- ======11=======

-- select film_ID, title, rental_rate from film
-- order by rental_rate asc limit 20 OFFSET 10

-- select film_ID, title, rental_rate from film
-- order by rental_rate 
-- OFFSET 10 rows
-- fetch first 10 rows only
-- =================12= data and payment====
-- select 
-- first_name, last_name, 
-- amount, payment_date 
-- from customer inner join payment
-- ON 
-- customer.customer_id = payment.customer_id
-- order by customer.customer_id 

-- ======================13======================
-- SELECT
-- 	film.film_id, 
-- 	film.title
-- FROM
-- 	film
-- 	LEFT JOIN
-- 	(select film_id from inventory group by film_id) as a
-- 	ON film.film_id = a.film_id 
-- where a.film_id is null ;
-- =================================14= City and country==================
-- select city, country 
-- from city
-- join country 
-- ON 
-- city.country_id = country.country_id
-- ;
-- =====================================15==========================
-- select 
-- customer.customer_id, customer.first_name, customer.last_name, 
-- payment.amount, payment.payment_date, payment.staff_id
-- from customer
-- join payment
-- ON 
-- customer.customer_id=payment.customer_id
-- order by payment.staff_id