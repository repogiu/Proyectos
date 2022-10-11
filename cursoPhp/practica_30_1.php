<?php 
// Acceso a la informacion desde otra pagina
session_start();

// funcion isset: para saber si hay algo vacio

if (isset($_SESSION['usuario'])) {

    echo "Sesión iniciada"."<br/>";

} else {
    echo "No hay datos";
}

?>