<?php 
// conexion de php con mysql
$servidor="localhost"; // 127.0.0.1
$usuario="root"; // usuario por defoult
$contrasenia=""; 

// Uso de try y catch: condicional de erroes
try{   // si no sucede ningun error, el sistema genera la conexion
    $conexion=new PDO("mysql:host=$servidor;dbname=album",$usuario,$contrasenia);
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
 // insercion de datos en php
    $sql= "INSERT INTO `fotos` (`id`, `nombre`, `ruta`) VALUES (NULL, 'Sentencia SQL', 'foto.jpg')";
    // ejecucion de la instruccion anterior con el metodo de PDO (exec) 
    $conexion-> exec($sql);
    echo "Conexión establecida";

}
catch(PDOException $error){  // si sucede un error, voy a mostrar el error con la instruccion catch
    echo "Conexion errónea".$error;
}




?>