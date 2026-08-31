# Practice set of all previous concepts 
create database if not exists khan;
use khan;

create table teacher(
	id int primary key,
    name varchar(30),
    subject varchar(50),
    salery int
);

insert into teacher
(id , name , subject, salery)
values
(1,'Hamza','Machine learning', 500000),
(2,'Majid','Data science', 400000),
(3,'tom','Physics', 300000),
(4,'bob','Maths', 200000);

select * from teacher;

select * from teacher
where salery >400000;

alter table teacher
add column city varchar(50) default 'Peshawar';

# increasing salery of all by 25%
update teacher
set salery = salery + salery * 0.25;

# adding new column grade and add there some conditions  like if salery is greater than 5 lac give them A+ grade for less than 5lac give A grade
alter table teacher
add column grade varchar(30);

update teacher 
set grade='A+'
where salery>=500000;

update teacher 
set grade='A'
where salery<500000;

select * from teacher;