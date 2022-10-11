<?php 
// Conversion del formato JSON (string) que nos envian algunas apis en objeto, arreglo, etc...

$json='[
    {"nombre":"Giuliana", "apellido":"Diaz Luna"},{"nombre":"Gael", "apellido":"Diaz"}]';

$conversion = json_decode($json);


//print_r($conversion);


foreach($conversion as $persona){
    // print_r($persona);
    // print_r($persona->nombre);
    echo ($persona->nombre)." ".($persona->apellido)."<br/>";
}

?> 