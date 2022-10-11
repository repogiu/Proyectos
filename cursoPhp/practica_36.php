
<!-- incluimos contenido con la funcion include
En caso de obtenerse un error en la fx include, continua mostrando el resto del contenido
include_ once: evita la duplicidad de include -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php include "practica_36_1.php"?>
    <br/>
    <?php include_once "practica_36_1.php"?>
    <br/>
    <?php echo "Hola, estoy en la pagina principal"; ?>
    
</body>
</html>