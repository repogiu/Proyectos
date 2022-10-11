<?php 
// variables de session: autenticacion, mantener informacion en cualquier pagina mientras el navegador este abierto
session_start();
// DECLARACION DE VARIABLES TIPO SESSION
$_SESSION['usuario']="giu";
$_SESSION['estado']="logueado"; // puede almacenar cualquier tipo de dato

echo "Sesión iniciada"."<br/>";

echo "Usuario: ".$_SESSION['usuario']."<br/>". "estado: ".$_SESSION['estado'];



?>