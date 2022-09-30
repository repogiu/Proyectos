 CREATE TABLE user (
   id int not null auto_increment,
   name varchar(50) not null,
   edad int not null,
   email varchar(100) not null,
   PRIMARY KEY (id)
 );
 INSERT INTO user (name,edad,email) VALUES ('Oscar','25','oscar@gmail.com');
 INSERT INTO user (name,edad,email) VALUES ('Layla','15','layla@gmail.com');
 INSERT INTO user (name,edad,email) VALUES ('Nicolas','36','layla@gmail.com');
 INSERT INTO user (name,edad,email) VALUES ('Chanchito','7','chanchito@gmail.com');
 
 -- obtener datos
 select * from user;
 -- funcion limit: limite la cantidad de recursos que va a retornar
 -- limit 1: retorna el primer registro que encuentre
 select * from user limit 1;
 -- condicion: where
 select * from user where edad > 15;
 
 -- operadores logicos
 select * from user where edad > 20 and email = 'layla@gmail.com';
 select * from user where edad > 20 or email = 'layla@gmail.com';
 select * from user where email != 'layla@gmail.com';
 
 -- between and
 select * from user where edad between 15 and 30;
 -- otra forma de consultar: no importa el inicio y el final 
 select * from user where email like '%gmail%';
  -- debe terminar en gmail: retorna nulo
 select * from user where email like '%gmail';
 -- debe comenzar en oscar y no importa el final
 select * from user where email like 'oscar%';
 
 -- orden ascendente con order by
 select * from user order by edad asc;
  -- orden descendente con order by
 select * from user order by edad desc;
 
 -- valor maximo
 select max(edad) as mayor from user;
 -- valor minimo
 select min(edad) as menor from user;
 
 -- sin asterico
 select id, name from user;
 
 -- cambiar el nombre de la colunma
 select id, name as nombre from user;
 
 
 
 
 