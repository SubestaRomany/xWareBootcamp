 sudo -u postgres psql

postgres=# \c maktpa;



postgres=# select ca_name from capital where c_id in (select c_id from country where c_name='USA');
 ca_name 
---------
 Newyork
(1 row)

postgres=# \l

postgres=# \c college 
You are now connected to database "college" as user "postgres".
college=# \dt
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | faculty | table | postgres
(1 row)

college=# drop table faculty;
DROP TABLE
college=# drop table department;
ERROR:  table "department" does not exist
college=# create table faculty(
college(# f_id serial primary key,
college(# f_name varchar(50));
CREATE TABLE
college=# create table department(
college(# d_id serial primary key,
college(# d_name varchar(50),
college(# f_id int,
college(# foreign key(f_id) references faculty(f_id));
CREATE TABLE
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
college(# foreign key(d_id) references department(d_id),
college(# primary key(f_id,d_id));
ERROR:  multiple primary keys for table "professor" are not allowed
LINE 12: primary key(f_id,d_id));
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
college(# ^C
college=# foreign key(f_id) references faculty(f_id),
college-# foreign key(d_id) references department(d_id));
ERROR:  syntax error at or near "foreign"
LINE 1: foreign key(f_id) references faculty(f_id),
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
college=# create table subject(
college(# s_id serial primary key,
college(# s_name varchar(50),
college(# s_code varchar(50),
college(# f_id int,
college(# foreign key(f_id) references faculty(f_id));
CREATE TABLE
college=# create table courses(
college(# co_id serial primary key,
college(# stu_id int,
college(# duration int,
college(# p_id int,
college(# foreign key(stu_id),;
college(# );
ERROR:  syntax error at or near ","
LINE 6: foreign key(stu_id),;
                           ^
college=# create table courses(
college(# co_id serial primary key,
college(# stu_id int,
college(# duration int,
college(# foreign keyllhjj);;
ERROR:  syntax error at or near "keyllhjj"
LINE 5: foreign keyllhjj);
                ^
college=# create table student(
college(# stu_id serial primary key,
college(# f_name varchar(50),
college(# l_name varchar(50),
college(# f_phone int,
college(# l_phone int,
college(# b_date date,
college(# image text);
CREATE TABLE
college=# create table course(
college(# co_id serial primary key,
college(# stu_id int,
college(# duration int,
college(# p_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(p_id) references professor(p_id));
CREATE TABLE
college=# create table enrollment(
college(# e_id serial primary key,
college(# co_id int,
college(# stu_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(co_id) references course(co_id));
CREATE TABLE
college=# create table exams(
college(# ex_id serial primary key,
college(# e_id int,
college(# date date,
college(# time time,
college(# duration int,
college(# foreign key(e_id) references enrollment(e_id));
CREATE TABLE
college=# create table address(
college(# add_id serial primary key,
college(# government varchar(50),
college(# city varchar(50),
college(# address1 varchar(50) not null,
college(# address2 varchar(50) null);
CREATE TABLE
college=# create table stu_address(
college(# sa_id serial primary key,
college(# add_id int,
college(# stu_id int,
college(# foreign key(stu_id) references student(stu_id),
college(# foreign key(add_id) references address(add_id));
CREATE TABLE
college=# insert into faculty values(1,'commerce');
INSERT 0 1
college=# insert into department values(1,'bis',1);
INSERT 0 1
college=# insert into department values(2,'hr',1),(3,'accounting',1);
INSERT 0 2
college=# insert into subject values(1,'accounting','123',1);
INSERT 0 1
college=# insert into subject values(2,'hr','124',1),(3,'pr','125',1);
INSERT 0 2
college=# insert into subject values(4,'eco','126',2),(5,'pr','127',2),(6,'math','128',2);
ERROR:  insert or update on table "subject" violates foreign key constraint "subject_f_id_fkey"
DETAIL:  Key (f_id)=(2) is not present in table "faculty".
college=# 

