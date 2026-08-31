create database hamza;
create database test;
drop database test;

use hamza;

create table student(
	rollno int,
    name varchar(30),
    age int
);

insert into student
values
(101, 'Hamza', 27),
(105, 'tom', 30);

select * from student;


use hamza;
show tables;

create database if not exists insta;  
drop database if exists insta


