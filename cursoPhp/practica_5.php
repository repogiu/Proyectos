<!--String y concatenacion -->
<?php 
// Recibir informacion del formulario HTML (Metodo Post)
if($_POST){ // para que no aparezca error, hacer un if, que si hay envio de informacion imprimir nombre
    $nombre=$_POST['txtNombre'];
    $apellido=$_POST['txtApellido'];
    echo "Hola ".$nombre. " ". $apellido;
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="practica_5.php" method="post">
        Nombre:
        <!--atajo:input:t --> 
        <input type="text" name="txtNombre" id="">
        <br/>
        Apellido:
        <input type="text" name="txtApellido" id="">
        <br/>
        <!--atajo:input:button --> 
        <input type="submit" value="Enviar"> 
    
</body>
</html>