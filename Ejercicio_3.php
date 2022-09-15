<?php 
//Programa que muestra la fecha actual
date_default_timezone_set("America/Argentina/Cordoba");

$fecha = date("d-m-Y h:i A");

echo "<p> Fecha y hora actual  <br/> 
        $fecha </p>";



?>