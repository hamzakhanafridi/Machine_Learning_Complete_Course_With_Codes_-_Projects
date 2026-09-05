create database student;
drop database student;
use student;
create table abcd(
	id int,
    name varchar(30),
    age int,
    primary key(id),
    constraint check(age >=13),
    foreign key (id) references abcde(id)
);

insert into abcd  values
(1, 'Hamza',27),
(2, 'bob',14),
(3, 'eve',29),
(4, 'tom',30);
select * from abcd;

show databases;
show tables;
drop table abcd;

select * from abcd
where age>20;

select * from abcd
where age+1=15;

select * from abcd
where name='Hamza' and age !=7;

select * from abcd
where age between 20 and 40;

select name,age from abcd
where age NOT in (14,27);

select name,age from abcd
where age in (14,27);

select name,age from abcde
where age>14
limit 2;

select * from abcde
order by age asc;

select max(age) from abcd;

select count(age) from abcde
where age=27;

select name, max(age) from abcde
group by name
having max(age) < 28;


set sql_safe_updates=0;
update abcde
set age=40
where name='Hamza';
select * from abcde;

delete from abcd
where age=29;
show tables;

select * from abcd;

alter table abcde
add column salery int default 25000;
select * from user;

alter table abcde
change column name person varchar(30);

alter table abcde
rename to user;

alter table user
modify salery int default 50000;
select salery from user;


drop table abcd;
show tables;

update user
set salery=salery +salery * 0.25;

select * from user;
select person from user
group by person;

select distinct person from user;

alter table user
add column grade varchar(30);

update user
set grade='A+'
where salery>3000;

select * from user;

update user
set salery=50000
where salery=7813;

select * from user;












# DAY 14  all  lectures related to transactions and commit etc
 select @@autocommit;
 set autocommit=0;
 
create database transac;
use transac;
 
CREATE TABLE account(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    balance DECIMAL(10,2)
);


INSERT INTO account (name, balance) VALUES
('Hamza', 5450),
('tom', 4000),
('bob', 5000),
('eve', 3000);


CREATE TABLE account1(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    balance DECIMAL(10,2)
);


INSERT INTO account1 (name, balance) VALUES
('Hamza', 5450),
('tom', 4000);

select * from account;

start transaction;
update account set balance= balance +300 where id=1;
update account set balance= balance - 300 where id=2;
commit;
select * from account;


start transaction;
update account set balance= balance +300 where id=1;
savepoint top_up;
update account set balance= balance + 30 where id=1;
rollback to top_up;
commit;


drop table account1;
select * from account;
select * from account1;

#outer join
SELECT *
FROM account AS a
LEFT JOIN account1 AS a1
ON a.id = a1.id

UNION

SELECT *
FROM account AS a
RIGHT JOIN account1 AS a1
ON a.id = a1.id;

# SELF join
SELECT *
FROM account AS a
JOIN account AS a1
ON a.id = a1.id;


# Right exclusive join
SELECT *
FROM account AS a
RIGHT JOIN account1 AS a1
ON a.id = a1.id
where a1.id is null;

---#   this is the example of sub query
select * from account
where balance> (
	select avg(balance) from account
);


select name,(
		select count(*) from account as a
        where a.id=c.id
) as count
from account1 as c;



-- # Creating view and also displaying it and also deleting view
create view v1 as
select name, balance from account;
select * from v1;

drop view v1;


create index idx on account(name);
show index from account;

select * from account
where name='Hamza';

#drop index idx on account;



-- creating procedure
DELIMITER //
create procedure neww(in bal int)
begin 
select balance from account
where id= bal;
end;

call neww(2);
drop procedure if exists new;