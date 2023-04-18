-- select language.name
-- from language 
-- join film
-- on film.language_id=language.language_id
-- group by language.name;

-- select film.title, film.description, language.name 
-- from language 
-- join film
-- on film.language_id=language.language_id
-- where language.name=null
-- group by film.title, language.name, film.description;

-- select film.title, film.description, language.name 
-- from language 
-- left join film
-- on language.language_id=film.language_id
-- group by film.title, language.name, film.description;

-- create table new_film (
-- 	id serial primary key,
-- 	name varchar(30));
	
-- insert into new_film(name) 
-- values
-- ('Dead and alive'),
-- ('War and piece'),
-- ('Slave of bracelet'),
-- ('0 still women')

-- create table customer_review(
-- review_id serial primary key,
-- film_id int, FOREIGN KEY (film_id) 
--         REFERENCES new_film(id) 
-- 		on delete cascade,
-- language_id int references language(language_id), 
-- title varchar(30),
-- score integer,
-- review_text text,
-- last_update timestamp not null default CURRENT_TIMESTAMP
-- );

-- insert into customer_review(film_id, language_id, title, score, review_text, last_update) 
-- values
-- (1, 2, 'Couldn"t watch till the end', 2, 'will be able to write later', '2023-01-04'),
-- (2, 1, 'Nice', 5, 'I advice to see it', '2023-02-01'),
-- (1, 2, 'Not onw', 0, 'will think of it later', '2023-04-06');

-- delete from new_film 
-- where new_film.id=2; 
-- will not work without ON DELETE CASCADE

-- -- ======================part2=============================
-- update film
-- set language_id=3
-- where film_id=10 or film_id=25

-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- (-address and store)
-- (I guess it doesn't)
 
--  We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- (Easy)

-- select 
-- count(rental_id)
-- from rental
-- where (return_date is null);


-- select rental_date, customer_id, film.film_id, title, rental_rate, rating, description from rental
-- inner join inventory on rental.inventory_id=inventory.inventory_id
-- left join film on inventory.film_id=film.film_id
-- where rental.return_date is null
-- order by film.rental_rate desc
-- limit 30

-- select film.title, film.film_id from film_actor
-- inner join film 
-- on film.film_id=film_actor.film_id
-- where (actor_id=(select actor_id from actor
-- 					   where (first_name like '%nelope%' and last_name like '%onro%')))
-- 					   and film.description like '%umo %restl%' 

-- select * from film
-- where film.length<60 and film.description like '%ocumentar%' and film.rating='R'

-- select film.title, film.film_id, film.description from film

-- select * from inventory
-- inner join film on film.film_id=inventory.film_id
-- inner join rental on rental.inventory_id=inventory.inventory_id
-- inner join customer on customer.customer_id=rental.customer_id
-- where customer.first_name='Matthew' and customer.last_name='Mahan' and film.rental_rate>4 and 
-- rental.return_date>'2005-07-28'
-- and rental.return_date<'2005-08-01'

select * from inventory
inner join film on film.film_id=inventory.film_id
inner join rental on rental.inventory_id=inventory.inventory_id
inner join customer on customer.customer_id=rental.customer_id
where customer.first_name='Matthew' and customer.last_name='Mahan' 
and film.title like '%oat%' or film.description ilike '%boat%'
order by film.replacement_cost desc limit 1
