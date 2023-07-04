create database estudiantes;
use estudiantes;
create table estudiantes2022(
idestudiantes2022 int auto_increment primary key,
nombre varchar(50),
apellido varchar(50),
telefono varchar (12),
email varchar (80)
);

/*Comenzamos con CRUD: create(crear), read(leer), update(actualizar), delete(eliminar)*/

-- Listar los estudiantes (read)
SELECT * FROM estudiantes2022;

-- Insertar estudiante (create)
INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES('Juan', 'Perez', '12233333', 'jperez@mail.com');

-- Modificar estudiante (update)
UPDATE estudiantes2022 SET nombre='Juan Carlos', apellido='Garcia' WHERE idestudiantes2022=1;

-- Eliminar registro (Delete)
DELETE FROM estudiantes2022 WHERE idestudiantes2022=3;

-- Para modificar el idestudiantes2022 y comience en 1
ALTER TABLE estudiantes2022 auto_increment = 1;

