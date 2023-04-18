-- create table product_orders(
-- id serial primary key,
-- quantity int not null,
-- purchase_time timestamp not null default current_timestamp,
-- product_id int references items(item_id) on delete no action
-- );

-- create table items (
-- item_id serial primary key,
-- name varchar(20) not null unique,
-- price int not null
-- )

-- insert into items(name, price)
-- values
-- ('knife', 20),
-- ('rope', 5),
-- ('soap', 3),
-- ('saw', 32);

-- insert into product_orders(quantity, product_id)
-- values
-- (5, (select item_id from items where name='rope')),
-- (1, (select item_id from items where name='soap')),
-- (1, (select item_id from items where name='saw'));


-- create or replace function total_price (order_id int)
-- returns integer as $$

-- declare total_sum int;

-- begin 
-- 	total_sum:= (select sum(price*quantity) from product_orders 
-- 			join items
-- 			on 
-- 			product_orders.product.id=items.item_id
-- 			where product_orders.id=order_id);
-- 		return total_sum;
-- 	end;

-- $$ language plpgsql;

-- create table users(
-- 	id serial primary key,
-- 	name varchar(20),
-- 	id_order int references product_orders(id)
-- );
-- insert into users(name, id_order)
-- values ('Ron', 1),
-- ('Bob', 2),
-- ('Bean', 3);
-- =====
-- total price for a given order of a given user
-- ===


create or replace function total_price_customer (user_id int, order_id int)
returns integer as $$

 declare total_pr int;

begin 
	total_sum:= select ((total_price(order_id)) from product_orders 
			join items
			on 
			product_orders.product.id=items.item_id
			
			joint product_orders
			
-- 			where product_orders.id=order_id);
-- 		return total_sum;
-- 	end;

-- $$ language plpgsql;