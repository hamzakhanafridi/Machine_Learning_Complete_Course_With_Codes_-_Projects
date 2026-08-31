create database if not exists afridi;    # ek database create kro afridi name ka 


create table user1(    # afridi database me user1 ka table banawo
	id int primary key,     # matlab id ko user1 ka primary key banawo
    age int,
    name varchar(30) not null,    # matalb name kese be sorat null nahi hone chaheye
    email varchar(50) unique,     # har email unique hone chaheye  
    salery int default 25000,     # agr salery me koey value na mele to osko default 25k set karo
    constraint check (age >= 13)    # constraint mean role   to role check kro ke age > hone chaheye 13 se
);

insert into user1     # matlab table me data ko add karo
 (id,age, name, email, salery)
 values
# (2,27,'Majid','majid@gmail.com', 40000),
 #(3,29,'adam','adam@gmail.com', 30000),
 #(4,33,'tom','tom@gmail.com', 656789),
 (5,30,'mam','mam@gmail.com', 550000),
 (6,33,'tomy','tomy@gmail.com', 5453456),
 (7,38,'boby','boby@gmail.com', 67677);
 

 
create table user2(
	user_id int primary key,   #  ye user2 ka primary key be he
    post varchar(100),
    foreign key (user_id) references user1(id)     # esme ham ne user ko foreign key banaya user1 ke id se
);

select * from user1 
where age>27 and salery >= 40000;     # and operator 

# select count(age) from user1   # aggregate function (wo function jo pehle se define ho our 1 output de de)
# where age=27

# select max(age) from user1   # it is also aggregate functio 

 # select name, age,  email from user1
# where age between 26 and 34
# limit 2;    # lecture 19 limit topic

# select age,name, email from user1
# order by age asc      # make the values in ascending order base on age column


# Groupby clause
# select age , max(salery) from user1
# group by age

# Where clause
# select age, max(salery) from user1
#group by age       # grouping is very important for having clause 
# having max(salery >= 40000)

# set sql_safe_updates=0    # this line is used for updating without this line sql is giving us an error
 
# updating table
# update user1
# set salery= 50000
# where age>=27

# select * from user1    # show all data from user
 
 # delete clause 
 #delete from user1
 #where age=27
 #order by age DESC
 
#select * from user1
#order by age DESC   # mean order it in descending order for ascending order write ASC

# Alter table (mean to do changes in schema (columns)) 
alter table company
add column city varchar(30) default 'Peshawar';   # adding new column in table

alter table user1   
drop column city;    # deleting column from the existing table

alter table user1     
rename to company;    # changing table name

alter table company
change column salery tankhwa int default 5;
 
 alter table company
 modify age int default 50;   # do modification in column like modification in datatypes and constraint(roles)
 
 # truncate mean to empty the table compltly    (truncate table user)
 # drop mean to delete the whole table from the database   (drop table user)
 
select * from company