Q1 :Select Subject id, Subject Name, Subject Code, Course Duration in One Query
Answer :
select s_id,s_name,s_code,c_duration from subject inner join course using(s_id);
  
Q2 :Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query
Answer :
select s_id,s_name,s_code,c_duration ,pro_f_name, pro_l_name from subject join professor using(f_id) join course using(p_id);

Q3 :Select All Students With Thier Address In one Query
Answer :

select * from student inner join stu_address using(stu_id) inner join address using(add_id);

Q4 :Select All Students With Thier Course In one Query
Answer :

select (f_name,l_name) as student_name from student inner join course using(stu_id);

* LeetCode Exercises 

Q1 :Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
Answer:

select * from person left join address using(persinId);

Q2 :Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Answer:

select employee_id from employees e left join salaries s using (employee_id) where e.name is null or s.salary is null 
union
select employee_id from employees e right join salaries s using (employee_id) where e.name is null or s.salary is null 
order by employee_id;


