-- para crear una base de datos
create database holamundo;
-- para ver registro de todas la base de datos
show databases;
-- indica que bd tenemos que utilizar antes de ejecutar la consulta
use holamundo;
-- crear tabla
CREATE TABLE animales (
id int,
tipo varchar(255),
estado varchar(255),
PRIMARY KEY(id)
);
-- insertar datos dentro de la tabla
-- INSERT INTO animales (tipo,estado) VALUES ('chanchito','feliz');
-- modificar tabla creada
 ALTER TABLE animales MODIFY COLUMN id int auto_increment;
 SHOW CREATE TABLE animales;
 use holamundo;
 SHOW CREATE TABLE animales;
 ALTER TABLE animales;
 SHOW CREATE TABLE animales;
 CREATE TABLE `animales` (
   `id` int NOT NULL AUTO_INCREMENT,
   `tipo` varchar(255) DEFAULT NULL,
   `estado` varchar(255) DEFAULT NULL,
   PRIMARY KEY (`id`)
 );
 INSERT INTO animales (tipo,estado) VALUES ('chanchito','feliz');
 INSERT INTO animales (tipo,estado) VALUES ('dragon','feliz');
 INSERT INTO animales (tipo,estado) VALUES ('felipe','triste');
 
 -- Listar todos los registros ingresados
 SELECT * FROM animales;
 -- Seleccionar un solo registro
 SELECT * FROM animales WHERE id=1;
 SELECT * FROM animales WHERE estado='feliz';
 SELECT * FROM animales WHERE estado='feliz' AND tipo = 'chanchito';
 -- actualizar tabla con id
 UPDATE animales SET estado = 'feliz' WHERE id=4;
 
 SELECT * FROM animales;
 -- Eliminar registros por id
 DELETE from animales WHERE id=2;
 SELECT * FROM animales;
 DELETE from animales WHERE id=5;
 SELECT * FROM animales;
 
 
 