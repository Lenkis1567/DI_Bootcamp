create table menu(
id serial primary key,
item varchar (40),
price float );

insert into menu(item, price)
values
('Veggy burger', 15.5),
('Potatoes', 11.3)

