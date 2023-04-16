-- create table expences (
-- id serial primary key,
-- pay_date date,
-- electricity float,
-- water float,
-- paid_by varchar(10)
-- );

-- insert into expences(pay_date, electricity, water, paid_by)
-- values
-- ('2023-01-01', 20.3, 15.2, 'She'),
-- ('2023-05-01', 44.3, 15.2, 'Him'),
-- ('2023-01-03', 44.3, 15.2, 'Somebody'),
-- ('2023-01-12', 44.0, 117.0, 'She'),
-- ('2023-01-22', 44.3, 15.2, 'She');
-- select water, electricity from expences;
-- select * from expences where electricity<44;
-- -- select * from expences where electricity>44 and paid_by='Him';
-- select max(water) as ddd, min(electricity), avg(electricity) from expences where paid_by!='She';
-- -- select min(electricity) from expences;
-- -- select avg(electricity) from expences where paid_by!='She' 
-- select * from expences where electricity = min(electricity);
-- select paid_by, avg(electricity), avg(water) from expences group by paid_by;
-- select sum(water)+sum(electricity) from expences where paid_by='She'; 

-- select paid_by, sum(water)+sum(electricity) from expences as total
-- group by paid_by; 

-- select paid_by, max(electricity+water) from expences group by paid_by;
-- update expences set paid_by='Yossi' where paid_by='Iossy';
-- update expences set electricity=0 where paid_by='Iossy';
-- delete from expences where id>7;
select count(id) from expences

