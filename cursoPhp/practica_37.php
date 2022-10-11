<!-- require: funciona igual que include, pero si el archivo que vincule muestra un error, no sigue ejecutando las otras lineas de codigo -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=php, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php require("practica_37_1.php"); ?> 
    <br/>
    <?php require_once("practica_37_1.php"); ?> 
    <br/>
    <?php echo "Hola, estoy en la pagina principal 
    "; ?>
</body>
</html>