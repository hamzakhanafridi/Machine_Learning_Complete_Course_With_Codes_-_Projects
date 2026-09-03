create database if not exists prime;
use prime;

create table account(
	id int primary key auto_increment,
    name varchar(30),
    balance decimal(10,2)
);

insert into account(name, balance) values
	('majid', 500.00),
    ('Hamza', 600.00);


# select * from account;

# lecture 2 transaction and commit
start transaction;

update account set balance= balance - 50 where id=1;
update account set balance= balance + 50 where id=2;
commit;        # select all these 4 lines and click on left side of execute option then run below select and change will be done 

select * from account;


#  lecture number 3 rollback and savepoint
start transaction;
update account set balance= balance +1000 where id=2;
savepoint wallet_topup;
update account set balance= balance + 20 where id=2;
-- error     # if there is any error occur in cash back then only rollback to savepoint
rollback to wallet_topup;
commit;        # and do commit to the cash which is deposited in the wallet



#   DOING INNER JOIN FOR THAT WE WILL CREATE 2 TABLES CUSTOMER AND ORDER AND THEN WE WILL DO INNER JOIN IN IT
use khan;
create table customer(
	id int primary key,
    name varchar(30),
    city varchar(30)
);

INSERT INTO customer VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');


CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

alter table orders
change column customer_id id int;

select * from customer;
select * from orders;

# Doing inner join now
select *
from customer c
inner join orders o 
on c.id=o.id;

#  Doing left join     Lecture 5 day 14
select *
from customer c
left join orders o 
on c.id=o.id;

#Doing right join   Lecture 5 day 14
select *
from customer c
right join orders o 
on c.id=o.id;

# outer and cross join  Lecture 6 day 14
# outer join (it is the union of left and right join) 
select *
from customer c
left join orders o 
on c.id=o.id
union
select *
from customer c
right join orders o 
on c.id=o.id;

# cross join (it combine the ist row of A with all rows of B then 2nd row of A with all rows of B and so on)
select *
from customer
cross join orders;

# Self join (do join on both same table like customer table here)     Lecture 7 day 14
select *
from customer as A
join customer as B
on A.id=B.id;

# left and right exclusive join  (LEJ mean A ke wo values jo B me na ho and REJ is inverse of LEJ)   Lecture 8 day 14
select *
from customer c
left join orders o 
on c.id=o.id
where o.id is null;   # mean ham ne dono table ko id ke lehaz se ek kia he to agr ham b ke null values nekale to wahe LEJ hoga matlab ordar A ke values serap movjod he B odar zero he

# REJ is inverse of it 

#  SUB Queries(Also called inner or nested Query)
select *
from orders
where amount > (
		select avg(amount)
        from orders
);

# sub query written in select
select name, (
		select count(*)
        from orders o
        where o.id=c.id
) as order_count
from customer c;

# sub Query written in from
select summary.id, summary.avg_amount
from(
select id, avg(amount) as avg_amount from orders
group by id
) as summary;

select * from customer;
# View
create View v1 as
select id, city from customer;
select * from v1;

# creating view on inner join
create view v2 as
select c.id,c.name, o.order_id
from customer c
inner join orders o
on c.id=o.id;
select * from v2;

# Index in SQL which is important to search some specific data in database
create table account(
	id int primary key,
    name varchar(30),
    branch varchar(30),
    balance decimal(10, 2)
);

insert into account values
(1,'adam','mumbai', 50000),
(2,'tom','dehli', 40000),
(3,'Hamza','peshawar', 25000);

select * from account;

create index idx_city on account(branch);
show index from account;
select * from account 
# where name='tom'
where branch='peshawar';

#  multi indexing(composite index)
create index idx on account(branch, balance);
show index from account;
drop index idx on account;


select * from account;
# store procedure
delimiter $$   # ye es leye use kia howa he q ke eske bager line 191 me ; eske waja se error de raha he q ke sql sochta he ke syntex end ho gaye he leken wo jari he to es waja se ham ne default sign bana leye he our last me end ke bad osko end kar deye he 
create procedure check_bal(in acc_id int)
begin
	select balance from account
    where id =acc_id;
end;
