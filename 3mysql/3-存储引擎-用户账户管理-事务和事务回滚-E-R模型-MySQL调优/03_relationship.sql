-- 1.创建wife表实现与teacher之间的一对一的关系
/*
create table wife(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    teacher_id int,
    constraint fk_teacher_wife foreign key(teacher_id)
    references teacher(id),
    unique (teacher_id)
)
*/
-- 2.插入数据
/*
    insert into wife(name,age,teacher_id)
values('吕老太',83,);
*/
/*
create table goods(id int primary key auto_increment,gname varchar(32) not null
,gprice int not null);
*/
/*
insert into goods(gname,gprice)
values ('Honner50',23459),('Huawei',6576548),('ipone',5);
*/
/*
create table shoppingcart(
id int primary key auto_increment,
t_id int not null,g_id int not null,count int default 1,
constraint fk_teacher_shoppingcart foreign key (t_id)
references teacher(id),
constraint fk_goods_shoppingcart foreign key (g_id)
references goods(id))
*/

insert into shoppingcart(t_id,g_id,count)
values (1,2,1),(1,3,1),(3,1,10),(3,2,1),(3,3,1);













