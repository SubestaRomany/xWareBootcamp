
postgres=# create database  university;
\CREATE DATABASE
postgres=# \c university;
You are now connected to database "university" as user "postgres".
university=# create table faculty(
university(# f_id int primary key,
university(# f_name varchar(50) not null);
CREATE TABLE
university=# create table department(
university(# d_id int primary key,
university(# d_name varchar(50) not null,
university(# f_id int,
university(# foreign key(f_id) references faculty(f_id));
CREATE TABLE

university=# create table address(
university(# a_id int primary key,
university(# government varchar(50) not null,
university(# city varchar(50) not null,
university(# address_1 varchar(50) not null,
university(# address_2 varchar(50) null);
CREATE TABLE

university=# create table stu_address(
university(# stu_a_id int primary key,
university(# a_id int,
university(# stu_id int,
university(# foreign key(a_id) references address(a_id));
CREATE TABLE

university=# create table professor(
university(# p_id int primary key,
university(# f_id int,
university(# d_id int,
university(# f_name varchar(50) not null,
university(# l_name varchar(50) not null,
university(# age int,
university(# salary float  not null,
university(# image text  not null);
CREATE TABLE
university=# create table subjects(
university(# sub_id int primary key,
university(# sub_name varchar(50) not null,
university(# sub_code int unique,
university(# f_id int,
university(# foreign key (f_id) references faculty(f_id));
CREATE TABLE
university=# create table course(
university(# c_id int primary key,
university(# sub_id int,
university(# duration float,
university(# p_id int,
university(# foreign key(sub_id) references subjects(sub_id),
university(# foreign key(p_id) references professor(p_id));
CREATE TABLE

university=# create table student(
university(# stu_id int primary key,
university(# f_name varchar(50) not null,
university(# l_name varchar(50) not null,
university(# f_phone int not null,
university(# l_phone int not null,
university(# b_date date not null,
university(# image text not null);
CREATE TABLE
university=# create table c_enrollment(
university(# c_e_id int primary key,
university(# c_id int,
university(# stu_id int,
university(# foreign key(c_id) references course(c_id),
university(# foreign key(stu_id) references student(stu_id));
CREATE TABLE

university=# create table exams(
university(# e_id int primary key,
university(# c_id int,
university(# e_date date,
university(# time time,
university(# duration int,foreign key(c_id) references course(c_id));
CREATE TABLE


