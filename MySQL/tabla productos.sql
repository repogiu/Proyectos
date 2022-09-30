 CREATE TABLE products (
   id int not null auto_increment,
   name varchar(50) not null,
   created_by int not null,
   marca varchar(100) not null,
   primary key(id),
   foreign key(created_by) references user(id)
 );
 -- cambiamos el nombre de la tabla
 rename table products to product;
 
 -- otra forma de insertar valores
 insert into product (name, created_by, marca)
 values
 ('ipad',1,'apple'),
 ('iphone',1,'apple'),
 ('watch',2,'apple'),
 ('macbook',1,'apple'),
 ('imac',3,'apple'),
 ('ipad mini',2,'apple');
 
 -- mostramos
 select * from product;
 
 -- Left join: la tabla user es la principal. Arroja todos los registros de la tabla de usuarios y los que estan asociados a productos
 select u.id, u.email, p.name from user u left join product p on u.id = p.created_by;
 
  -- Right join: la tabla product es la principal. Arroja todos los registros de la tabla de product y los usuarios asociados si existe.
 select u.id, u.email, p.name from user u right join product p on u.id = p.created_by;
 
  -- Inner join: solo trae los productos y usuarios asociados.
 select u.id, u.email, p.name from user u inner join product p on u.id = p.created_by;
 
   -- Cross join: producto cartesiano entre las tabla user y product (cada producto se cruza con todos los usuarios)
 select u.id, u.name, p.id, p.name from user u cross join product p;
 
 -- Group by - count: instruccion que agrupa varios elementos
 -- agrupamos por la marca ( cuenta la cantidad de producto por marca)
 select count(id), marca from product group by marca;
 
 -- mostramos cantidad de productos creados por los usuarios
 select count(p.id), u.name from product p left join user u on u.id= p.created_by group by p.created_by;
 
 -- Having: Group by con condicion
 -- mostramos registros mayores a 2
 select count(p.id), u.name from product p left join user u 
 on u.id= p.created_by group by p.created_by
 having count(p.id)>=2;
 
 -- Eliminar tabla
 drop table product;
 drop table animales;
 drop table user;
 
 