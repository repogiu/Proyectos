<?php 
// crear un archivo en php
// escritura de archivo

$nombreArchivo= "archivo.txt";
$contenidoArchivo= "Hola, me converti en un archivo";
// abrir el archivo en modo de escritura
$crearArchivo= fopen($nombreArchivo,"w");
// Escribimos el contenido 
fwrite($crearArchivo,$contenidoArchivo);
// cerramos el archivo 
fclose($crearArchivo);

?>