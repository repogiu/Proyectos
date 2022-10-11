<?php 
// Destruir variable de session: cej: cuando se paga un carrito de compra, la variable de session debe destruirse

session_start();
session_destroy();

echo "Sesión destruida";

?>