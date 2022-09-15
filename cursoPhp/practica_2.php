<?php 
// Recibir informacion del formulario HTML (Metodo Post)
if($_POST){ // si hay envio de informacion imprimir nombre
    $nombre=$_POST['txtNombre'];
    echo "Hola ".$nombre;
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
</head>
<body>
    <!--Creacion de formulario -->
    <form action="practica_1.php" method="post">
        Nombre:
        <!--atajo:input:t --> 
        <input type="text" name="txtNombre" id="">
        <br/>
        <!--atajo:input:button --> 
        <input type="submit" value="Enviar"> 


    </form>
    

    
</body>
</html>