-- 单行注释(--后+空格)
/*多行注释*/
-- 创建course表:id,cname,cduration
/*
create table course(
    id int primary key auto_increment,
    cname varchar(30) not null,
    cduration int not null
);
-- 向course表中插入数据
insert into course(cname,cduration)
values('Python基础',20),('Python高级',15),
('WEB基础',9),('Python Web',15),
('爬虫',10),('数据分析&人工智能',20)


-- 创建teacher表:id,name,age,gender,hobby,course_id
-- course_id是外键,引用自course表的主键id
create table teacher(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender varchar(2) not null,
    hobby varchar(50) not null,
    -- 创建外键列
    course_id int,
    -- 外键约束
    constraint fk_course_teacher foreign key(course_id)
    references course(id)
)


-- 向 teacher 表中插入测试数据
insert into teacher
values
(null,'齐天大圣',28,'M','工作','1'),
(null,'猪八戒',28,'M','吃','2'),
(null,'沙僧',28,'M','劳动','3'),
(null,'小龙女',18,'F','买买买','4')
*/
/*
-- 创建major：id,m_name

create table major(
    id int primary key auto_increment,
    m_name varchar(30) not null
);
-- 向major插入数据
insert into major(m_name)
values('AID'),('UID'),('JSD'),('WEB');
*/
/*
-- 创建student表:id,name,age,gender,school,class_id,major_id
create table student(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender char(2) not null,
    school varchar(100) not null,
    class_id int not null,
    major_id int not null
)
*/
/*
-- 更新student表,增加外键关系在major_id上,引用自major表的主键id
alter table student
add constraint fk_major_student
foreign key(major_id)
references major(id);
*/
/*
-- 向student 表中插入数据
insert into student
values
(null,'马柳柳',18,'M','哈佛大学',5,1),
(null,'耿耿',19,'M','麻省理工大学',4,1),
(null,'王二麻子',26,'F','蓝翔技校',4,3),
(null,'朱俊',19,'F','五道口技术学院',4,1)
*/
/*
-- 创建Classinfo表: id,classname,status
create table Classinfo(
    id int primary key auto_increment,
    classname int not null,
    status int not null
);
*/
/*
alter table student
add constraint fk_Classinfo_student
foreign key(class_id)
references Classinfo(id);
*/
/*
-- 向classinfo 表中插入数据
insert into  Classinfo
values
(null,1901,0),
(null,1902,1),
(null,1903,1),
(null,1904,1),
(null,1905,1)
*/
/*
-- 创建Score表: id,stu_id,course_id,score
create table Score(
    id int primary key auto_increment,
    stu_id int not null,
    course_id int not null,
    score int not null
)
*/
/*
-- 向score 表中插入数据
insert into Score
values
(null,1,1,98),
(null,2,1,99),
(null,1,2,86),
(null,4,3,68)
*/
/*
alter table Score

add constraint fk_student_Score foreign key(stu_id)
references student(id)
*/
/*
add constraint fk_course_Score foreign key(course_id)
references course(id);
*/
/*
insert into Score
values
(null,1,3,98),
(null,2,2,94),
(null,2,4,67),
(null,3,2,76),
(null,3,3,88),
(null,3,4,85)
*/
-- 删除score表中的fk_student_score外键
/*
alter table Score drop foreign key fk_student_Score
*/
-- 增加Score表中的stu_id增加外键，引用自student主键id，并设置级联操作
/*
alter table Score
add constraint fk_student_score
foreign key(stu_id)
references student(id)
on delete cascade
on update cascade
*/

-- 使用内连接查询teacher和course表中的数据(姓名，年龄，课程，名称，课时)
/*
select t.name,t.age,c.cname,c.cduration
from teacher as t
inner join course as c
on t.course_id=c.id
*/
-- 1.查询学员的姓名，年龄，所在班级名称，专业名称,并筛选出1904的学员
-- 2.查询学生的姓名，毕业院校，所在班级，考试科目，考试成绩
/*
select s.name,s.age,C.classname ,m.m_name
from student as s
inner join Classinfo as C on s.class_id=C.id
inner join major as m on s.major_id=m.id
where C.Classname='1904';
*/
select s.name,s.school,C.Classname,cou.cname,Sc.score
from student as s
inner join Classinfo as C on s.Class_id=C.id
inner join Score as Sc on s.id=Sc.stu_id
inner join course as cou on Sc.course_id=cou.id









