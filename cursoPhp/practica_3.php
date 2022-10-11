<?php 
//Recepcion de informacion de formulario html (Metodo Get)
if($_GET){
    $nombre=$_GET["nombre"];
    echo "Hola ".$nombre;
} // imprime Hola "" pero no muestra el formulario html

?>