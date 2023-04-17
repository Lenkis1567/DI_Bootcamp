-- create table apartment (
-- id serial primary key,
-- location varchar(50),
-- act_id int references actors(actor_id)
-- ); 

-- insert into apartment(location, act_id)
-- values 
-- ('Beeverly', (select actor_id from actors where first_name='Matt'));

-- create table producers (
-- id serial primary key,
-- name varchar(15))
-- insert into producers (name)
-- values 
-- ('Stanley'),
-- ('Clooney');
-- alter table apartment add column producer_is int;
-- alter table apartment add constraint fk_producers 
-- foreign key (producers_id) references producers(id);
-- insert into apartment(location, producer_is) values
-- ('New York', 1);
-- select name, location from
-- apartment
-- join producers
-- on apartment.producer_is=producers.id
-- insert into apartment (location, act_id)
-- values
-- ('Alaska', (select actor_id from actors where first_name='Matt'))

-- create table movies(
-- id serial primary key,
-- title varchar(50));

-- create table actors_movies(
-- actor_id int references actors(actor_id),
-- movie_id int references movies(id));

-- insert into movies(title) values ('Pulp fiction');
-- delete from movies 
-- where id=2
-- delete from actors 
-- where actor_id=4

insert into actors_movies(actor_id, movie_id) values
((select actor_id from actors where first_name = 'Kim'), (select id from movies where title = 'Pulp fiction')),
((select actor_id from actors where first_name = 'Matt'), (select id from movies where title = 'Pulp fiction')),
((select actor_id from actors where first_name = 'George'), (select id from movies where title = 'Pulp fiction'));