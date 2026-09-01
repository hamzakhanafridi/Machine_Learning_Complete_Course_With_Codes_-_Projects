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

# outer and cross join  Lecture 5 day 14
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