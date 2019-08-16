-- 1.左外连接:左表:Teacher,右表:Course,关联条件:teacher.course_id=course.id
/*select * from teacher left join course
 on teacher.course_id=course.id;
*/
-- 2.左外连接:左表:Course,右表:Teacher,关联条件:teacher.course_id=course.
/*
select  * from course left join teacher
on teacher.course_id=course.id;
*/
-- 3.右外连接:左表:Teacher,右表:Course,关联条件:teacher.course_id=course.id
/*
select * from teacher right join course
 on teacher.course_id=course.id;
 */
-- 4.右外连接:左表:Course,右表:Teacher,关联条件:teacher.course_id=course.id
/*
select * from course right join teacher
 on teacher.course_id=course.id;
*/

-- 5.完整外连接
/*
select * from teacher full join course
 on teacher.course_id=course.id;
*/
-- 没参加考试的学生信息
/*
select * from student left join Score
on student.id=Score.stu_id
where Score.score is null;
*/
-- 6.子查询:查询student表中比'李四'年龄大的学员信息
/*
select * from student where age in
(select age from student where name='耿耿')
*/

-- 练习:

-- 查询 '齐天大圣'教过的课程的学员信息
-- select course_id from teacher where name='齐天大圣'
-- 从score中查询出score——id的值为1的stu_id
/*
select stu_id from Score where course_id=(
    select course_id from teacher where name='齐天大圣'
    );
*/
-- 从student中查出id在以上结果中出现过的学员信息
/*
-- 1.查询考过'齐天大圣'老师所交课程的学员的信息
select * from student where id in (
select stu_id from Score where course_id=(
    select course_id from teacher where name='齐天大圣'
 ));
*/
/*
select * from Score where score is not null
*/
/*
-- 2.查询在score表中有成绩的学员信息
select *from student where id in(select stu_id from Score);
*/
/*
-- 3.查询'python基础'课程并且分数在80分以上的学员的姓名和毕业院校
select name,school from student where id in(
select stu_id from Score where course_id=(select id from course where cname='python基础')and score > 80   );
*/
-- 4.查询和'张三'相同班级以及相同专业同学的信息
/*
select  * from student where name != '耿耿' and class_id=(
select class_id from student where name = '耿耿') and major_id=(
select major_id from student where name = '耿耿')
*/































































