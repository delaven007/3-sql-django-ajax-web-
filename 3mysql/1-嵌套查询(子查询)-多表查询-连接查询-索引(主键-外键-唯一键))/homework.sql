-- 2.
/*
create table comment(comment_id int primary key auto_increment,
ariticle_id int not null, user_id int not null ,data datetime);
*/
/*
insert into comment(article_id,user_id)
values(10000,10000),(10001,10001),(10002,10000),
(10003,10015),(10004,10006),(10025,10006),(10009,10000);
*/
/*
select user_id,article_id from comment  order by article_id desc limit 10;
*/
-- 3.顾客信息表,完成后插入3条表记录
/*
create table customers(c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint,
c_sex enum('M','F'),
c_city varchar(20),
c_salary float(10.2) );
*/
-- 顾客订单表(在表中插入5条记录)
create table orders(o_id int,
o_name varchar(30),
o_price float(10.2),
constraint fk_orders_customers foreign key(o_id)
references customers(c_id)
on delete cascade
on update cascade);
























