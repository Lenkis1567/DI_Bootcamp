-- create table students(
-- id serial primary key,
-- first_name varchar(10),	
-- last_name varchar(15),
-- birth_date date
-- );
-- insert into students(first_name, last_name, birth_date)
-- values
-- ('Marc','Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou','1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03');

-- select * from students;

-- select *
-- from students 
-- where last_name='Benichou' and first_name='Marc';

-- select *
-- from students 
-- where last_name='Benichou' or first_name='Marc';

-- insert into students(first_name, last_name, birth_date)
-- values
-- ('Elena','Ch', '1999-09-09');

-- select *
-- from students 
-- where first_name like '%a%';

-- select *
-- from students 
-- where lower(first_name) like 'a%';

-- select *
-- from students 
-- where first_name like '%a';

-- select *
-- from students 
-- where first_name like '%a_';

-- select first_name, last_name
-- from students 
-- where id=1 or id=3;

-- select *
-- from students 
-- where birth_date >='2000-01-01'