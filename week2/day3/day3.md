subesta@subesta-Lenovo-Yoga-C740-14IML:~$ sudo -u postgres psql





maktpa=# \c postgres;
You are now connected to database "postgres" as user "postgres".

Q1 : Get only the capital of specific country (USA)
Answer : select ca_name from capital where c_id in (select c_id from country where c_name='USA');
 ca_name 
---------
 Newyork
(1 row)


postgres=# \c college 

Q2 : Create Table faculty
Answer :

college=# create table faculty(
college(# f_id serial primary key,
college(# f_name varchar(50));
CREATE TABLE

Q3 : Create Table department
Answer :

college=# create table department(
college(# d_id serial primary key,
college(# d_name varchar(50),
college(# f_id int,
college(# foreign key(f_id) references faculty(f_id));
CREATE TABLE

Q4 : Create Table professor
Answer :
^
college=# create table professor(
college(# p_id serial primary key,
college(# f_id int,
college(# d_id int,
college(# f_name varchar(50),
college(# l_name varchar(50),
college(# age int,
college(# salary decimal(8,2),
college(# image text,
college(# foreign key(f_id) references faculty(f_id),
college(# foreign key(d_id) references department(d_id));
CREATE TABLE

Q5 : Create Table subject
Answer :

college=# create table subject(
college(# s_id serial primary key,
college(# s_name varchar(50),
college(# s_code varchar(50),
college(# f_id int,
college(# foreign key(f_id) references faculty(f_id));
CREATE TABLE

Q6 : Create Table student
Answer :

college=# create table student(
college(# stu_id serial primary key,
college(# f_name varchar(50),
college(# l_name varchar(50),
college(# f_phone int,
college(# l_phone int,
college(# b_date date,
college(# image text);
CREATE TABLE

Q7 : Create Table course
Answer :

college=# create table course(
college(# co_id serial primary key,
college(# stu_id int,
college(# duration int,
college(# p_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(p_id) references professor(p_id));
CREATE TABLE

Q8 : Create Table enrollment
Answer :

college=# create table enrollment(
college(# e_id serial primary key,
college(# co_id int,
college(# stu_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(co_id) references course(co_id));
CREATE TABLE

Q9 : Create Table exams
Answer :

college=# create table exams(
college(# ex_id serial primary key,
college(# e_id int,
college(# date date,
college(# time time,
college(# duration int,
college(# foreign key(e_id) references enrollment(e_id));
CREATE TABLE

Q10: Create Table exams
Answer :

college=# create table address(
college(# add_id serial primary key,
college(# government varchar(50),
college(# city varchar(50),
college(# address1 varchar(50) not null,
college(# address2 varchar(50) null);
CREATE TABLE

Q11 : Create Table <address></address>
Answer :

college=# create table stu_address(
college(# sa_id serial primary key,
college(# add_id int,
college(# stu_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(add_id) references address(add_id));
CREATE TABLE

Q1 : Insert One Faculty
Answer:

college=# insert into faculty values(1,'commerce');
INSERT 0 1

Q2 : Insert Three Departments Into This Faculty
Answer:

college=# insert into department values(1,'bis',1);
college=# insert into department values(2,'hr',1),(3,'accounting',1);
INSERT 0 2

Q3 : Insert Three Subjects In Every Department
Answer:

college=# insert into subject values(1,'accounting','123',1);
INSERT 0 1
college=# insert into subject values(2,'hr','124',1),(3,'pr','125',1);
INSERT 0 2

Q1 :Select all Students, Professor, Subjects, Courses, Exams, Departments
Answer:

select*from Students, Professor, Subjects, Courses, Exams, Departments;

Q2 :Select all Professors with the Age is 40
Answer:

select * from professor where age=40;

Q3 :Select all Professors with the salary greater than 10000
Answer:

select * from professor where salary >10000;

Q4 :Order the Professors by the salary
Answer:

select * from professor order by salary;

Q5 :Order the students by the Birth_Date
Answer:

select * from professor order by Birth_Date;

Q6 :Get the average salary of the Professors
Answer:

select avg(salary) from professor;

Q7 :Update the salary of the Professors with the salary greater than 10000 to 20000
Answer:

update professor set salary=20000.00 where p_id=1

Q8 :Delete the Professors with the salary greater than 20000
Answer:

update professor set salary=30000.00 where p_id=2;

Q9 :Add Age Column in Student Table
Answer:

alter table student add age int null;

Q10 :Set Students Age
Answer:

insert into student (stu_id,age) values(10,21);


* EXERCISE :2

Q1 :Find all customers who never order anything.
Answer:

select * as Customers from Customers where id not in (select customerId from Orders) ;








