<?php
// valores input file: permite adjuntar imagenes o archivo

if ($_POST) {
    // la recepcion por el metodo post, solo recibe el nombre del archivo
    print_r($_POST);
    echo "<br/>"; 
    // primero se accede al nombre del input y luego el dato que quiero obtener (nombre, nombre temporal, tamaño)
    print_r($_FILES); 
    echo "<br/>"; // muestra el nombre temporal, tipo de imagen, nombre, tamaño
    print_r($_FILES["archivo"]["name"]);
    echo "<br/>";
// movemos el archivo temporal y lo o copiamos con el mismo nombre que la imagen original  a nuestra carpeta o servidor 
    move_uploaded_file($_FILES["archivo"]["tmp_name"], $_FILES["archivo"]["name"]);
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
    <!-- la propiedad enctype: activa la compatibilidad de adjuntar una imagen -->

    <form action="practica_32.php" enctype="multipart/form-data" method="post">
        Imagen:
        <!-- el input file no se puede poner un valor predeterminado o por default -->
       
        <input type="file" name="archivo" id="">
        <br/>
        <input type="submit" name="btn" value="Enviar">

    </form>

</body>

</html>