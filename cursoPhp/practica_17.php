<?php 
// Funciones
// $apellido=""  valor por defoult vacio para no enviar apellido
function imprimirNombre($nombre,$apellido="") {
    echo "Hola ".$nombre." ".$apellido."<br>";

}

// LLamada a la funcion
 imprimirNombre("Giuliana");
 imprimirNombre("Gael","Diaz");
 imprimirNombre("Mateo","Valdez");

?>