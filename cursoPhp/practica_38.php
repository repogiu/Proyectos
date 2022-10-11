<?php 
// abrir un archivo txt en php

$archivo ="contenido.txt";
// abrir archivo modo lectura (r)
$abrirArchivo =fopen($archivo, "r");
// leemos el contenido del archivo
$contenido =fread($abrirArchivo, filesize($archivo));

echo $contenido;

?>