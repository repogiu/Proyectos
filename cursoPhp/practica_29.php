<?php 
// Leer datos de mysql con php
$servidor="localhost"; // 127.0.0.1
$usuario="root"; // usuario por defoult
$contrasenia=""; 


try{   
    $conexion=new PDO("mysql:host=$servidor;dbname=album",$usuario,$contrasenia);
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
 // lectura de datos en php
    $sql="SELECT * FROM `fotos`";
    $sentencia=$conexion->prepare($sql);
    $sentencia->execute();

    $resultado = $sentencia->fetchAll();
// impresion
    print_r($resultado);
    echo "<br/>";

    foreach ($resultado as $fotos) {    
        echo $fotos['nombre']."<br/>";
        
    echo "Conexión establecida";

}
}


catch(PDOException $error){  
    echo "Conexion errónea".$error;
}




?>